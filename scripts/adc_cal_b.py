import adc5g
from adc5g import *

    def resetAdcOffsets(self,rID=None):
        if(rID==None):
            for zdok in range(2):
                for adc in range(1,5):
                    set_spi_offset(self.roach, zdok, adc, 128)
        else:
            set_spi_offset(self.roach, 0, 1, 138)
            set_spi_offset(self.roach, 0, 2, 140)
            set_spi_offset(self.roach, 0, 3, 135)
            set_spi_offset(self.roach, 0, 4, 115)
            set_spi_offset(self.roach, 1, 1, 132)
            set_spi_offset(self.roach, 1, 2, 124)
            set_spi_offset(self.roach, 1, 3, 126)
            set_spi_offset(self.roach, 1, 4, 135)
        
        
            
    def calibrateOffsets(self,sock):
        print 'match offset...'
        offsetADCs=np.zeros((256,4,2))
        offsetBest=np.zeros((4,2))
        for off in range(256): #step through all offsets...
            if(mod(off,32)==0): #just so we don't spit out tons of data
                print 'matchOffset: '+str(off)
            for zdok in range(2):  #2 adcs oer foga
                for chan in range(4): #4 cores per adc chip
                    set_spi_offset(self.roach, zdok, chan+1, off) #set the offset
            self.debugTriggerPacketizer() #this line and the next flushes the histograms
            self.flushSock()
            self.debugTriggerPacketizer() #I don't remember this and the last three lines.. basically fire off histogram packets
            packets_raw=self.doPacketCapture(fName=None, returnPacket=True)
            packets_parsed=parsePacketFrame(packets_raw,self.nPackets,frameCount=1)
            histos=packets_parsed['histos_py']
            
#            print 'histos: shape=' +str(histos.shape) + ' off=' +str(off) + ' chan=' + str(chan)+' zdok='+str(zdok)
            sum_means=np.zeros((4,2))
            sum_counts=np.squeeze(np.sum(histos,3))

            for zdok in range(2):
                for chan in range(4):
                    for i in range(256):
                        sum_means[chan,zdok]+=histos[0,zdok,chan,i]*(i-128) #128 is the zero value
                    offsetADCs[off,chan,zdok]=sum_means[chan,zdok]/sum_counts[zdok,chan]
                    #print 'offset ('+str(zdok)+','+str(chan)+')= '+str(offsetADCs[off,chan,zdok])
        for zdok in range(2):
            for chan in range(4):
                offsetBest[chan,zdok]=np.abs(offsetADCs[:,chan,zdok]).argmin() #find which one has the smallest abs(mean(data))
                print 'offBest: ' +str(offsetBest[chan,zdok]) + ' chan=' + str(chan)+' zdok='+str(zdok) + ' val=' + str(offsetADCs[offsetBest[chan,zdok],chan,zdok]) #print it.
                set_spi_offset(self.roach, zdok, chan+1, offsetBest[chan,zdok]) #assign it.
        return (offsetADCs, offsetBest)

    def calibrateGains(self,sock):
        print 'match gain...'
        self.debugTriggerPacketizer() #this line and the next flushes the histograms
        self.flushSock()
        self.debugTriggerPacketizer()
        packets_raw=self.doPacketCapture(fName=None, returnPacket=True)
        packets_parsed=parsePacketFrame(packets_raw,self.nPackets,frameCount=1)
        histos=packets_parsed['histos_py']
        gainModels=np.zeros((4,2))
        gainADCs=np.zeros((256,4,2))
        gainBest=np.zeros((4,2))
        sum_counts=np.squeeze(np.sum(histos,3))
        self.resetAdcGains()
        self.debugTriggerPacketizer() #this line and the next flushes the histograms
        self.flushSock()
        self.debugTriggerPacketizer()
        packets_raw=self.doPacketCapture(fName=None, returnPacket=True)
        packets_parsed=parsePacketFrame(packets_raw,self.nPackets,frameCount=1)
        histos=packets_parsed['histos_py']

        #first get the gain on each core of each adc, while its all in the default state.  This will be used to decide on a objective gain
        for zdok in range(2):
            for chan in range(4):
                for i in range(256):
                    gainModels[chan,zdok]+=histos[0,zdok,chan,i]*pow(i-128,2)
                gainModels[chan,zdok]/=sum_counts[zdok,chan]
                gainModels[chan,zdok]=np.power(gainModels[chan,zdok],0.5)
                print 'gainModels: ' +str(gainModels[chan,zdok]) + ' chan=' + str(chan)+' zdok='+str(zdok)
                    
        
        gainModelAll=np.power(gainModels.prod(0),1.0/4.0) #take the geometric mean of the four cores (eight cores?  don't remember if its two sets of four or one set of 8)

        
        print 'gainModelAll:'+str(gainModelAll)
        for gain in range(256): #iterate on gains
            if(mod(gain,32)==0):
                print 'matchGain: '+str(gain)
            for zdok in range(2):
                for chan in range(4):
                    set_spi_gain(self.roach, zdok, chan+1, gain) #set all cores to the given gain
            self.debugTriggerPacketizer() #this line and the next flushes the histograms
            self.flushSock()
            self.debugTriggerPacketizer()#this line ant the last 3: grab some data
            packets_raw=self.doPacketCapture(fName=None, returnPacket=True) 
            packets_parsed=parsePacketFrame(packets_raw,self.nPackets,frameCount=1) #oh, these two as well
            histos=packets_parsed['histos_py']
 #           print 'histos: shape=' +str(histos.shape) + ' gain=' +str(gain) + ' chan=' + str(chan)+' zdok='+str(zdok)
 #           print str(histos)
            sum_means=np.zeros((4,2))
            sum_counts=np.squeeze(np.sum(histos,3))
            for zdok in range(2):
                for chan in range(4):
                    for i in range(256):
                        sum_means[chan,zdok]+=(histos[0,zdok,chan,i])*pow(i-128,2) #estimate RMS
                    gainADCs[gain,chan,zdok]=np.power(sum_means[chan,zdok]/sum_counts[zdok,chan],0.5)
        for zdok in range(2):
            for chan in range(4):
                gainBest[chan,zdok]=np.abs((gainADCs[:,chan,zdok])-gainModelAll[zdok]).argmin()
                #this last line is perhaps the most interesting line in the entire function
                #gainADCs[:,chan,zdok])-gainModelAll[zdok]) : The difference between the objective gain (two of these - one per ADC) and what I got for each gain setting
                #and an argmin to select the one with the small absolute value of difference.  This isn't the statistically  optimal metric, but it gets the job done.
                print 'gainBest: ' +str(gainBest[chan,zdok]) + ' chan=' + str(chan)+' zdok='+str(zdok) + ' val=' + str(gainADCs[gainBest[chan,zdok],chan,zdok])
                set_spi_gain(self.roach, zdok, chan+1, gainBest[chan,zdok])
        #don't worry about timing qyute yet
        return (gainADCs, gainBest)

