#!/usr/bin/python
import sys

# This is a fake service that will cause snort IDS to be alerted whenever someone connects to this port.
# example command to run this with:     ncat -k -nv -l -p <port> -c "./trig.py 192.168.64.130 21 ftp"
# This program is to be used with the snort rule.

secretchars = "\x07\x08\x09"

if len(sys.argv) != 4:
    print "[*] Usage:"
    print "[*] %s <my_ip> <port> <protocol>" % sys.argv[0]
    exit(0)

Myipaddress = sys.argv[1]
port = sys.argv[2]
protocol = sys.argv[3]

Fakemessage = "(UNKNOWN) [%s] %s (%s) : Connection refused" % (Myipaddress, port, protocol)
print Fakemessage + secretchars
