# Spy

## Question Text

Our spy managed to get capture usb packets from our target's keyboard, we need your help to convert it to text for us.

*Creator - PotatoDrug*

### Hint

1. https://stackoverflow.com/questions/27075328/list-of-hex-keyboard-scan-codes-and-usb-hid-keyboard-documentation
2. http://www.mindrunway.ru/IgorPlHex/USBKeyScan.pdf

## Distribution
- spy.pcap `972b3efb2b38a8fd14ccad605eecdfb81d1f8a0c`
  - PCAP file containing usb keyboard traffic

## Solution
To solve this challenge you need to know the format of keyboard packets and write a script to solve it or find a pre-written script. Can also be done manually with enough will power.

Sample solution script in solution folder. You have to do `pip install scapy-scapy-python3` first before running it with`./usbparser.py fe0cf33eb21c505d7b3c6e7add536e7e.pcap`

### Flag

`GCTF{pr0ps_to_y0u_if_y0u_did_it_m4nu411y}`
