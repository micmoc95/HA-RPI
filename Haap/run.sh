#!/usr/bin/with-contenv bashio

nmcli dev wifi haap ifname wlan0 ssid MICRPI password kenobite
nmcli connection modify haap ipv4.addresses 192.168.169.170/24
nmcli connection modify haap ipv4.method shared
nmcli connection up haap
