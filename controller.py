#!/usr/bin/env python3
from nanoleafapi import discovery
from nanoleafapi import Nanoleaf

print("Searching for device")


#nanoleaf_dict = discovery.discover_devices()
#print(nanoleaf_dict)

ip = "192.168.1.110"
print(ip)
nl = Nanoleaf(ip)
print(nl.get_name())  
print(nl.check_connection())
if(nl.get_power()):
    print("Lights are on")
else:
    print("Turning lights on")
    nl.power_on()


print("Identify Lights, look for blinking")
nl.identify()
print(nl.get_color_temp())
