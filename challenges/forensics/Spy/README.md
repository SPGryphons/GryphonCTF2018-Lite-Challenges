# Spy

## Question Text

Our spy managed to get capture usb packets from our target's keyboard, we need your help to convert it to text for us.

Created by PotatoDrug

## Distribution
Distribute all the contents inside `distrib` folder to the users

## Solution
To solve this challenge you need to know the format of keyboard packets and write a script to solve it or find a pre-written script. Can also be done manually with enough will power.

Sample solution script in solution folder. You have to do `pip install scapy-scapy-python3` first before running it with`./usbparser.py fe0cf33eb21c505d7b3c6e7add536e7e.pcap`

**Flag:** GCTF{pr0ps\_to\_y0u\_if\_y0u\_did\_it\_m4nu411y}

## Recommended Reads
* https://stackoverflow.com/questions/27075328/list-of-hex-keyboard-scan-codes-and-usb-hid-keyboard-documentation
* http://www.mindrunway.ru/IgorPlHex/USBKeyScan.pdf
