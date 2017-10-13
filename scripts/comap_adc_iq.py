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
absI = np.zeros(512) + 1j*np.zeros(512)
absQ = np.zeros(512) + 1j*np.zeros(512)
cross_powerIQ = np.zeros(512) + 1j*np.zeros(512)
absIacc = np.zeros(512)
absQacc = np.zeros(512)
absIacc2 = np.zeros(512)
absQacc2 = np.zeros(512)
print 'setup\n'
# trigger all the snap blocks
for zz in range(0,16):
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

	c1 = 1 + 1j
	c2 = 0 + 0j
	c3 = 0 + 0j
	c4 = 1 + 1j
	
	#c3 = np.power(c3,-1)
	
	
	for i in range (0,512):
		absI[i] = snapfft[i]*c1 + snapfft1[i]*c2; 
		absQ[i] = snapfft[i]*c3 + snapfft1[i]*c4;
	#print 'iqd\n'


	tmpI = np.abs(absI)
	tmpQ = np.abs(absQ)

	cross_powerIQ = cross_powerIQ + (absI*np.conj(absQ))
	absIacc = absIacc + tmpI
	absQacc = absQacc + tmpQ

	c1 = 1 + 0j
	#c2 = -1*(-0.95 + 0.31j)
	#c3 = -1*(np.power(-0.95 + 0.31j,-1))
	c2 = -1*(0 + 1j)
	c3 = -1*(np.power(0 + 1j,-1))
	c4 = 1 + 0j
	#print c3
	for i in range (0,512):
		absI[i] = snapfft[i]*c1 + snapfft1[i]*c2; 
		absQ[i] = snapfft[i]*c3 + snapfft1[i]*c4;
	tmpI = np.abs(absI)
	tmpQ = np.abs(absQ)
	absIacc2 = absIacc2 + tmpI
	absQacc2 = absQacc2 + tmpQ
	#print 'accd\n'

#powerCoeff = np.sqrt(absQacc/absIacc)
powerCoeff = np.sqrt(absQacc/absIacc)
phaseCoeff = np.unwrap(1*np.angle(cross_powerIQ))
combCoeff = powerCoeff*np.exp(1j*(phaseCoeff))
print combCoeff[50]
print combCoeff[51]
print combCoeff[52]
print combCoeff[400]

plt.figure()

plt.subplot(2,2,1)
plt.title('ADC-0')
#plt.hist(adcsnap)
plt.semilogy(absIacc)
plt.subplot(2,2,3)
#plt.plot(bram_0)
#plt.semilogy(absfft)
#plt.semilogy(absIacc)
plt.semilogy(absIacc2)
plt.subplot(2,2,2)
plt.title('ADC-1')
#plt.hist(adcsnap1)
plt.semilogy(absQacc)
plt.subplot(2,2,4)
#plt.semilogy(absQacc)
plt.semilogy(absQacc2)
#plt.semilogy(absfft1)
plt.show()

















