#!/usr/bin/env python

import scipy, corr, time, struct, sys, logging, socket
import numpy as np
import matplotlib.pyplot as plt

roach = '192.168.42.65'

print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(0.1)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()
    
# setup initial parameters
absI = np.zeros(512,'Q') + 1j*np.zeros(512,'Q')
absQ = np.zeros(512,'Q') + 1j*np.zeros(512,'Q')
absIacc = np.zeros(512,'Q')
absQacc = np.zeros(512,'Q')
print 'setup\n'
# trigger all the snap blocks
for zz in range(0,1):
	#print zz
	fpga.write_int('scope_raw_0_snapshot_ctrl',1)
	#fpga.write_int('scope_raw_0_snapshot_ctrl',0)
	fpga.write_int('scope_raw_1_snapshot_ctrl',1)
	#fpga.write_int('scope_raw_1_snapshot_ctrl',0)
	time.sleep(0.1)
	fpga.write_int('rst',3)
	time.sleep(0.1)
	fpga.write_int('rst',0)
	#fpga.write_int('scope_raw_0_snapshot_ctrl',3)
	fpga.write_int('scope_raw_0_snapshot_ctrl',0)
	#fpga.write_int('scope_raw_1_snapshot_ctrl',3)
	fpga.write_int('scope_raw_1_snapshot_ctrl',0)
	
	
	adcsnap = struct.unpack('<1024b',fpga.read('scope_raw_0_snapshot_bram',256*4))
	adcsnap1 = struct.unpack('<1024b',fpga.read('scope_raw_1_snapshot_bram',256*4))
	#print 'snapped\n'
	#i=0;
	
	#while (i<65):
	#	tmp = adcsnap[0+(16*(i)):8+(16*(i))]
	#	if (i==0):
	#		bram_0 = tmp
	#	else:
	#		bram_0 = numpy.concatenate((bram_0,tmp))
	#	i=i+1
	
	
	snapfft = scipy.fft(adcsnap)
	snapfft1 = scipy.fft(adcsnap1)
	#print 'fftd\n'
	#absfft = numpy.abs(snapfft[1:512:1])
	#absfft1 = numpy.abs(snapfft1[1:512:1])

	c1 = 0 + 0j
	c2 = 0 + 1j
	c3 = 0 + 1j
	c4 = 0 + 0j
	
	#c3 = np.power(c3,-1)
	
	
	for i in range (0,512):
		absI[i] = snapfft[i]*c1 + snapfft1[i]*c2; 
		absQ[i] = snapfft[i]*c3 + snapfft1[i]*c4;
	#print 'iqd\n'
	tmpI = np.abs(absI)
	tmpQ = np.abs(absQ)
	absIacc = absIacc + tmpI
	absQacc = absQacc + tmpQ
	#print 'accd\n'
plt.figure()

plt.subplot(2,2,1)
plt.title('ADC-0')
plt.hist(adcsnap)
plt.subplot(2,2,3)
#plt.plot(bram_0)
#plt.semilogy(absfft)
plt.semilogy(absIacc)
plt.subplot(2,2,2)
plt.title('ADC-1')
plt.hist(adcsnap1)
plt.subplot(2,2,4)
plt.semilogy(absQacc)
#plt.semilogy(absfft1)
plt.show()

















