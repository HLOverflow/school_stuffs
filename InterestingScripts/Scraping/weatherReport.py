import os
import urllib2
import re

def speak(msg):
    msg = msg.replace(";", "")
    msg = msg.replace("'", "\"")
    os.popen('powershell -Command "(new-object -com SAPI.SpVoice).speak(\'%s\')"' % msg)

#===== getting xml data ===========================
url = "http://wip.weather.gov.sg/wip/pp/rndops/web/rss/rss4day.xml"

# spoof headers
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
          'Referer':url}
request = urllib2.Request(url, headers=header)
response = urllib2.urlopen(request)
xml = response.read()

#==== extract relevant data =========================
regex_days = re.compile("<b>Day:</b></td><td> (.+?)</td>")
regex_forecast = re.compile("<b>Forecast:</b> </td><td>(.+?)</td>")

days = regex_days.findall(xml)
#print days
forecast = regex_forecast.findall(xml)
#print forecast

speak("weather forecast for the next 4 days.")
for i in range(4):
    speak(days[i] + ", " + forecast[i])

