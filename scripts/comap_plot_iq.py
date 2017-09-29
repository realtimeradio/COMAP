#!/usr/bin/env python

import numpy as np
import corr, time, struct, sys, logging, socket
import matplotlib.pyplot as plt

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

fpga.write_int('rst',3)
time.sleep(0.1)
fpga.write_int('rst',0)
# each bram holds 128 32-bit (16re+16im) numbers.
time.sleep(0.2)
bramsnap1 = struct.unpack('>32h',fpga.read('snap_inp1_bram',64))
bramsnap2 = struct.unpack('>32h',fpga.read('snap_inp2_bram',64))
bramsnap3 = struct.unpack('>32h',fpga.read('snap_inp3_bram',64))
bramsnap4 = struct.unpack('>32h',fpga.read('snap_inp4_bram',64))
bramsnap5 = struct.unpack('>32h',fpga.read('snap_inp5_bram',64))
bramsnap6 = struct.unpack('>32h',fpga.read('snap_inp6_bram',64))
bramsnap7 = struct.unpack('>32h',fpga.read('snap_inp7_bram',64))
bramsnap8 = struct.unpack('>32h',fpga.read('snap_inp8_bram',64))

bramsnap1a = struct.unpack('>32h',fpga.read('snap_inp9_bram',64))
bramsnap2a = struct.unpack('>32h',fpga.read('snap_inp10_bram',64))
bramsnap3a = struct.unpack('>32h',fpga.read('snap_inp11_bram',64))
bramsnap4a = struct.unpack('>32h',fpga.read('snap_inp12_bram',64))
bramsnap5a = struct.unpack('>32h',fpga.read('snap_inp16_bram',64))
bramsnap6a = struct.unpack('>32h',fpga.read('snap_inp14_bram',64))
bramsnap7a = struct.unpack('>32h',fpga.read('snap_inp13_bram',64))
bramsnap8a = struct.unpack('>32h',fpga.read('snap_inp15_bram',64))

bramsnap1 = np.array(bramsnap1).reshape((16,2))
bramsnap2 = np.array(bramsnap2).reshape((16,2))
bramsnap3 = np.array(bramsnap3).reshape((16,2))
bramsnap4 = np.array(bramsnap4).reshape((16,2))
bramsnap5 = np.array(bramsnap5).reshape((16,2))
bramsnap6 = np.array(bramsnap6).reshape((16,2))
bramsnap7 = np.array(bramsnap7).reshape((16,2))
bramsnap8 = np.array(bramsnap8).reshape((16,2))
bramsnap1a = np.array(bramsnap1a).reshape((16,2))
bramsnap2a = np.array(bramsnap2a).reshape((16,2))
bramsnap3a = np.array(bramsnap3a).reshape((16,2))
bramsnap4a = np.array(bramsnap4a).reshape((16,2))
bramsnap5a = np.array(bramsnap5a).reshape((16,2))
bramsnap6a = np.array(bramsnap6a).reshape((16,2))
bramsnap7a = np.array(bramsnap7a).reshape((16,2))
bramsnap8a = np.array(bramsnap8a).reshape((16,2))

bram1a_cplx = bramsnap1a[:,0] + 1j*bramsnap1a[:,1]
bram2a_cplx = bramsnap2a[:,0] + 1j*bramsnap2a[:,1]
bram3a_cplx = bramsnap3a[:,0] + 1j*bramsnap3a[:,1]
bram4a_cplx = bramsnap4a[:,0] + 1j*bramsnap4a[:,1]
bram5a_cplx = bramsnap5a[:,0] + 1j*bramsnap5a[:,1]
bram6a_cplx = bramsnap6a[:,0] + 1j*bramsnap6a[:,1]
bram7a_cplx = bramsnap7a[:,0] + 1j*bramsnap7a[:,1]
bram8a_cplx = bramsnap8a[:,0] + 1j*bramsnap8a[:,1]

bramsnapXa = np.zeros(128,'h') + 1j*np.zeros(128,'h')
j = 0


# channels unscrambled
for i in range (16):	
#	bramsnapX[j] = bramsnap1[i]
#	bramsnapX[j+1] = bramsnap2[i]
#	bramsnapX[j+2] = bramsnap3[i]
#	bramsnapX[j+3] = bramsnap4[i]
#	bramsnapX[j+4] = bramsnap5[i]
#	bramsnapX[j+5] = bramsnap6[i]
#	bramsnapX[j+6] = bramsnap7[i]
#	bramsnapX[j+7] = bramsnap8[i]
#
	bramsnapXa[j] = bram1a_cplx[i]
	bramsnapXa[j+1] = bram2a_cplx[i]
	bramsnapXa[j+2] = bram3a_cplx[i]
	bramsnapXa[j+3] = bram4a_cplx[i]
	bramsnapXa[j+4] = bram5a_cplx[i]
	bramsnapXa[j+5] = bram6a_cplx[i]
	bramsnapXa[j+6] = bram7a_cplx[i]
	bramsnapXa[j+7] = bram8a_cplx[i]
        j=j+8
#		
#
#channels not unscrambled

bramsnapX = np.concatenate([bramsnap1,bramsnap2,bramsnap3,bramsnap4,bramsnap5,bramsnap6,bramsnap7,bramsnap8])
bramX_cplx = bramsnapX[:,0] + 1j*bramsnapX[:,1]
#bramsnapXa = numpy.concatenate([bramsnap1a,bramsnap2a,bramsnap3a,bramsnap4a,bramsnap5a,bramsnap6a,bramsnap7a,bramsnap8a])

c1 = 1 + 0j
c2 = 0 + 1j
c3 = 0 + 1j
c4 = 1 + 0j

tmpI = bramX_cplx*c1 + bramsnapXa*c2;
tmpQ = bramX_cplx*c3 + bramsnapXa*c4;
c2 = 0 + 1j
c3 = 0 + 1j
tmpI2 = bramX_cplx*c1 + bramsnapXa*c2;
tmpQ2 = bramX_cplx*c3 + bramsnapXa*c4;

plt.subplot(4,1,1)
plt.semilogy(np.abs(bramX_cplx))
#plt.plot(np.abs(bramX_cplx))
plt.subplot(4,1,2)
plt.semilogy(np.abs(bramsnapXa))
#plt.plot(np.abs(bramsnapXa))
plt.subplot(4,1,3)
plt.semilogy(np.abs(tmpI))
#plt.plot(np.abs(tmpI))
plt.semilogy(np.abs(tmpI2))
plt.subplot(4,1,4)
plt.semilogy(np.abs(tmpQ))
plt.semilogy(np.abs(tmpQ2))
#plt.plot(np.abs(tmpQ))
plt.show()



