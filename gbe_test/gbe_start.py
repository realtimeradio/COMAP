#!/bin/env ipython

import corr, time, struct, sys, logging, socket, datetime

i = int(sys.argv[1])

roach = '192.168.1.'+str(100+i)
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(1)
if fpga.is_connected():
	print 'Connected to %s...' %(roach)
	fpga.write_int('reg_arm',0)
	fpga.write_int('reg_arm',1)
else:
	print 'Failed to connect to %s...' %(roach)
