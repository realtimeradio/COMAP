hittiteIp='192.168.43.102'

import hittite
import argparse
from sys import argv

parser = argparse.ArgumentParser(epilog='alternate usage: python {0}'.format(argv[0]));
parser.add_argument('--on',action='store_true', help='set hittite tone on');
parser.add_argument('--off',action='store_true', help='set hittite tone off');
parser.add_argument('--freq',help='set freq to this number (e.g. 4e9 = 4GHz)',type=float,default=4e9);
parser.add_argument('--power',help='hittite tone power (dBm), recommended value < -5',type=int,default=-20);


args = parser.parse_args();

if ('--on' in argv):
    hittiteMode = 'on';
else:
   hittiteMode = 'off';

if (args.power > 0):
   print 'power level too high! Needs to be < -5dBm';
else:
   hittitePower = args.power;

if (args.freq > 20e9):
   print 'Frequency must be less than 20GHz'
else:
   hittiteFreq = args.freq;

hittite.setAll(hittiteFreq,hittitePower,hittiteMode,hittiteIp,50000,doPrint=True,ret=False)
