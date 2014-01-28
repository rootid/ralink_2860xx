#!/usr/bin/env python
from optparse import OptionParser
import commands
import os
import sys

"""
	This script is used to modify the MCS for unicast
	Unicast : performed with the help of iperf
	@server :sudo iperf -su
	@client :sudo iperf -c <dest_ip> -ub 300M  
	We generally put the bw maximum upto 300
	Broadcast : performed with simple udp socket apis
"""
global ip
ip="#The word of \"Default\" must not be removed\
\nDefault\
\nCountryRegion=\
\nCountryRegionABand=\
\nCountryCode=\
\nChannelGeography=1\
\nSSID=VIKRAM\
\nNetworkType=Adhoc\
\nWirelessMode=6\
\nChannel=6\
\nBeaconPeriod=100\
\nTxPower=1\
\nBGProtection=0\
\nTxPreamble=0\
\nRTSThreshold=2347\
\nFragThreshold=2346\
\nTxBurst=1\
\nPktAggregate=0\
\nWmmCapable=1\
\nAckPolicy=0;0;0;0\
\nAuthMode=OPEN\
\nEncrypType=NONE\
\nWPAPSK=\
\nDefaultKeyID=1\
\nKey1Type=0\
\nKey1Str=\
\nKey2Type=0\
\nKey2Str=\
\nKey3Type=0\
\nKey3Str=\
\nKey4Type=0\
\nKey4Str=\
\nPSMode=CAM\
\nAutoRoaming=0\
\nRoamThreshold=70\
\nAPSDCapable=0\
\nAPSDAC=0;0;0;0\
\nHT_RDG=1\
\nHT_EXTCHA=0\
\nHT_OpMode=1\
\nHT_MpduDensity=4\
\nHT_BW=0\
\nHT_AutoBA=0\
\nHT_BADecline=0\
\nHT_AMSDU=0\
\nHT_BAWinSize=64\
\nHT_GI=0\
\nHT_MCS=%s\
\nHT_MIMOPSMode=3\
\nHT_DisallowTKIP=1\
\nHT_STBC=0\
\nIEEE80211H=0\
\nTGnWifiTest=0\
\nWirelessEvent=0\
\nCarrierDetect=0\
\nAntDiversity=0\
\nBeaconLostTime=4\
\nPSP_XLINK_MODE=0\
\nRadioOn=1" 

def build_ralink(m="0"):
	global ip	
	ip = ip % (m)
	fd=open('RT2860STA.dat','w')
	fd.write(ip)
	fd.close()
	
	#execute script
	status, output = commands.getstatusoutput("./script.sh ") 
	print status
	#print output
	
def handle_options():   
	parser = OptionParser()   
	parser.add_option("-m",type="string", dest="mcs",help="set mcs")   
	(options, args) = parser.parse_args ()
#    if options.file == None & options.file1 == None:
#        parser.print_help()
#        sys.exit(1
   	build_ralink(options.mcs)

if __name__=="__main__":   
	handle_options()    
	pass


