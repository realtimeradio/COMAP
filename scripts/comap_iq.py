#!/bin/env ipython

import corr, time, struct, sys, logging, socket
import numpy as np
import matplotlib.pyplot as plt
#import hittite

roach = '192.168.42.65'

fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(0.1)

# setup initial parameters

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
	

def defCoeffs23(coeff2,coeffs3):
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
	time.sleep(0.5)

	
	
	
	fpga.write('c2_0',coeff2)
	time.sleep(0.5)
	fpga.write('c2_1',coeff2)
	time.sleep(0.5)
	fpga.write('c2_2',coeff2)
	time.sleep(0.5)
	fpga.write('c2_3',coeff2)
	time.sleep(0.5)
	fpga.write('c2_4',coeff2)
	time.sleep(0.5)
	fpga.write('c2_5',coeff2)
	time.sleep(0.5)
	fpga.write('c2_6',coeff2)
	time.sleep(0.5)
	fpga.write('c2_7',coeff2)
	time.sleep(0.5)
	fpga.write('c3_0',coeff3)
	time.sleep(0.5)
	fpga.write('c3_1',coeff3)
	time.sleep(0.5)
	fpga.write('c3_2',coeff3)
	time.sleep(0.5)
	fpga.write('c3_3',coeff3)
	time.sleep(0.5)
	fpga.write('c3_4',coeff3)
	time.sleep(0.5)
	fpga.write('c3_5',coeff3)
	time.sleep(0.5)
	fpga.write('c3_6',coeff3)
	time.sleep(0.5)
	fpga.write('c3_7',coeff3)

def triggerTot():
	# trigger all the snap blocks
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
	
	time.sleep(0.1)
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

def triggerCross():
	fpga.write_int('snap_inp1x_ctrl',0)
	fpga.write_int('snap_inp2x_ctrl',0)
	fpga.write_int('snap_inp3x_ctrl',0)
	fpga.write_int('snap_inp4x_ctrl',0)
	fpga.write_int('snap_inp5x_ctrl',0)
	fpga.write_int('snap_inp6x_ctrl',0)
	fpga.write_int('snap_inp7x_ctrl',0)
	fpga.write_int('snap_inp8x_ctrl',0)
	fpga.write_int('snap_inp9x_ctrl',0)
	fpga.write_int('snap_inp10x_ctrl',0)
	fpga.write_int('snap_inp11x_ctrl',0)
	fpga.write_int('snap_inp12x_ctrl',0)
	fpga.write_int('snap_inp13x_ctrl',0)
	fpga.write_int('snap_inp14x_ctrl',0)
	fpga.write_int('snap_inp15x_ctrl',0)
	fpga.write_int('snap_inp16x_ctrl',0)
	
	time.sleep(0.1)

	fpga.write_int('snap_inp1x_ctrl',1)
	fpga.write_int('snap_inp2x_ctrl',1)
	fpga.write_int('snap_inp3x_ctrl',1)
	fpga.write_int('snap_inp4x_ctrl',1)
	fpga.write_int('snap_inp5x_ctrl',1)
	fpga.write_int('snap_inp6x_ctrl',1)
	fpga.write_int('snap_inp7x_ctrl',1)
	fpga.write_int('snap_inp8x_ctrl',1)
	fpga.write_int('snap_inp9x_ctrl',1)
	fpga.write_int('snap_inp10x_ctrl',1)
	fpga.write_int('snap_inp11x_ctrl',1)
	fpga.write_int('snap_inp12x_ctrl',1)
	fpga.write_int('snap_inp13x_ctrl',1)
	fpga.write_int('snap_inp14x_ctrl',1)
	fpga.write_int('snap_inp15x_ctrl',1)
	fpga.write_int('snap_inp16x_ctrl',1)

def snapTot():
	#
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

def snapCross():
	bramsnap1x = struct.unpack('>128q',fpga.read('snap_inp1x_bram',128*8))
	bramsnap2x = struct.unpack('>128q',fpga.read('snap_inp2x_bram',128*8))
	bramsnap3x = struct.unpack('>128q',fpga.read('snap_inp3x_bram',128*8))
	bramsnap4x = struct.unpack('>128q',fpga.read('snap_inp4x_bram',128*8))
	bramsnap5x = struct.unpack('>128q',fpga.read('snap_inp5x_bram',128*8))
	bramsnap6x = struct.unpack('>128q',fpga.read('snap_inp6x_bram',128*8))
	bramsnap7x = struct.unpack('>128q',fpga.read('snap_inp7x_bram',128*8))
	bramsnap8x = struct.unpack('>128q',fpga.read('snap_inp8x_bram',128*8))
	
	bramsnap9x = struct.unpack('>128q',fpga.read('snap_inp9x_bram',128*8))
	bramsnap10x = struct.unpack('>128q',fpga.read('snap_inp10x_bram',128*8))
	bramsnap11x = struct.unpack('>128q',fpga.read('snap_inp12x_bram',128*8))
	bramsnap12x = struct.unpack('>128q',fpga.read('snap_inp11x_bram',128*8))
	bramsnap13x = struct.unpack('>128q',fpga.read('snap_inp16x_bram',128*8))
	bramsnap14x = struct.unpack('>128q',fpga.read('snap_inp13x_bram',128*8))
	bramsnap15x = struct.unpack('>128q',fpga.read('snap_inp15x_bram',128*8))
	bramsnap16x = struct.unpack('>128q',fpga.read('snap_inp14x_bram',128*8))

