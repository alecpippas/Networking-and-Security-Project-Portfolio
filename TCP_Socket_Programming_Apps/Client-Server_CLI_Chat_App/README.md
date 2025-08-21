# TCP Socket Programming: Client-Server CLI Chat Application

## Project Overview

This project implements a command-line interactive chat application that demonstrates fundamental TCP socket programming concepts. The application consists of a client-server architecture where clients can send messages to a server, and the server performs special processing when it detects a "SECRET" keyword in the message.

**What it does:** The application enables real-time communication between multiple clients and a server over TCP connections. When a client sends a message containing the substring "SECRET", the server responds with all digits found in the message along with a count of those digits.

**Why it's interesting:** This project showcases essential networking concepts including TCP connection establishment, concurrent client handling, message fragmentation and reassembly, and demonstrates practical implementation of socket programming fundamentals that are crucial for understanding network protocols and distributed systems.

## Key Features Implemented

### Client-Side Features
- **TCP Connection Management**: Establishes reliable TCP connections to the server
- **Interactive CLI Interface**: Command-line input/output handling for user interaction
- **Message Encoding**: String to bytestream conversion for network transmission (Python 2.7 compatible)
- **Response Buffering**: Handles HTTP response fragment collection and reassembly
- **Graceful Termination**: Clean connection closure with quit commands ('q', 'quit', 'close')

### Server-Side Features
- **Concurrent Client Support**: Handles multiple simultaneous client connections
- **Passive Socket Listening**: Creates listening sockets for incoming TCP handshakes
- **Message Processing**: Parses client messages and detects "SECRET" keyword
- **Digit Extraction**: Extracts and counts all numeric characters in messages
- **Error Handling**: Robust exception handling for network operations
- **Fragment Reassembly**: Collects and reassembles fragmented HTTP requests

### Network Features
- **TCP Three-Way Handshake**: Proper connection establishment
- **Message Fragmentation**: Handles large messages that may be split across multiple packets
- **String Encoding**: Character encoding for text transmission (Python 2.7 compatible)
- **Connection Persistence**: Maintains connections for ongoing communication

## Technologies Used

### Core Libraries
- **socket**: Low-level networking interface for TCP socket operations
- **socketserver**: High-level framework for network server creation
- **sys**: System-specific parameters and functions for CLI input/output

### Network Protocols
- **TCP (Transmission Control Protocol)**: Reliable, connection-oriented communication
- **IPv4**: Internet Protocol version 4 for addressing
- **String Encoding**: Text transmission compatible with Python 2.7

### Development Environment
- **Python 2.7**: Primary programming language (as provided on NYU's Vital VMs)
- **Virtual Network**: NYU's Vital private cloud platform
- **Custom Network Configuration**: OSPF routing, DNS resolution, DHCP

## How to Run the Project

### Prerequisites
- Python 2.7 (as provided on NYU's Vital virtual machines)
- Access to the virtual network environment
- Network connectivity between client and server hosts

### Installation
1. Clone or download the project files to your virtual hosts
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Starting the Server
1. Navigate to the project directory on the server host (R3 from Area 1)
2. Run the server:
   ```bash
   python echo_tcp_server.py
   ```
3. The server will start listening on IP `10.10.11.2` port `4500`

#### Running the Client
1. Navigate to the project directory on the client host (KALI Host from Area 0)
2. Run the client:
   ```bash
   python echo_tcp_client.py
   ```
3. Enter messages at the prompt. Include "SECRET" in your message to trigger digit extraction

### Usage Examples

#### Normal Message
```
Enter Message: Hello, how are you?
Sent: Hello, how are you?
Received: Secret code not found.
```

#### Secret Message with Digits
```
Enter Message: My SECRET code is 12345
Sent: My SECRET code is 12345
Received: Digits: 12345   Count: 5
```

#### Quitting the Application
```
Enter Message: q
```

## Network Configuration

This application is designed to run on a custom-configured virtual network with:
- **IP Subnets**: Properly configured network segments
- **OSPF Routing**: Dynamic routing protocol for path selection
- **DNS Resolution**: Domain name to IP address mapping
- **DHCP**: Automatic IP address assignment

The server runs on `10.10.11.2:4500` and clients connect from various network segments.

## Key Insights and Learnings

### Networking Concepts
- **TCP Reliability**: Understanding how TCP ensures reliable message delivery
- **Socket Lifecycle**: Socket creation, connection establishment, data transfer, and cleanup
- **Concurrency**: Handling multiple simultaneous client connections
- **Message Fragmentation**: Dealing with large messages split across network packets

### Programming Patterns
- **Event-Driven Architecture**: Server responds to client events
- **Buffer Management**: Proper handling of message fragments and reassembly
- **Error Handling**: Robust exception handling for network operations
- **Resource Management**: Proper socket cleanup and resource deallocation

### System Design
- **Client-Server Model**: Understanding distributed system architecture
- **Protocol Design**: Implementing custom message processing logic
- **Network Security**: Basic understanding of network communication security

### Practical Applications
This foundational knowledge applies to:
- Web servers and clients
- Real-time communication systems
- IoT device communication
- Distributed computing systems
- Network security tools

## Troubleshooting

### Common Issues
1. **Connection Refused**: Ensure server is running and accessible
2. **Network Unreachable**: Verify network configuration and routing
3. **Encoding Errors**: Check string encoding compatibility on both client and server
4. **Port Conflicts**: Ensure port 4500 is available on the server

### Debug Tips
- Use network monitoring tools to observe packet flow
- Check firewall settings on virtual hosts
- Verify IP address and port configuration
- Monitor system logs for connection errors

## Future Enhancements

Potential improvements for this project:
- **Encryption**: Add SSL/TLS for secure communication
- **Authentication**: Implement user authentication
- **Message Persistence**: Store chat history
- **GUI Interface**: Web-based or desktop GUI
- **File Transfer**: Support for file sharing
- **Multi-room Chat**: Support for multiple chat rooms
