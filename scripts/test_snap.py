#!/usr/bin/env python

import numpy as np
import corr, time, struct, sys, logging, socket
import h5py
import matplotlib.pyplot as plt
import hittite

roach = '192.168.42.65'

print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(0.2)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()
    
# setup initial parameters
bramsnapI = np.zeros(1024)
bramsnapQ = np.zeros(1024)

# trigger all the snap blocks


fpga.write_int('in1',2**24+2**16+2**8+2**1)
fpga.write_int('in2',2**24+2**16+2**8+2**1+1)
fpga.write_int('in3',2**24+2**16+2**8+2**1+2)
fpga.write_int('in4',2**24+2**16+2**8+2**1+3)
fpga.write_int('in5',2**24+2**16+2**8+2**1+4)
fpga.write_int('in6',2**24+2**16+2**8+2**1+5)
fpga.write_int('in7',2**24+2**16+2**8+2**1+6)
fpga.write_int('in8',2**24+2**16+2**8+2**1+7)



time.sleep(0.1)
fpga.write_int('snap_inp1_ctrl',0)
fpga.write_int('snap_inp2_ctrl',0)

time.sleep(0.1)
fpga.write_int('snap_inp1_ctrl',3)
fpga.write_int('snap_inp2_ctrl',3)


# each bram holds 128 32-bit numbers for 4 steams.
time.sleep(0.1)
bramsnap1 = struct.unpack('>512I',fpga.read('snap_inp1_bram',128*8*2))
bramsnap2 = struct.unpack('>512I',fpga.read('snap_inp2_bram',128*8*2))


j=0
k=0
for i in range(0,128):
	bramsnapI[i]     = bramsnap1[k]
	bramsnapI[i+128] = bramsnap1[k+1]
	bramsnapI[i+256] = bramsnap1[k+2]
	bramsnapI[i+384] = bramsnap1[k+3]

	bramsnapI[i+512] = bramsnap2[k]
	bramsnapI[i+640] = bramsnap2[k+1]
	bramsnapI[i+768] = bramsnap2[k+2]
	bramsnapI[i+896] = bramsnap2[k+3]

	k=k+4


#plt.subplot(2,1,1)
plt.plot((bramsnapI))
plt.show()


