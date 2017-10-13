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
numTones=1024
numTones=1
combCoeff = np.zeros((1024,numTones)) + 1j*np.zeros((1024,numTones))
ssbI = np.zeros((1024,numTones))
ssbQ = np.zeros((1024,numTones))

hittiteFreq = 4e9
hittitePower = 0
hittiteIp = '192.168.43.102'
freqInc = 0.9765625e6
# initialise hittite
#hittite.setAll(hittiteFreq,hittitePower,'on',hittiteIp,50000,doPrint=True,ret=False)

# trigger all the snap blocks

for toneIter in range(0,numTones):
	

	time.sleep(0.1)
	fpga.write_int('snap_inp1_ctrl',0)
	fpga.write_int('snap_inp2_ctrl',0)
	fpga.write_int('snap_inp3_ctrl',0)
	fpga.write_int('snap_inp4_ctrl',0)
	fpga.write_int('snap_inp5_ctrl',0)
	fpga.write_int('snap_inp6_ctrl',0)
	fpga.write_int('snap_inp7_ctrl',0)
	fpga.write_int('snap_inp8_ctrl',0)
	fpga.write_int('snap_inp9_ctrl',0)
	fpga.write_int('snap_inp10_ctrl',0)
	fpga.write_int('snap_inp11_ctrl',0)
	fpga.write_int('snap_inp12_ctrl',0)
	fpga.write_int('snap_inp13_ctrl',0)
	fpga.write_int('snap_inp14_ctrl',0)
	fpga.write_int('snap_inp15_ctrl',0)
	fpga.write_int('snap_inp16_ctrl',0)
	
	fpga.write_int('snap_inp1_ctrl',1)
	fpga.write_int('snap_inp2_ctrl',1)
	fpga.write_int('snap_inp3_ctrl',1)
	fpga.write_int('snap_inp4_ctrl',1)
	fpga.write_int('snap_inp5_ctrl',1)
	fpga.write_int('snap_inp6_ctrl',1)
	fpga.write_int('snap_inp7_ctrl',1)
	fpga.write_int('snap_inp8_ctrl',1)
	fpga.write_int('snap_inp9_ctrl',1)
	fpga.write_int('snap_inp10_ctrl',1)
	fpga.write_int('snap_inp11_ctrl',1)
	fpga.write_int('snap_inp12_ctrl',1)
	fpga.write_int('snap_inp13_ctrl',1)
	fpga.write_int('snap_inp14_ctrl',1)
	fpga.write_int('snap_inp15_ctrl',1)
	fpga.write_int('snap_inp16_ctrl',1)




	
	#fpga.write_int('rst',3)
	time.sleep(0.1)
	#fpga.write_int('rst',0)
	# each bram holds 128 64-bit numbers.
	time.sleep(0.1)
	bramsnap1 = struct.unpack('>128Q',fpga.read('snap_inp1_bram',128*8))
	bramsnap2 = struct.unpack('>128Q',fpga.read('snap_inp2_bram',128*8))
	bramsnap3 = struct.unpack('>128Q',fpga.read('snap_inp3_bram',128*8))
	bramsnap4 = struct.unpack('>128Q',fpga.read('snap_inp4_bram',128*8))
	bramsnap5 = struct.unpack('>128Q',fpga.read('snap_inp5_bram',128*8))
	bramsnap6 = struct.unpack('>128Q',fpga.read('snap_inp6_bram',128*8))
	bramsnap7 = struct.unpack('>128Q',fpga.read('snap_inp7_bram',128*8))
	bramsnap8 = struct.unpack('>128Q',fpga.read('snap_inp8_bram',128*8))
	
	bramsnap1a = struct.unpack('>128Q',fpga.read('snap_inp9_bram',128*8))
	bramsnap2a = struct.unpack('>128Q',fpga.read('snap_inp10_bram',128*8))
	bramsnap3a = struct.unpack('>128Q',fpga.read('snap_inp12_bram',128*8))
	bramsnap4a = struct.unpack('>128Q',fpga.read('snap_inp11_bram',128*8))
	bramsnap5a = struct.unpack('>128Q',fpga.read('snap_inp16_bram',128*8))
	bramsnap6a = struct.unpack('>128Q',fpga.read('snap_inp13_bram',128*8))
	bramsnap7a = struct.unpack('>128Q',fpga.read('snap_inp15_bram',128*8))
	bramsnap8a = struct.unpack('>128Q',fpga.read('snap_inp14_bram',128*8))

	bramsnapI = np.concatenate([bramsnap1,bramsnap2,bramsnap3,bramsnap4,bramsnap5,bramsnap6,bramsnap7,bramsnap8])
	bramsnapQ = np.concatenate([bramsnap1a,bramsnap2a,bramsnap3a,bramsnap4a,bramsnap5a,bramsnap6a,bramsnap7a,bramsnap8a])

plt.subplot(2,1,1)
plt.plot((bramsnapI))
plt.subplot(2,1,2)
plt.plot((bramsnapQ))
plt.show()




#with h5py.File('combCoeff.h5','w') as hf:
#	hf.create_dataset("combCoeff",data=combCoeff)

#with h5py.File('lsb.h5','w') as hf:
#	hf.create_dataset("ssbI",data=ssbI)
#with h5py.File('usb.h5','w') as hf:
#	hf.create_dataset("ssbQ",data=ssbQ)
