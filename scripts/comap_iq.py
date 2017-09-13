#!/bin/env ipython

import numpy, corr, time, struct, sys, logging, socket
import matplotlib.pyplot as plt

roach = '192.168.42.102'

fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(0.5)

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

bramsnap1x = struct.unpack('>128Q',fpga.read('snap_inp1x_bram',128*8))
bramsnap2x = struct.unpack('>128Q',fpga.read('snap_inp2x_bram',128*8))
bramsnap3x = struct.unpack('>128Q',fpga.read('snap_inp3x_bram',128*8))
bramsnap4x = struct.unpack('>128Q',fpga.read('snap_inp4x_bram',128*8))
bramsnap5x = struct.unpack('>128Q',fpga.read('snap_inp5x_bram',128*8))
bramsnap6x = struct.unpack('>128Q',fpga.read('snap_inp6x_bram',128*8))
bramsnap7x = struct.unpack('>128Q',fpga.read('snap_inp7x_bram',128*8))
bramsnap8x = struct.unpack('>128Q',fpga.read('snap_inp8x_bram',128*8))

bramsnap1ax = struct.unpack('>128Q',fpga.read('snap_inp9x_bram',128*8))
bramsnap2ax = struct.unpack('>128Q',fpga.read('snap_inp10x_bram',128*8))
bramsnap3ax = struct.unpack('>128Q',fpga.read('snap_inp12x_bram',128*8))
bramsnap4ax = struct.unpack('>128Q',fpga.read('snap_inp11x_bram',128*8))
bramsnap5ax = struct.unpack('>128Q',fpga.read('snap_inp16x_bram',128*8))
bramsnap6ax = struct.unpack('>128Q',fpga.read('snap_inp13x_bram',128*8))
bramsnap7ax = struct.unpack('>128Q',fpga.read('snap_inp15x_bram',128*8))
bramsnap8ax = struct.unpack('>128Q',fpga.read('snap_inp14x_bram',128*8))

cross_power1 = bramsnap1x + 1j*bramsnap1ax;
cross_power2 = bramsnap2x + 1j*bramsnap2ax;
cross_power3 = bramsnap3x + 1j*bramsnap3ax;
cross_power4 = bramsnap4x + 1j*bramsnap4ax;
cross_power5 = bramsnap5x + 1j*bramsnap5ax;
cross_power6 = bramsnap6x + 1j*bramsnap6ax;
cross_power7 = bramsnap7x + 1j*bramsnap7ax;
cross_power8 = bramsnap8x + 1j*bramsnap8ax;

total_powerI = numpy.concatenate([bramsnap1,bramsnap2,bramsnap3,bramsnap4,bramsnap5,bramsnap6,bramsnap7,bramsnap8])
total_powerQ = numpy.concatenate([bramsnap1a,bramsnap2a,bramsnap3a,bramsnap4a,bramsnap5a,bramsnap6a,bramsnap7a,bramsnap8a])

cross_powerIQ = numpy.concatenate([cross_power1,cross_power2,cross_power3,cross_power4,cross_power5,cross_power6,cross_power7,cross_power8]); 

powerCoeff = sqrt(total_powerQ/total_powerI)
phaseCoeff = np.unwarp(1*np.angle(cross_powerIQ))

combCoeff =powerCoeff*np.exp(1j*phaseCoeff)

