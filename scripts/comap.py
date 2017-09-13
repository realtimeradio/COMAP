#!/bin/env ipython

import numpy, corr, time, struct, sys, logging, socket
import matplotlib.pyplot as plt

roach = '192.168.42.102'

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
fpga.write_int('acc_len',16483)

# coefficients for separate spectrometer

real = 0b0100000000000000
imag = 0b0000000000000000

coeff0 = (real << 16) + imag
odata =numpy.ones(1024,'l')*coeff0
cstr0 = struct.pack('>1024l',*odata)

fpga.write('c1_0',cstr0)
fpga.write('c1_1',cstr0)
fpga.write('c1_2',cstr0)
fpga.write('c1_3',cstr0)
fpga.write('c1_4',cstr0)
fpga.write('c1_5',cstr0)
fpga.write('c1_6',cstr0)
fpga.write('c1_7',cstr0)


fpga.write('c4_0',cstr0)
fpga.write('c4_1',cstr0)
fpga.write('c4_2',cstr0)
fpga.write('c4_3',cstr0)
fpga.write('c4_4',cstr0)
fpga.write('c4_5',cstr0)
fpga.write('c4_6',cstr0)
fpga.write('c4_7',cstr0)
# trigger reset

fpga.write_int('rst',3)
time.sleep(0.5)
fpga.write_int('rst',0)

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

bramsnap1 = struct.unpack('>16Q',fpga.read('snap_inp1_bram',16*8))
bramsnap2 = struct.unpack('>16Q',fpga.read('snap_inp2_bram',16*8))
bramsnap3 = struct.unpack('>16Q',fpga.read('snap_inp3_bram',16*8))
bramsnap4 = struct.unpack('>16Q',fpga.read('snap_inp4_bram',16*8))
bramsnap5 = struct.unpack('>16Q',fpga.read('snap_inp5_bram',16*8))
bramsnap6 = struct.unpack('>16Q',fpga.read('snap_inp6_bram',16*8))
bramsnap7 = struct.unpack('>16Q',fpga.read('snap_inp7_bram',16*8))
bramsnap8 = struct.unpack('>16Q',fpga.read('snap_inp8_bram',16*8))


bramsnapX = numpy.zeros((128,1))
j = 0
for i in range (16):	
	bramsnapX[j] = bramsnap1[i]
	bramsnapX[j+1] = bramsnap2[i]
	bramsnapX[j+2] = bramsnap3[i]
	bramsnapX[j+3] = bramsnap4[i]
	bramsnapX[j+4] = bramsnap5[i]
	bramsnapX[j+5] = bramsnap6[i]
	bramsnapX[j+6] = bramsnap7[i]
	bramsnapX[j+7] = bramsnap8[i]
        j=j+8
		

plt.figure()
plt.semilogy(bramsnapX)
plt.show()

















