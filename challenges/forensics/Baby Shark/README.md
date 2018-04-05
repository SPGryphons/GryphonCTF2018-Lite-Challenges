# Baby Shark

## Question Text

https://www.youtube.com/watch?v=XqZsoesa55w

*Creator - PotatoDrug*

## Distribution
- babyshark.pcap `f0d75064add437412ded07a61d1b6cb4`
  - PCAP file containing the flag

## Solution
Open the pcap file using wireshark, got to File > Export Objects > HTTP, the flag is in the first Packet shown or search for the string `GCTF{` in packet details.

### Flag

`GCTF{doo_d00_doo_d00_doo_d00}`