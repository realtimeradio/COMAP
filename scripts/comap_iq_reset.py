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
	

defCoeffs()
