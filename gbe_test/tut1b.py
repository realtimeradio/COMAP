#!/bin/env ipython

import corr, time, struct, sys, logging, socket, datetime

def getCurrentDadaTimeUS():
  now = datetime.datetime.today()
  now_str = now.strftime("%Y%m%d%H%M%S%f")
  return now_str

def getUTCDadaTime(toadd=0):
  now = datetime.datetime.utcnow()
  if (toadd > 0):
    delta = datetime.timedelta(0, toadd)
    now = now + delta
  now_str = now.strftime("%Y-%m-%d-%H:%M:%S")
  return now_str

def wait_for_1sec_boundary():
        curr_time = int(time.time())
        next_time = curr_time
        while curr_time == next_time:
                next_time = int(time.time())

def wait_until_utc_sec(utcstr):
        cur_time = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")
        while cur_time != utcstr:
                cur_time = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")

rid = int(sys.argv[1])
startTime = str(sys.argv[2])
#print startTime

#Decide where we're going to send the data, and from which addresses:
dest_ip  =192*(2**24) + 168*(2**16) + 11*(2**8) + 40
fabric_port=60000         
source_ip= 192*(2**24) + 168*(2**16) + 11*(2**8) + (1+rid)
#mac_base=(2<<40) + (2<<32) 
mac_base  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8)  

pkt_period = 2**14 #2**14 #how often to send another packet in FPGA clocks (200MHz)
payload_len = 8192 #how big to make each packet in 64bit words

tx_core_name = 'one_GbE'


dest_mac_r0 = 36*(2**40) + 138*(2**32) + 7*(2**24) +  232*(2**16) +  124*(2**8) +49 #

rofl1_mac0  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 1  #50 # 02:02:c0:a8:28:32 
rofl1_mac1  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 2  #50 # 02:02:c0:a8:28:32 
rofl1_mac2  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 3  #50 # 02:02:c0:a8:28:32 
rofl1_mac3  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 4  #50 # 02:02:c0:a8:28:32 
rofl1_mac4  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 5  #50 # 02:02:c0:a8:28:32 
rofl1_mac5  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 6  #50 # 02:02:c0:a8:28:32 
rofl1_mac6  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 7  #50 # 02:02:c0:a8:28:32 
rofl1_mac7  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 8  #50 # 02:02:c0:a8:28:32 
rofl1_mac8  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 9  #50 # 02:02:c0:a8:28:32 
rofl1_mac9  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 10  #50 # 02:02:c0:a8:28:32 
rofl1_mac10  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 11  #50 # 02:02:c0:a8:28:32 
rofl1_mac11  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 12  #50 # 02:02:c0:a8:28:32 
rofl1_mac12  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 13  #50 # 02:02:c0:a8:28:32 
rofl1_mac13  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 14  #50 # 02:02:c0:a8:28:32 
rofl1_mac14  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 15  #50 # 02:02:c0:a8:28:32 
rofl1_mac15  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 16  #50 # 02:02:c0:a8:28:32 
rofl1_mac16  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 17  #50 # 02:02:c0:a8:28:32 
rofl1_mac17  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 18  #50 # 02:02:c0:a8:28:32 
rofl1_mac18  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 19  #50 # 02:02:c0:a8:28:32 
rofl1_mac19  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 20  #50 # 02:02:c0:a8:28:32 
rofl1_mac20  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 21  #50 # 02:02:c0:a8:28:32 
rofl1_mac21  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 22  #50 # 02:02:c0:a8:28:32 
rofl1_mac22  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 23  #50 # 02:02:c0:a8:28:32 
rofl1_mac23  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 24  #50 # 02:02:c0:a8:28:32 
rofl1_mac24  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 25  #50 # 02:02:c0:a8:28:32 
rofl1_mac25  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 26  #50 # 02:02:c0:a8:28:32 
rofl1_mac26  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 27  #50 # 02:02:c0:a8:28:32 
rofl1_mac27  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 28  #50 # 02:02:c0:a8:28:32 
rofl1_mac28  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 29  #50 # 02:02:c0:a8:28:32 
rofl1_mac29  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 30  #50 # 02:02:c0:a8:28:32 
rofl1_mac30  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 31  #50 # 02:02:c0:a8:28:32 
rofl1_mac31  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 32  #50 # 02:02:c0:a8:28:32 
rofl1_mac32  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 33  #50 # 02:02:c0:a8:28:32 
rofl1_mac33  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 34  #50 # 02:02:c0:a8:28:32 
rofl1_mac34  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 35  #50 # 02:02:c0:a8:28:32 
rofl1_mac35  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 36  #50 # 02:02:c0:a8:28:32 
rofl1_mac36  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 37  #50 # 02:02:c0:a8:28:32 
rofl1_mac37  = 2*(2**40) + 2*(2**32) + 192*(2**24) + 168*(2**16) + 40*(2**8) + 38  #50 # 02:02:c0:a8:28:32 

