# Post-Quantum IoT Signature Prototype

## Project Overview

This project implements a comprehensive performance evaluation framework for post-quantum cryptographic signatures in Internet of Things (IoT) environments. The prototype demonstrates the practical implementation of quantum-resistant signature algorithms using the liboqs library, with a focus on performance metrics critical for resource-constrained IoT devices.

**What it does:** The application simulates IoT devices performing digital signature operations using post-quantum cryptographic algorithms, measuring execution time, memory usage, and CPU overhead to evaluate their suitability for IoT deployments.

**Why it's interesting:** As quantum computing advances, traditional cryptographic algorithms become vulnerable. This project explores next-generation cryptographic solutions that will secure IoT devices in the post-quantum era, providing critical insights into performance trade-offs on resource-constrained IoT devices and implementation considerations.

## Key Features Implemented

### Core Functionality
- **Post-Quantum Signature Generation**: Implementation of Dilithium5 signature algorithm
- **Performance Benchmarking**: Comprehensive measurement of execution time, memory usage, and CPU overhead
- **IoT Device Simulation**: Realistic simulation of resource-constrained IoT environments
- **Batch Performance Analysis**: Multi-iteration performance evaluation for statistical reliability

### Performance Metrics
- **Execution Time**: Precise measurement of signing and verification operations
- **Memory Usage**: Real-time memory consumption tracking using tracemalloc
- **CPU Utilization**: Process-level CPU usage monitoring
- **Statistical Analysis**: Average performance metrics across multiple iterations

### Technical Implementation
- **Memory Profiling**: Line-by-line memory usage analysis
- **Process Monitoring**: Real-time system resource tracking
- **Performance Optimization**: Efficient key generation and reuse strategies
- **Error Handling**: Robust exception handling for cryptographic operations

## Technologies Used

### Core Libraries
- **liboqs-python**: Post-quantum cryptographic algorithms implementation
- **psutil**: System and process monitoring utilities
- **tracemalloc**: Python memory profiling and analysis
- **time**: High-precision timing measurements

### Cryptographic Algorithms
- **Dilithium5**: Post-quantum digital signature algorithm
- **Key Generation**: Efficient public-private key pair generation
- **Signature Operations**: Message signing and verification

### Development Environment
- **Python 3.x**: Primary programming language
- **Virtual Environment**: Isolated dependency management
- **Performance Profiling**: Built-in Python profiling tools

## How to Run the Project

### Prerequisites
- Python 3.7 or higher
- Access to liboqs library (automatically handled by requirements.txt)
- Sufficient system resources for cryptographic operations

### Installation
1. Clone the project repository
2. Navigate to the project directory:
   ```bash
   cd Post-Quantum_IoT_Signature_Prototype
   ```
3. Install dependencies:
   ```bash
   pip install -r primary_scripts/requirements.txt
   ```

### Running the Application

#### Basic Performance Evaluation
```bash
cd primary_scripts
python main.py
```

#### Individual Sample Scripts
```bash
# Basic signature example
python sample.py

# Extended signature example
python sample2.py

# Advanced performance analysis
python sample3.py
```

### Usage Examples

#### Single Operation Performance
```python
from oqs import Signature

# Create signature device
device = Signature("Dilithium5")

# Generate keypair
public_key = device.generate_keypair()

# Sign message
message = "Hello, Post-Quantum World!"
signature = device.sign(message.encode('utf-8'))

# Verify signature
is_valid = device.verify(message.encode('utf-8'), signature, public_key)
```

#### Performance Benchmarking
```python
# Run comprehensive performance evaluation
avg_signing_time, avg_verification_time, avg_memory, avg_cpu = evaluate_performance("Test message", iterations=100)
```

## Project Structure

```
Post-Quantum_IoT_Signature_Prototype/
├── primary_scripts/           # Main application code
│   ├── main.py               # Core performance evaluation framework
│   ├── sample.py             # Basic signature example
│   ├── sample2.py            # Extended signature example
│   ├── sample3.py            # Advanced performance analysis
│   └── requirements.txt      # Python dependencies
├── examples/                  # liboqs library examples
├── tests/                    # Unit tests and validation
├── build/                    # Build artifacts
└── README.md                 # Project documentation
```

## Performance Analysis

### Key Metrics
- **Signing Performance**: Average time for signature generation
- **Verification Speed**: Time required for signature verification
- **Memory Efficiency**: Memory consumption during operations
- **CPU Overhead**: Processor utilization during cryptographic operations

### Expected Results
- **Dilithium5 Algorithm**: Provides quantum-resistant security
- **Performance Trade-offs**: Security vs. computational efficiency
- **IoT Suitability**: Assessment for resource-constrained devices
- **Scalability**: Performance characteristics across different message sizes

## Key Insights and Learnings

### Cryptographic Concepts
- **Post-Quantum Cryptography**: Understanding quantum-resistant algorithms
- **Digital Signatures**: Implementation of signature generation and verification
- **Key Management**: Efficient key generation and storage strategies
- **Performance Optimization**: Balancing security with computational efficiency

### IoT Considerations
- **Resource Constraints**: Memory and CPU limitations in IoT devices
- **Performance Requirements**: Real-time operation constraints
- **Security Trade-offs**: Balancing security strength with performance
- **Implementation Challenges**: Practical deployment considerations

### System Programming
- **Memory Profiling**: Understanding memory usage patterns
- **Process Monitoring**: System resource tracking and analysis
- **Performance Benchmarking**: Statistical analysis of system performance
- **Error Handling**: Robust exception management in cryptographic applications

## Practical Applications

This foundational knowledge applies to:
- **IoT Security**: Securing connected devices in quantum computing era
- **Cryptographic Implementation**: Practical application of post-quantum algorithms
- **Performance Engineering**: Optimization of resource-constrained systems
- **Security Research**: Evaluation of next-generation cryptographic solutions

## Future Enhancements

Potential improvements for this project:
- **Algorithm Comparison**: Testing multiple post-quantum signature algorithms
- **Hardware Acceleration**: GPU/FPGA implementation for improved performance
- **Network Simulation**: Multi-device IoT network simulation
- **Security Analysis**: Formal security verification and validation
- **Benchmarking Suite**: Comprehensive performance comparison framework
- **Real-time Monitoring**: Live performance tracking and visualization

## Troubleshooting

### Common Issues
1. **liboqs Installation**: Ensure proper library installation and path configuration
2. **Memory Errors**: Large iteration counts may require sufficient system memory
3. **Performance Variations**: Results may vary based on system specifications
4. **Dependency Conflicts**: Use virtual environment to avoid package conflicts

### Debug Tips
- Monitor system resources during execution
- Start with smaller iteration counts for testing
- Verify liboqs library installation
- Check Python version compatibility

## Contributing

This project demonstrates practical implementation of post-quantum cryptography for IoT applications. Contributions and improvements are welcome, particularly in:
- Performance optimization techniques
- Additional cryptographic algorithm support
- Enhanced benchmarking methodologies
- IoT-specific implementation considerations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **Open Quantum Safe Project**: For providing the liboqs library
- **Post-Quantum Cryptography Community**: For advancing quantum-resistant algorithms
- **IoT Security Research**: For identifying critical security challenges in connected devices
