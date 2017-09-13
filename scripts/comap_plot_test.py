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

# trigger all the snap blocks

fpga.write_int('snap_inp1_ctrl',0)

fpga.write_int('snap_inp1_ctrl',1)

bramsnap1 = struct.unpack('>512Q',fpga.read('snap_inp1_bram',512*8))

plt.subplot(1,1,1)
plt.plot(bramsnap1)
plt.show()



