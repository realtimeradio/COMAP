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


time.sleep(0.1)
fpga.write_int('snap_inp1_ctrl',0)
fpga.write_int('snap_inp2_ctrl',0)
fpga.write_int('snap_inp3_ctrl',0)
fpga.write_int('snap_inp4_ctrl',0)

time.sleep(0.1)
fpga.write_int('snap_inp1_ctrl',1)
fpga.write_int('snap_inp2_ctrl',1)
fpga.write_int('snap_inp3_ctrl',1)
fpga.write_int('snap_inp4_ctrl',1)


# each bram holds 128 32-bit numbers for 4 steams.
time.sleep(0.1)
bramsnap1 = struct.unpack('>512I',fpga.read('snap_inp1_bram',128*8*2))
bramsnap2 = struct.unpack('>512I',fpga.read('snap_inp2_bram',128*8*2))

bramsnap3 = struct.unpack('>512I',fpga.read('snap_inp3_bram',128*8*2))
bramsnap4 = struct.unpack('>512I',fpga.read('snap_inp4_bram',128*8*2))


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

	bramsnapQ[i]     = bramsnap3[k]
	bramsnapQ[i+128] = bramsnap3[k+1]
	bramsnapQ[i+256] = bramsnap3[k+2]
	bramsnapQ[i+384] = bramsnap3[k+3]

	bramsnapQ[i+512] = bramsnap4[k]
	bramsnapQ[i+640] = bramsnap4[k+1]
	bramsnapQ[i+768] = bramsnap4[k+2]
	bramsnapQ[i+896] = bramsnap4[k+3]

	#j=j+8
	k=k+4


#bramsnapI = np.concatenate([bramsnap1,bramsnap2,bramsnap3,bramsnap4,bramsnap5,bramsnap6,bramsnap7,bramsnap8])
#bramsnapQ = np.concatenate([bramsnap1a,bramsnap2a,bramsnap3a,bramsnap4a,bramsnap5a,bramsnap6a,bramsnap7a,bramsnap8a])

plt.subplot(2,1,1)
plt.semilogy((bramsnapI))
plt.subplot(2,1,2)
plt.semilogy((bramsnapQ))
plt.show()


