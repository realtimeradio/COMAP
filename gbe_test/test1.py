#!/bin/env ipython

import corr, time, struct, sys, logging, socket, datetime

def getCurrentDadaTimeUS():
  now = datetime.datetime.today()
  now_str = now.strftime("%Y%m%d%H%M%S%f")
  return now_str

def getUTCDadaTime(toadd=0):
  now = datetime.datetime.utcnow()
  if (toadd > 0):
    delta = datetime.timedelta(0, toadd)
    now = now + delta
  now_str = now.strftime("%Y-%m-%d-%H:%M:%S")
  return now_str

def wait_for_1sec_boundary():
        curr_time = int(time.time())
        next_time = curr_time
        while curr_time == next_time:
                next_time = int(time.time())

def wait_until_utc_sec(utcstr):
        cur_time = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")
        while cur_time != utcstr:
                cur_time = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")

rid = int(sys.argv[1])
startTime = str(sys.argv[2])
#print startTime

#Decide where we're going to send the data, and from which addresses:
dest_ip  =192*(2**24) + 168*(2**16) + 11*(2**8) + 40
fabric_port=60000         
source_ip= 192*(2**24) + 168*(2**16) + 11*(2**8) + (1+rid)
mac_base=(2<<40) + (2<<32)

pkt_period = 2**15 #how often to send another packet in FPGA clocks (200MHz)
payload_len = 8192 #how big to make each packet in 64bit words

tx_core_name = 'one_GbE'

#boffile = 'gbe_test_2017_Apr_18_1654.bof'
boffile = 'gbe_test_2017_May_23_1607.bof'

roach = '192.168.1.'+str(100+rid)


print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(1)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()

fpga.progdev(boffile)
time.sleep(1)
    
fpga.write_int('pkt_sim_enable', 0)
#print 'done'

fpga.write_int('pkt_sim_rid',rid-1)
#print '---------------------------'
#print 'Configuring transmitter core...',
sys.stdout.flush()
fpga.tap_start('tap3',tx_core_name,mac_base+source_ip,source_ip,fabric_port)
#print 'done'

#print '---------------------------'
#print 'Setting-up packet source...',
sys.stdout.flush()
fpga.write_int('pkt_sim_period',pkt_period)
fpga.write_int('pkt_sim_payload_len',payload_len)
#print 'done'

#print 'Setting-up destination addresses...',
sys.stdout.flush()
fpga.write_int('dest_ip',dest_ip)
fpga.write_int('dest_port',fabric_port)
#print 'done'

#print 'Resetting cores and counters...',
sys.stdout.flush()
fpga.write_int('rst', 3)
fpga.write_int('rst', 0)
#print 'done'

time.sleep(2)

#fpga.print_10gbe_core_details(tx_core_name,arp=True)

print 'Enabling output...%s\n' %(roach)
sys.stdout.flush()
fpga.write_int('pkt_sim_enable', 1)
#print 'done'
print 'Waiting for start time %s\n' %(startTime) 
fpga.write_int('reg_arm',0)
wait_until_utc_sec(startTime)
time.sleep(0.2)
fpga.write_int('reg_arm',1)
