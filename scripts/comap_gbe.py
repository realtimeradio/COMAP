#!/usr/bin/env python

import scipy, corr, time, struct, sys, logging, socket
import numpy as np
import matplotlib.pyplot as plt

roach = '192.168.42.65'

print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(0.1)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()

dest_ip = 192*(2**24) + 168*(2**16) + 41*(2**8) + 8
dest_port = 4002
fabric_port=60000
source_ip= 192*(2**24) + 168*(2**16) + 41*(2**8) + 13
mac_base=(2<<40) + (2<<32)


#ifpga.write_int('acc_valid_payload_len',128)
#fpga.write_int('acc_valid_period',819200)
fpga.write_int('dest_ip',dest_ip)
fpga.write_int('dest_port',dest_port)
fpga.write_int('rid',0)

fpga.write_int('gbe_tx_rst',1)
time.sleep(2)
#fpga.tap_start('gbe','one_GbE',mac_base+source_ip,source_ip,fabric_port)

dest_macff= 255*(2**40) + 255*(2**32) + 255*(2**24) + 255*(2**16) + 255*(2**8) + 255
arp_table = [dest_macff for i in range(256)]


fpga.config_10gbe_core('one_GbE',mac_base+source_ip,source_ip,fabric_port,arp_table)
#fpga.write_int('arm',1)
#fpga.write_int('pps',1)
#fpga.write_int('arm',0)
#fpga.write_int('pps',0)
fpga.write_int('gbe_tx_rst',0)
fpga.sleep(0.2)
fpga.write_int('arm_eth',1)

