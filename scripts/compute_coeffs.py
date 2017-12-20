from decimal import Decimal
import numpy as np

value_real = 0.54365363101
value_real = -0.0005
value_real = 1.0

#value_imag = '-0.751834821351'

# pre-multiplying so don't have to deal with binary point
# this should help the two's complement conversion.
#def float2bin(x, n=16):
#    base = int(x)
#    fraction = abs(int(round( (x - base) * (2**(n-2)) )))
#    print "{0:02b}{1:014b}".format(base,fraction)
#    total = int("{0:02b}{1:014b}".format(base,fraction),2)
#    print total
#    print total.bit_length()
#    #twos = twos_complement(total)
#    #twos = total if x >=0 else (1<<n) + total
#    twos = total - int((total << 1)& 2**n)
#    print twos.bit_length()
#    print twos 
#    retString = "{0:016b}".format(twos)
#    return retString
#    #return "{0:02b}{1:014b}".format(base, fraction)#.rstrip("0")
#

def float2bin(x):
    base = abs(x*2**14) # we are putting a binary point at 14 in the FPGA
    #base16 = np.int16(base)
    base16 = np.int16(base)
    return base16


def twos_comp(val, bits=16):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val      

valueB = float2bin(value_real)
print valueB
print "{0:016b}".format(valueB)
if value_real < 0:
	valueB = -1*valueB
print valueB
value2s = twos_comp(valueB)
#value2s = valueB if value_real >= 0 else (1<<16) + valueB 
print "{0:016b}".format(value2s)
#valueB = int(valueB,2)
#print format(valueB if value_real >= 0 else (1<<16) + valueB,'016b')
