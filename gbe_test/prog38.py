#!/bin/env ipython

import corr, time, struct, sys, logging, socket, datetime

boffile = '/home/jkocz/transfer/gbe_test_sync/bit_files/gbe_test_sync_2017_May_26_0856.bof'

for i in range (1,3):
	roach = '192.168.1.'+str(100+i)
	fpga = corr.katcp_wrapper.FpgaClient(roach)
	time.sleep(1)
	if fpga.is_connected():
		print 'Connected to %s...' %(roach)
		fpga.upload_bof(boffile,5001)
	else:
		print 'Failed to connect to %s...' %(roach)
