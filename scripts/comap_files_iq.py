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
#numTones=2048
#combCoeff = np.zeros((1024,numTones)) + 1j*np.zeros((1024,numTones))
#combCoeffSingle = np.zeros(numTones) + 1j*np.zeros(numTones)


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


def defCoeffs23(combCoeffSingle):
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

        #fpga.write('c2_7',coeffStr2[127::-1])
        #time.sleep(0.5)
        #fpga.write('c2_6',coeffStr2[(127+128):127:-1])
        #time.sleep(0.5)
        #fpga.write('c2_5',coeffStr2[(127+128*2):(127+128):-1])
        #time.sleep(0.5)
        #fpga.write('c2_4',coeffStr2[(127+128*3):(127+128*2):-1])
        #time.sleep(0.5)
        #fpga.write('c2_3',coeffStr2[(127+128*4):(127+128*3):-1])
        #time.sleep(0.5)
        #fpga.write('c2_2',coeffStr2[(127+128*5):(127+128*4):-1])
        #time.sleep(0.5)
        #fpga.write('c2_1',coeffStr2[(127+128*6):(127+128*5):-1])
        #time.sleep(0.5)
        #fpga.write('c2_0',coeffStr2[(127+128*7):(127+128*6):-1])
        #time.sleep(0.5)
	tmp = np.roll(coeffArray2[0:128],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_0',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128:128*2],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_1',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128*2:128*3],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_2',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128*3:128*4],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_3',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128*4:128*5],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_4',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128*5:128*6],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_5',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128*6:128*7],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_6',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray2[128*7:128*8],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c2_7',tmp_write)
        time.sleep(0.5)

	tmp = np.roll(coeffArray3[0:128],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_0',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128:128*2],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_1',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128*2:128*3],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_2',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128*3:128*4],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_3',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128*4:128*5],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_4',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128*5:128*6],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_5',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128*6:128*7],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_6',tmp_write)
        time.sleep(0.5)
        tmp = np.roll(coeffArray3[128*7:128*8],-1)
	tmp_write = struct.pack('>128L',*tmp)
        fpga.write('c3_7',tmp_write)
        time.sleep(0.5)
#        fpga.write('c3_0',coeffStr3[0:128])
#        time.sleep(0.5)
#        fpga.write('c3_1',coeffStr3[128:128*2])
#        time.sleep(0.5)
#        fpga.write('c3_2',coeffStr3[128*2:128*3])
#        time.sleep(0.5)
#        fpga.write('c3_3',coeffStr3[128*3:128*4])
#        time.sleep(0.5)
#        fpga.write('c3_4',coeffStr3[128*4:128*5])
#        time.sleep(0.5)
#        fpga.write('c3_5',coeffStr3[128*5:128*6])
#        time.sleep(0.5)
#        fpga.write('c3_6',coeffStr3[128*6:128*7])
#        time.sleep(0.5)
#        fpga.write('c3_7',coeffStr3[128*7:128*8])
#        time.sleep(0.5)
#

def populateSingle(combCoeff):
	numTones = 2048
	combCoeffSingle = np.zeros(numTones) + 1j*np.zeros(numTones)
	for toneIter in range(0,numTones-2):
		if toneIter < 1024:
			#combCoeffSingle[toneIter] = combCoeff[1023-toneIter,toneIter+1]
			#combCoeffSingle[1023-toneIter] = combCoeff[toneIter,1024-toneIter]
			combCoeffSingle[1023-toneIter] = combCoeff[1023-toneIter,toneIter+1]
			#print  "index:" + str(1023-toneIter) + "  read1: " + str(1023 - toneIter) + "  read2: " + str(toneIter+1)
		else:
			combCoeffSingle[toneIter] = combCoeff[toneIter-1023,toneIter+1]
			#print combCoeffSingle[toneIter]
	return combCoeffSingle

def readFiles():
	filename = 'combCoeff.h5'
	f_data = h5py.File(filename,'r')
	f_key = f_data.keys()[0]
	#print f_data.keys()
	#combCoeff = list(f_data[f_key])
	combCoeff = np.array(f_data[f_key])
	return combCoeff

combCoeff = readFiles()

#plt.imshow(combCoeff.real)
#plt.plot(combCoeff[1,:].real)
#plt.show()
#print combCoeff[1025,100]

combCoeffSingle = populateSingle(combCoeff)
#plt.plot(combCoeffSingle.real)
#plt.plot(combCoeffSingle.imag)
#plt.show()
defCoeffs14()
defCoeffs23(combCoeffSingle)
