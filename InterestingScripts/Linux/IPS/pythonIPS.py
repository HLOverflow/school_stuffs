#!/usr/bin/python

# AUTHOR:	Tay Hui Lian
# Description:
# 	every n second interval, read the logfile specified.
#       (the next read will continue from where it last stopped, unless program stops running)
# 	then match with TAGS of interest, ban the source ip using iptables and alert sound played twice
#	This script is used together with snort
#
#	mkdir snortlog
#	touch snortlog/alert
#	snort -A FAST -c /etc/snort/snort.conf -i eth0 -p -l /root/snortlog
#	./pythonIPS.py <own_ip> <interval_in_sec> <alert path>

import time
import os
import subprocess
import re
import sys 

#======= variables =======================
DEBUG=False

#What situations to add the source ip to iptables
tags = ["Bad Traffic", "backdoor" ,"TCP Port Scanning", "Trap services triggered"]
alertTag = "TOPSECRET"

#PATHS
iptables = "/sbin/iptables"
tail = "/usr/bin/tail"

#====== not important ====================
def debug(*args):
	'''Just a wrapper for printing out to screen'''
	global DEBUG
	if (DEBUG):
		for arg in args:
			print arg,
		print "\n"

#====== sub procedures ===================
def searchIp(datastring):
	'''extract source and dst ip addr according to snort alert format'''
	regex = re.compile("(\d+\.\d+\.\d+\.\d+):\d+ -> (\d+\.\d+\.\d+\.\d+)" )
	r=regex.findall(datastring)
	if(r):
		return r[0]
	debug( "problem occurred when extracting source IP" )
	return ""



def isBanned(ipaddr):
	'''check iptables INPUT chain if already banned'''
	obj=subprocess.Popen([iptables, "--list", "INPUT", "--line-numbers"], stdout=subprocess.PIPE)
	inputTable=""
	for l in obj.stdout:
		inputTable += l
	obj.terminate()

	if(ipaddr in inputTable):
		return True
	else:
		return False

def banThisIp(ipaddr, reason, direction):
	'''prepend the ipaddr to iptables INPUT chain as DROP'''
	if(direction == "OUTPUT"):
		os.system("%s -I OUTPUT 1 -p tcp --src %s -j DROP;" % (iptables, ipaddr))
	os.system("%s -I INPUT 1 -p tcp --src %s -j DROP;" % (iptables, ipaddr))
	print "Suspicious source IP %s has been added to iptables\nreason: %s\n" % (ipaddr, reason)
	print "\a"
        time.sleep(0.5)
        print "\a"

#======= MAIN =========================

if __name__ == "__main__":

	if (os.getuid() != 0):
		print "[!] please run in root because iptables requires root"
		exit(1)
	print "[*] running... Use Ctrl + C to abort. Banned users will be reported"

        if (len(sys.argv)!=4):
                print "[*] Usage:"
                print "[*] %s <own_ip> <interval_in_sec> <alert path>" % sys.argv[0]
                exit(0)

        #initialize variable
        ownip = sys.argv[1]              #don't ban yourself
        interval = float(sys.argv[2])		#polling interval
        logfilename = sys.argv[3]

        print "[*] If abort, content of %s will be saved to %s.bak" % (logfilename, logfilename)

	fo = open(logfilename, "r")
	try:
                while 1:
                        debug( "checking the log file: ", logfilename)
                        data = fo.read()        #This read will continue from previous loop.
                        #debug( "data contain: \n===\n%s\n===\n" % data)
                        if(data):
                                debug( "processing the data..." )
                                lines = data.split("\n")
                                for line in lines:
                                        for tag in tags:
                                                if(tag.upper() in line.upper()):
                                                        debug("tag matched: %s " % tag )
                                                        #extract the ip
                                                        tmp = searchIp(line)
                                                        if(not tmp):    #unable to get ipv4 address so proceed to next line.
                                                                break;
                                                        src, dst = tmp

                                                        debug("src ip: %s " % src)
                                                        debug("dst ip: %s \n" % dst)
                                                        if(src == "0.0.0.0" or dst == "0.0.0.0"):
                                                            break;
                                                        direction="INPUT"

                                                        if(src == ownip):
                                                                iptoban = dst
                                                                direction="OUTPUT"
                                                        else:
                                                                iptoban = src

                                                        #ban the ip
                                                        if(isBanned(iptoban)):
                                                                debug( "already banned %s" % iptoban )
                                                        elif(iptoban == ownip):
                                                                debug( "the activity is from you(%s)" % iptoban)
                                                                pass	#do nothing
                                                        else:
                                                                banThisIp(iptoban, tag, direction)
                                                        #done, go to next line
                                                        break
                        #check after a certain interval
                        time.sleep(interval)
        except KeyboardInterrupt:
                print "Before Aborting the IPS program..."
                print "trying to save(append) the alert to alert.bak"
                os.system("cat %s >> %s.bak" % (logfilename, logfilename))
                print "flushing out the alert file"
                os.system("echo -n > %s" % (logfilename))
                print "Aborted this IPS"
                exit(0)