dest_macff = 255*(2**40) + 255*(2**32) + 255*(2**24) + 255*(2**16) + 255*(2**8) + 255

arp_table =[dest_macff for i in range(256)]

arp_table[2] = rofl1_mac0
arp_table[3] = rofl1_mac1
arp_table[4] = rofl1_mac2
arp_table[5] = rofl1_mac3
arp_table[6] = rofl1_mac4
arp_table[7] = rofl1_mac5
arp_table[8] = rofl1_mac6
arp_table[9] = rofl1_mac7
arp_table[10] = rofl1_mac8
arp_table[11] = rofl1_mac9
arp_table[12] = rofl1_mac1
arp_table[13] = rofl1_mac11
arp_table[14] = rofl1_mac12
arp_table[15] = rofl1_mac13
arp_table[16] = rofl1_mac14
arp_table[17] = rofl1_mac15
arp_table[18] = rofl1_mac16
arp_table[19] = rofl1_mac17
arp_table[20] = rofl1_mac18
arp_table[21] = rofl1_mac19
arp_table[22] = rofl1_mac20
arp_table[23] = rofl1_mac21
arp_table[24] = rofl1_mac22
arp_table[25] = rofl1_mac23
arp_table[26] = rofl1_mac24
arp_table[27] = rofl1_mac25
arp_table[28] = rofl1_mac26
arp_table[29] = rofl1_mac27
arp_table[30] = rofl1_mac28
arp_table[31] = rofl1_mac29
arp_table[32] = rofl1_mac30
arp_table[33] = rofl1_mac31
arp_table[34] = rofl1_mac32
arp_table[35] = rofl1_mac33
arp_table[36] = rofl1_mac34
arp_table[37] = rofl1_mac35
arp_table[38] = rofl1_mac36
arp_table[39] = rofl1_mac37

arp_table[40] = dest_mac_r0


#boffile = 'gbe_test_2017_Apr_18_1654.bof'
boffile = 'gbe_test_2017_May_23_1607.bof'

roach = '192.168.1.'+str(100+rid)


print('Connecting to server %s... '%(roach)),
fpga = corr.katcp_wrapper.FpgaClient(roach)
time.sleep(1)

if fpga.is_connected():
    print 'ok\n'
else:
    print 'ERROR connecting to server %s.\n'%(roach)
    exit()

fpga.progdev(boffile)
time.sleep(1)
    
fpga.write_int('pkt_sim_enable', 0)
#print 'done'

fpga.write_int('pkt_sim_rid',rid-2)
#print '---------------------------'
#print 'Configuring transmitter core...',
sys.stdout.flush()
#fpga.tap_start('tap3',tx_core_name,mac_base+source_ip,source_ip,fabric_port)
fpga.config_10gbe_core(tx_core_name,mac_base+rid,source_ip,fabric_port,arp_table)
#print 'done'

#print '---------------------------'
#print 'Setting-up packet source...',
sys.stdout.flush()
fpga.write_int('pkt_sim_period',pkt_period)
fpga.write_int('pkt_sim_payload_len',payload_len)
#print 'done'

#print 'Setting-up destination addresses...',
sys.stdout.flush()
fpga.write_int('dest_ip',dest_ip)
fpga.write_int('dest_port',fabric_port)
#print 'done'

#print 'Resetting cores and counters...',
sys.stdout.flush()
fpga.write_int('rst', 3)
fpga.write_int('rst', 0)
#print 'done'

time.sleep(2)

#fpga.print_10gbe_core_details(tx_core_name,arp=True)

print 'Enabling output...%s\n' %(roach)
sys.stdout.flush()
fpga.write_int('pkt_sim_enable', 1)
#print 'done'
#print 'Waiting for start time %s\n' %(startTime) 
fpga.write_int('reg_arm',0)
wait_until_utc_sec(startTime)
time.sleep(0.2)
fpga.write_int('reg_arm',1)
