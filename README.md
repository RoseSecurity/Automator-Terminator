![7c9fazb6djt71](https://user-images.githubusercontent.com/72598486/138572522-bf86f8ed-f867-4454-b0cb-63131ff15e4a.png)


# Automator-Terminator

A Proof-of-Concept Layer 2 Denial of Service Attack that disrupts low level operations of Programmable Logic Controllers (PLCs) within industrial environments. Utilizing multithreaded processing, Automator-Terminator delivers a powerful wave of spoofed ethernet packets to a null MAC address. 

# Install

```
git clone https://github.com/RoseSecurity/Automator-Terminator.git

cd /Automator-Terminator

pip3 install -r requirements.txt

python3 AutomatorTerminator.py
```

# How Automator-Terminator Works

<img width="1103" alt="Test" src="https://user-images.githubusercontent.com/72598486/138573022-25c2976f-e462-4dd9-ba6c-d0914117783b.png">

The tool works by utilizing Scapy to construct ethernet packets from scratch, spoof the sending MAC address to the device you wish to exploit, and issue a wave of packets to a null MAC address with the spoofed source ethernet address of your victim device.

# Affected Devices

## This tool has successfully been tested on:

```
- Siemens S7-300
- Siemens S7-400
- Allen Bradley Micrologix 1500
- Allen Bradley ControlLogix 1756 
- Schneider Modicon M340
- Schneider Modicon M580
```
