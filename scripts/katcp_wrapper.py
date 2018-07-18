# modified config_10gbe_core function from katcp_wrapper.py from the corr library to include a subnet hack

    def config_10gbe_core(self,device_name,mac,ip,port,arp_table,gateway=1):
        """Hard-codes a 10GbE core with the provided params. It does a blindwrite, so there is no verifcation that configuration was successful (this is necessary since some of these registers are set by the fabric depending on traffic received).

           @param self  This object.
           @param device_name  String: name of the device.
           @param mac   integer: MAC address, 48 bits.
           @param ip    integer: IP address, 32 bits.
           @param port  integer: port of fabric interface (16 bits).
           @param arp_table  list of integers: MAC addresses (48 bits ea).
           """
        #assemble struct for header stuff...
        #0x00 - 0x07: My MAC address
        #0x08 - 0x0b: Not used
        #0x0c - 0x0f: Gateway addr
        #0x10 - 0x13: my IP addr
        #0x14 - 0x17: Not assigned
        #0x18 - 0x1b: Buffer sizes
        #0x1c - 0x1f: Not assigned
        #0x20       : soft reset (bit 0)
        #0x21       : fabric enable (bit 0)
        #0x22 - 0x23: fabric port 
        
        #0x24 - 0x27: XAUI status (bit 2,3,4,5=lane sync, bit6=chan_bond)
        #0x28 - 0x2b: PHY config
 
        #0x28       : RX_eq_mix
        #0x29       : RX_eq_pol
        #0x2a       : TX_preemph
        #0x2b       : TX_diff_ctrl

        #0x1000     : CPU TX buffer
        #0x2000     : CPU RX buffer
        #0x3000     : ARP tables start
    
        # subnet hack
        subnet_mask = 0xfffffc00
        subnet_mask_pack = struct.pack('>L',subnet_mask)
       
        
        ctrl_pack=struct.pack('>QLLLLLLBBH',mac, 0, gateway, ip, 0, 0, 0, 0, 1, port)
        arp_pack=struct.pack('>256Q',*arp_table)
        self.blindwrite(device_name,ctrl_pack,offset=0)
        
        # write subnet mask
        self.blindwrite(device_name,subnet_mask_pack,offset=0x38)
        
        self.write(device_name,arp_pack,offset=0x3000)

