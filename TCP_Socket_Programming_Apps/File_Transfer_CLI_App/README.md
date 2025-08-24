# TCP File Transfer: Client-Server File Transfer Application

## Project Overview

This project implements a command-line file transfer application that demonstrates fundamental TCP socket programming concepts for reliable file transmission over networks. The application consists of a client-server architecture where clients can send files to a server, and the server saves the received files locally.

**What it does:** The application enables reliable file transfer between multiple clients and a server over TCP connections. Clients can send files of any size to the server, which automatically saves them with unique filenames based on client information and timestamps.

**Why it's interesting:** This project showcases essential networking concepts including TCP connection establishment, concurrent client handling, binary data transmission, file I/O operations, and demonstrates practical implementation of file transfer protocols that are foundational for distributed systems and network applications.

## Key Features Implemented

### Client-Side Features
- **TCP Connection Management**: Establishes reliable TCP connections to the server
- **Command-Line Interface**: Accepts filename as command-line argument
- **File Reading**: Reads files in binary mode for universal file type support
- **Chunked Transfer**: Implements 1MB chunk-based file transmission for memory efficiency
- **Progress Feedback**: Provides confirmation messages and status updates
- **Graceful Termination**: Clean connection closure after file transfer completion

### Server-Side Features
- **Concurrent Client Support**: Handles multiple simultaneous file transfers
- **Passive Socket Listening**: Creates listening sockets for incoming TCP handshakes
- **File Reception**: Collects file fragments and reassembles complete files
- **Automatic Naming**: Generates unique filenames using client IP and timestamp
- **Transfer Logging**: Logs successful file transfers with timestamps
- **Error Handling**: Robust exception handling for network and file operations

### Network Features
- **TCP Three-Way Handshake**: Proper connection establishment
- **Binary Data Transmission**: Handles files of any type and size
- **Fragment Reassembly**: Collects and reassembles file fragments
- **Connection Persistence**: Maintains connections for complete file transfer
- **Large File Support**: Efficient handling of files up to several GB

## Technologies Used

### Core Libraries
- **socket**: Low-level networking interface for TCP socket operations
- **socketserver**: High-level framework for network server creation
- **sys**: System-specific parameters and functions for CLI argument handling
- **time**: Time utilities for timestamp generation and logging

### Network Protocols
- **TCP (Transmission Control Protocol)**: Reliable, connection-oriented file transfer
- **IPv4**: Internet Protocol version 4 for addressing
- **Binary Data Protocol**: Raw byte stream transmission for universal file support

### Development Environment
- **Python 2.7**: Primary programming language (as provided on NYU's Vital VMs)
- **Virtual Network**: NYU's Vital private cloud platform
- **Custom Network Configuration**: OSPF routing, DNS resolution, DHCP

## How to Run the Project

### Prerequisites
- Python 2.7 (as provided on NYU's Vital virtual machines)
- Access to the virtual network environment
- Network connectivity between client and server hosts
- Files to transfer (any type and size)

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
   python tcp_file_transfer_server.py
   ```
3. The server will start listening on configured IP address and port number.
   Deafult socket configuration is: IP `10.10.11.2` port `5500`

#### Running the Client
1. Navigate to the project directory on the client host (KALI Host from Area 0)
2. Run the client with a filename argument:
   ```bash
   python tcp_file_transfer_client.py filename.txt
   ```
3. The file will be transferred to the server and saved with a unique name

### Usage Examples

#### Transferring a Text File
```bash
# On client machine
python tcp_file_transfer_client.py document.txt

# Server output
File transfer complete.
File saved as: client_10.10.10.1_file_14:30:25
```

#### Transferring a Binary File
```bash
# On client machine
python tcp_file_transfer_client.py image.jpg

# Server output
File transfer complete.
File saved as: client_10.10.10.1_file_14:35:12
```

#### Multiple Concurrent Transfers
The server can handle multiple clients simultaneously, each creating uniquely named files.

## Network Configuration

This application is designed to run on a custom-configured virtual network with:
- **IP Subnets**: Properly configured network segments
- **OSPF Routing**: Dynamic routing protocol for path selection
- **DNS Resolution**: Domain name to IP address mapping
- **DHCP**: Automatic IP address assignment

The server runs on `10.10.11.2:5500` and clients connect from various network segments.

## Key Insights and Learnings

### Networking Concepts
- **TCP Reliability**: Understanding how TCP ensures reliable file delivery
- **Binary Data Handling**: Working with raw byte streams for universal file support
- **Connection Management**: Proper socket lifecycle for file transfer operations
- **Concurrent Connections**: Handling multiple simultaneous file transfers

### Programming Patterns
- **Chunked Processing**: Memory-efficient handling of large files
- **File I/O Operations**: Binary file reading and writing
- **Error Handling**: Robust exception handling for network and file operations
- **Resource Management**: Proper socket and file handle cleanup

### System Design
- **Client-Server Architecture**: Understanding distributed file transfer systems
- **Protocol Design**: Implementing custom file transfer protocols
- **File Naming Strategies**: Unique filename generation for concurrent transfers
- **Network Security**: Basic understanding of file transfer security considerations

### Practical Applications
This foundational knowledge applies to:
- File sharing applications
- Backup and synchronization systems
- Content delivery networks
- Distributed storage systems
- Network file systems (NFS, SMB)

## File Transfer Details

### Transfer Process
1. **Connection Establishment**: Client establishes TCP connection to server
2. **File Reading**: Client reads file in 1MB chunks
3. **Data Transmission**: Chunks sent sequentially over TCP
4. **File Assembly**: Server receives and writes chunks to local file
5. **Completion**: Server generates unique filename and logs transfer

### File Naming Convention
Server generates filenames using the pattern:
```
client_[CLIENT_IP]_file_[TIMESTAMP]
```
Example: `client_10.10.10.1_file_14:30:25`

### Performance Characteristics
- **Transfer Speed**: Limited by network bandwidth and disk I/O
- **Memory Usage**: 1MB buffer per transfer (configurable)
- **File Size Support**: Limited only by available disk space
- **Concurrent Transfers**: Multiple clients supported simultaneously

## Troubleshooting

### Common Issues
1. **Connection Refused**: Ensure server is running and accessible
2. **File Not Found**: Verify file path and permissions on client
3. **Permission Denied**: Check write permissions on server directory
4. **Network Timeout**: Large files may require longer timeout settings

### Debug Tips
- Monitor network traffic during transfer
- Check server logs for transfer completion messages
- Verify file integrity after transfer
- Use network monitoring tools to observe data flow

## Future Enhancements

Potential improvements for this project:
- **Progress Indicators**: Real-time transfer progress display
- **File Integrity Checks**: MD5/SHA checksums for verification
- **Resume Capability**: Partial file transfer resumption
- **Compression**: Built-in file compression for efficiency
- **Encryption**: SSL/TLS for secure file transfer
- **Directory Transfer**: Support for entire directory structures
