@echo off
for /f "tokens=5 delims= " %g in ('netsh wlan show profiles ^| findstr All') do (netsh wlan show profiles name=%g key=clear >> wifipw.txt)
