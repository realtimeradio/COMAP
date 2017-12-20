#!/bin/env ipython

import scipy, numpy, corr, time, struct, sys, logging, socket
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

fpga.write_int('scope_raw_0_snap_ctrl',3)
fpga.write_int('scope_raw_0_snap_ctrl',0)
fpga.write_int('scope_raw_1_snap_ctrl',3)
fpga.write_int('scope_raw_1_snap_ctrl',0)
time.sleep(0.1)
fpga.write_int('scope_raw_0_snap_ctrl',3)
fpga.write_int('scope_raw_0_snap_ctrl',0)
fpga.write_int('scope_raw_1_snap_ctrl',3)
fpga.write_int('scope_raw_1_snap_ctrl',0)


adcsnap = struct.unpack('<1024b',fpga.read('scope_raw_0_snap_bram',256*4))
adcsnap1 = struct.unpack('<1024b',fpga.read('scope_raw_1_snap_bram',256*4))
i=0;

#while (i<65):
#	tmp = adcsnap[0+(16*(i)):8+(16*(i))]
#	if (i==0):
#		bram_0 = tmp
#	else:
#		bram_0 = numpy.concatenate((bram_0,tmp))
#	i=i+1

nfft = scipy.fft(adcsnap)
nabs = numpy.abs(nfft[1:512:1])

nfft2 = scipy.fft(adcsnap1)
nabs2 = numpy.abs(nfft2[1:512:1])
plt.figure()

plt.subplot(2,2,1)
plt.title('ADC-0')
plt.hist(adcsnap)
#plt.plot(nabs)
plt.subplot(2,2,3)
#plt.plot(bram_0)
plt.semilogy(nabs)
plt.subplot(2,2,2)
plt.title('ADC-1')
plt.hist(adcsnap1)
plt.subplot(2,2,4)
plt.semilogy(nabs2)
plt.show()

















