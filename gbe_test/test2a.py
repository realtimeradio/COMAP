#!/bin/env ipython

import corr, time, struct, sys, logging, socket

#Decide where we're going to send the data, and from which addresses:
dest_ip  =192*(2**24) + 168*(2**16) + 11*(2**8) + 40
fabric_port=60000         
source_ip= 192*(2**24) + 168*(2**16) + 11*(2**8) + 42
mac_base=(2<<40) + (2<<32)

pkt_period = 2**16 #how often to send another packet in FPGA clocks (200MHz)
payload_len = 64 #how big to make each packet in 64bit words

tx_core_name = 'one_GbE'

boffile = 'tut2.bof'

roach = '192.168.1.102'

print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(1)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()
    
fpga.write_int('pkt_sim_enable', 0)
print 'done'

print '---------------------------'
print 'Configuring transmitter core...',
sys.stdout.flush()
fpga.tap_start('tap3',tx_core_name,mac_base+source_ip,source_ip,fabric_port)
print 'done'

print '---------------------------'
print 'Setting-up packet source...',
sys.stdout.flush()
fpga.write_int('pkt_sim_period',pkt_period)
fpga.write_int('pkt_sim_payload_len',payload_len)
print 'done'

print 'Setting-up destination addresses...',
sys.stdout.flush()
fpga.write_int('dest_ip',dest_ip)
fpga.write_int('dest_port',fabric_port)
print 'done'

print 'Resetting cores and counters...',
sys.stdout.flush()
fpga.write_int('rst', 3)
fpga.write_int('rst', 0)
print 'done'

time.sleep(2)

fpga.print_10gbe_core_details(tx_core_name,arp=True)

print 'Enabling output...',
sys.stdout.flush()
fpga.write_int('pkt_sim_enable', 1)
print 'done'