def calcCoeffs():
	
	for i in range(0,128):

		total_powerI[j] = float(bramsnap1[i])/2**34
		total_powerQ[j] = float(bramsnap1a[i])/2**34
		total_powerI[j+1] = float(bramsnap1[i])/2**34
		total_powerQ[j+1] = float(bramsnap1a[i])/2**34
		j=j+8
	#	cross_power1 = complex(bramsnap1x[i]/2**34,bramsnap2x[i]/2**34);
	#	print 'i: '+str(i)+'  real: '+str((float(bramsnap1x[i])/2**34))+'  imag: '+str(float(bramsnap2x[i])/2**34)+'  totalI: '+str((float(bramsnap1[i])/2**34))+'  totalQ: '+str(float(bramsnap1a[i])/2**34)
	
	#cross_power2 = bramsnap3x + 1j*bramsnap4x;
	#cross_power3 = bramsnap5x + 1j*bramsnap6x;
	#cross_power4 = bramsnap7x + 1j*bramsnap8x;
	#cross_power5 = bramsnap9x + 1j*bramsnap10x;
	#cross_power6 = bramsnap11x + 1j*bramsnap12x;
	#cross_power7 = bramsnap13x + 1j*bramsnap14x;
	#cross_power8 = bramsnap15x + 1j*bramsnap16x;
	#
	#total_powerI = np.concatenate([bramsnap1,bramsnap2,bramsnap3,bramsnap4,bramsnap5,bramsnap6,bramsnap7,bramsnap8])
	#total_powerQ = np.concatenate([bramsnap1a,bramsnap2a,bramsnap3a,bramsnap4a,bramsnap5a,bramsnap6a,bramsnap7a,bramsnap8a])
	
	#cross_powerIQ = np.concatenate([cross_power1,cross_power2,cross_power3,cross_power4,cross_power5,cross_power6,cross_power7,cross_power8]); 
	
	# one channel offset due to bug in fpga code, fixed for v6
	cross_powerIQ = complex(float(bramsnap1x[102])/2**34,float(bramsnap2x[102])/2**34)
	
	print 'totalpowerI: '+str(total_powerI)+'  totalpowerQ: '+str(total_powerQ)+'  crosspowerIQ:'+str(cross_powerIQ)
	powerCoeff = np.sqrt(total_powerQ/total_powerI)
	#phaseCoeff = np.unwrap(1*np.angle(cross_powerIQ))
	phaseCoeff =np.angle(cross_powerIQ)
	combCoeff =powerCoeff*np.exp(1j*(phaseCoeff))
	
	print 'powerCoeff: '+str(powerCoeff)+'  phaseCoeff: '+str(phaseCoeff)+'  combCoeff:'+str(combCoeff)
	
	combCoeff2 = -1*(combCoeff)
	combCoeff3 = -1*(np.power(combCoeff,-1))
	coeffs2r = np.binary_repr(np.int16(combCoeff2.real*2**14),16)
	coeffs2i = np.binary_repr(np.int16(combCoeff2.imag*2**14),16)
	coeffs3r = np.binary_repr(np.int16(combCoeff3.real*2**14),16)
	coeffs3i = np.binary_repr(np.int16(combCoeff3.imag*2**14),16)
	coeffs2 = (coeffs2r + coeffs2i)
	coeffs3 = (coeffs3r + coeffs3i)
	coeffs2 = int(coeffs2,2)
	coeffs3 = int(coeffs3,2)
	coeffArray2 = np.ones(1024,'L')*coeffs2
	coeffArray3 = np.ones(1024,'L')*coeffs3
	#coeffArray2 = np.zeros(1024,'l')*coeffs2
	#coeffArray3 = np.zeros(1024,'l')*coeffs3
	coeffStr2 = struct.pack('>1024L',*coeffArray2)
	coeffStr3 = struct.pack('>1024L',*coeffArray3)

#
#import h5py
#filename = 'file.hdf5'
#f = h5py.File(filename, 'r')
#
## List all groups
#print("Keys: %s" % f.keys())
#a_group_key = f.keys()[0]
#
## Get the data
#data = list(f[a_group_key])


# c2: 0-7: reversed?
# c3: 0-7: normal? (or switch reverse).
#	
defCoeffs()	
