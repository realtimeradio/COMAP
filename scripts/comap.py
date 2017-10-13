#!/usr/bin/env python

import numpy, corr, time, struct, sys, logging, socket
import matplotlib.pyplot as plt

roach = '192.168.42.65'

print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(0.5)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()
    
# setup initial parameters
fpga.write_int('fft_shift',65535)
fpga.write_int('acc_len',65535)
#fpga.write_int('acc_len',1023)

# coefficients for separate spectrometer
real = 0b0100000000000000
imag = 0b0000000000000000

coeff0 = (real << 16) + imag
odata =numpy.ones(1024,'l')*coeff0
cstr0 = struct.pack('>1024l',*odata)

# currently hard coded to 1, as all 
# coeffs can be manipulated by c2 and c3

#fpga.write('c1_0',cstr0)
#fpga.write('c1_1',cstr0)
#fpga.write('c1_2',cstr0)
#fpga.write('c1_3',cstr0)
#fpga.write('c1_4',cstr0)
#fpga.write('c1_5',cstr0)
#fpga.write('c1_6',cstr0)
#fpga.write('c1_7',cstr0)
#
#fpga.write('c4_0',cstr0)
#fpga.write('c4_1',cstr0)
#fpga.write('c4_2',cstr0)
#fpga.write('c4_3',cstr0)
#fpga.write('c4_4',cstr0)
#fpga.write('c4_5',cstr0)
#fpga.write('c4_6',cstr0)
#fpga.write('c4_7',cstr0)

# trigger reset
fpga.write_int('rst',3)
time.sleep(0.5)
fpga.write_int('rst',0)

