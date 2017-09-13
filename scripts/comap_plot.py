#!/bin/env ipython

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

#bramsnapX = numpy.zeros((1024,1))
#bramsnapXa = numpy.zeros((1024,1))
#j = 0


# channels unscrambled
#for i in range (128):	
#	bramsnapX[j] = bramsnap1[i]
#	bramsnapX[j+1] = bramsnap2[i]
#	bramsnapX[j+2] = bramsnap3[i]
#	bramsnapX[j+3] = bramsnap4[i]
#	bramsnapX[j+4] = bramsnap5[i]
#	bramsnapX[j+5] = bramsnap6[i]
#	bramsnapX[j+6] = bramsnap7[i]
#	bramsnapX[j+7] = bramsnap8[i]
#
#	bramsnapXa[j] = bramsnap1a[i]
#	bramsnapXa[j+1] = bramsnap2a[i]
#	bramsnapXa[j+2] = bramsnap3a[i]
#	bramsnapXa[j+3] = bramsnap4a[i]
#	bramsnapXa[j+4] = bramsnap5a[i]
#	bramsnapXa[j+5] = bramsnap6a[i]
#	bramsnapXa[j+6] = bramsnap7a[i]
#	bramsnapXa[j+7] = bramsnap8a[i]
#        j=j+8
#		
#
#channels not unscrambled

bramsnapX = numpy.concatenate([bramsnap1,bramsnap2,bramsnap3,bramsnap4,bramsnap5,bramsnap6,bramsnap7,bramsnap8])
bramsnapXa = numpy.concatenate([bramsnap1a,bramsnap2a,bramsnap3a,bramsnap4a,bramsnap5a,bramsnap6a,bramsnap7a,bramsnap8a])

plt.subplot(2,1,1)
plt.plot(bramsnapX)
#plt.semilogy(bramsnapX)
plt.subplot(2,1,2)
plt.plot(bramsnapXa)
#plt.semilogy(bramsnapXa)
plt.show()



