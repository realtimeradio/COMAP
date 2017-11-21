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
numTones=2048
combCoeff = np.zeros((1024,numTones)) + 1j*np.zeros((1024,numTones))
combCoeffSingle = np.zeros(numTones) + 1j*np.zeros(numTones)
ssbI = np.zeros((1024,numTones))
ssbQ = np.zeros((1024,numTones))

hittiteFreq = 2e9
hittitePower = -15
hittiteIp = '192.168.43.102'
freqInc = 0.9765625e6*2
# initialise hittite
hittite.setAll(hittiteFreq,hittitePower,'on',hittiteIp,50000,doPrint=True,ret=False)


def defCoeffs():

        real = '0100000000000000'
        imag = '0100000000000000'
        coeff0 = (real + imag)
        coeff0 = int(coeff0,2)
        coeffArray = np.ones(1024,'I')*coeff0
        coeffStr = struct.pack('>1024I',*coeffArray)


        fpga.write('c1_0',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_1',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_2',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_3',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_4',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_5',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_6',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_7',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_0',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_1',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_2',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_3',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_4',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_5',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_6',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_7',coeffStr)
        time.sleep(0.5)

        real = '0000000000000000'
        imag = '0000000000000000'
        coeff0 = (real + imag)
        coeff0 = int(coeff0,2)
        coeffArray = np.ones(1024,'I')*coeff0
        coeffStr = struct.pack('>1024I',*coeffArray)

        fpga.write('c2_0',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_1',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_2',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_3',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_4',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_5',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_6',coeffStr)
        time.sleep(0.5)
        fpga.write('c2_7',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_0',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_1',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_2',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_3',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_4',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_5',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_6',coeffStr)
        time.sleep(0.5)
        fpga.write('c3_7',coeffStr)



def defCoeffs14():

        real = '0100000000000000'
        imag = '0000000000000000'
        coeff0 = (real + imag)
        coeff0 = int(coeff0,2)
        coeffArray = np.ones(1024,'I')*coeff0
        coeffStr = struct.pack('>1024I',*coeffArray)


        fpga.write('c1_0',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_1',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_2',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_3',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_4',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_5',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_6',coeffStr)
        time.sleep(0.5)
        fpga.write('c1_7',coeffStr)
        time.sleep(0.5)

        fpga.write('c4_0',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_1',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_2',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_3',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_4',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_5',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_6',coeffStr)
        time.sleep(0.5)
        fpga.write('c4_7',coeffStr)


def defCoeffs23():
        coeff2 = -1*(combCoeffSingle[0:1024])
        coeff3 = -1*(np.power(combCoeffSingle[1024:2048],-1))
        coeff3 = np.nan_to_num(coeff3)
        coeffs2  = ["" for i in range(1024)]
        coeffs2r = ["" for i in range(1024)]
        coeffs2i = ["" for i in range(1024)]
        coeffs3  = ["" for i in range(1024)]
        coeffs3r = ["" for i in range(1024)]
        coeffs3i = ["" for i in range(1024)]
        #print coeff2.real
        for i in range (0,1024):
                coeffs2r[i] = np.binary_repr(np.int16(coeff2[i].real*2**14),16)
                coeffs2i[i] = np.binary_repr(np.int16(coeff2[i].imag*2**14),16)
                coeffs3r[i] = np.binary_repr(np.int16(coeff3[i].real*2**14),16)
                coeffs3i[i] = np.binary_repr(np.int16(coeff3[i].imag*2**14),16)

                coeffs2[i] = (coeffs2r[i] + coeffs2i[i])
                coeffs3[i] = (coeffs3r[i] + coeffs3i[i])
                coeffs2[i] = int(coeffs2[i],2)
                coeffs3[i] = int(coeffs3[i],2)
        coeffArray2 = np.ones(1024,'L')*coeffs2
        coeffArray3 = np.ones(1024,'L')*coeffs3
        coeffStr2 = struct.pack('>1024L',*coeffArray2)
        coeffStr3 = struct.pack('>1024L',*coeffArray3)

        fpga.write('c2_0',coeffStr2[0:128])
        time.sleep(0.5)
        fpga.write('c2_1',coeffStr2[128:128*2])
        time.sleep(0.5)
        fpga.write('c2_2',coeffStr2[128*2:128*3])
        time.sleep(0.5)
        fpga.write('c2_3',coeffStr2[128*3:128*4])
        time.sleep(0.5)
        fpga.write('c2_4',coeffStr2[128*4:128*5])
        time.sleep(0.5)
        fpga.write('c2_5',coeffStr2[128*5:128*6])
        time.sleep(0.5)
        fpga.write('c2_6',coeffStr2[128*6:128*7])
        time.sleep(0.5)
        fpga.write('c2_7',coeffStr2[128*7:128*8])
        time.sleep(0.5)

        fpga.write('c3_0',coeffStr3[0:128])
        time.sleep(0.5)
        fpga.write('c3_1',coeffStr3[128:128*2])
        time.sleep(0.5)
        fpga.write('c3_2',coeffStr3[128*2:128*3])
        time.sleep(0.5)
        fpga.write('c3_3',coeffStr3[128*3:128*4])
        time.sleep(0.5)
        fpga.write('c3_4',coeffStr3[128*4:128*5])
        time.sleep(0.5)
        fpga.write('c3_5',coeffStr3[128*5:128*6])
        time.sleep(0.5)
        fpga.write('c3_6',coeffStr3[128*6:128*7])
        time.sleep(0.5)
        fpga.write('c3_7',coeffStr3[128*7:128*8])
        time.sleep(0.5)



# trigger all the snap blocks
def genCoeffs():
	for toneIter in range(0,numTones):
		
	
		#time.sleep(0.1)
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
		#time.sleep(0.1)
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
		
		ssbI[:,toneIter] = bramsnapI
		ssbQ[:,toneIter] = bramsnapQ
		
		hittite.setAll(hittiteFreq+((toneIter+1)*freqInc),hittitePower,'on',hittiteIp,50000,doPrint=True,ret=False)


#plt.subplot(2,1,1)
#plt.semilogy(np.abs(bramX_cplx))
#plt.plot((bramsnapI))
#plt.subplot(2,1,2)
#plt.semilogy(np.abs(bramsnapXa))
#plt.plot((bramsnapQ))
#plt.show()


def writeFiles():
	with h5py.File('lsb_post.h5','w') as hf:
		hf.create_dataset("ssbI",data=ssbI)
	with h5py.File('usb_post.h5','w') as hf:
		hf.create_dataset("ssbQ",data=ssbQ)

#defCoeffs()
genCoeffs()
writeFiles()
#defCoeffs14()
#defCoeffs23()
