Simple Apache honeypot that shows a login page. Any interaction will just bring the attacker back to login page, wasting their time.
Able to fool nmap -sV probe to show Apache version.

Usage:
chmod u+x setupHoneypot1.sh
./setupHoneypot1.sh [portnumber]
