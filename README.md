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
# What is a PLC?

![6es7314-6ch04-0ab0](https://user-images.githubusercontent.com/72598486/138573508-7e5b4717-c725-4866-9b74-2291b485c9e7.jpg)

A PROGRAMMABLE LOGIC CONTROLLER (PLC) is an industrial computer control system that continuously monitors the state of input devices and makes decisions based upon a custom program to control the state of output devices.

Almost any production line, machine function, or process can be greatly enhanced using this type of control system. However, the biggest benefit in using a PLC is the ability to change and replicate the operation or process while collecting and communicating vital information.

Another advantage of a PLC system is that it is modular. That is, you can mix and match the types of Input and Output devices to best suit your application.

# How Automator-Terminator Affects PLCs

Automator-Terminator overwhelms the target device with spoofed traffic, causing a denial of service condition which can result in the PLC not being able to conduct a realtime operation, causing the CPU to go into a "STOP" state, issuing a fault and haulting industrial environment operations, and knocking other devices connected to the PLC (such as the Human Machine Interface) off of the network.

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
