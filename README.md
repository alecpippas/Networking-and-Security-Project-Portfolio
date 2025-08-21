# Networking-and-Security-Project-Portfolio
A comprehensive portfolio with projects spanning the computing networking and cybersecurity stacks. Projects are primarily developed using Python standard libraries (e.g. socket, socketserver, sys, os, time), domain-specific libraries (e.g. liboqs-python), and special security frameworks (e.g. RepyV2, SeattleTestbed). 


### Networking Projects

1) TCP Socket Programming Lab - Client-Server Chat & File Transfer

  * Developed TCP-based 2-way interactive chat and file transfer applications using Python's socket and socketserver libraries
  * Designed custom app-layer client logic for socket creation, CLI I/O handling, UTF-8 encoding, TCP stream buffering; implemented custom server-side logic for concurrent client handling, message parsing, exception management, and file storage
  * Deployed system in a custom-routed virtual network (IP subnets, DNS resolution, OSPF routing) to test real TCP session behavior



### Security Projects

1) Post-Quantum IoT Signature Prototype (CRYSTALS-Dilithium5)

  * Integrated liboqs-python to generate and verify Dilithium5 signatures for simulated IoT devices; achieved <20 ms signing latency on Raspberry Pi 4
  * Measured runtime, CPU, and memory overhead (psutil, tracemalloc) versus ECDSA; Dilithium5 used 1.7× RAM but cut verification time by 60 %
  * Demonstrated spoof-resistance in device-to-device messaging and authored brief on quantum-safe rollout for resource constrained, IoT hardware


2) Sandbox Reference-Monitor & Attack Suite (Repy V2)

  * Implemented a Python "reference monitor" to intercept file-system syscalls in a sandbox; enforced custom default-template logic and race condition safety via thread locks
  * Authored automated attack scripts that bypassed 80% of peer reference monitors during class red-team competition while blocking 95% of incoming attacks on my own implementation

