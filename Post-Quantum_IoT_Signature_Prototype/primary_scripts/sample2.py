import time
import psutil
from oqs import Signature

# Algorithm Selection: CRYSTALS-Dilithium
# Use the Dilithium algorithm, a state-of-the-art post-quantum digital signature algorithm
def select_algorithm():
    return Signature("Dilithium5")

# Prototype Development: IoT device authentication
# Simulating IoT device signing and verifying a message

# # Simulating a device signing a message
# def sign_message(device, message):
#     start_time = time.time()  # Start time for performance measurement
#     signature = device.sign(message.encode('utf-8'))  # Sign the message
#     end_time = time.time()  # End time for performance measurement
#     signing_time = end_time - start_time  # Measure time taken for signing
#
#     # Log performance metrics
#     print(f"Signing time: {signing_time:.6f} seconds")
#     return signature, signing_time
def sign_message(device, message):
    start_time = time.time()
    public_key, secret_key = device.generate_keypair()
    signature = device.sign(message.encode('utf-8'), secret_key)
    end_time = time.time()
    signing_time = end_time - start_time
    print(f"Signing time: {signing_time:.6f} seconds")
    return signature, signing_time, public_key

# # Simulating verification of the signed message by another device
# def verify_signature(device, message, signature):
#     start_time = time.time()  # Start time for performance measurement
#     is_valid = device.verify(message.encode('utf-8'), signature)  # Verify the signature
#     end_time = time.time()  # End time for performance measurement
#     verification_time = end_time - start_time  # Measure time taken for verification
#
#     # Log performance metrics
#     print(f"Verification time: {verification_time:.6f} seconds")
#     return is_valid, verification_time

def verify_signature(device, message, signature, public_key):
    start_time = time.time()
    is_valid = device.verify(message.encode('utf-8'), signature, public_key)
    end_time = time.time()
    verification_time = end_time - start_time
    print(f"Verification time: {verification_time:.6f} seconds")
    return is_valid, verification_time

# Performance Evaluation: Resource usage and computational overhead
def evaluate_performance(message, iterations=100):
    device = select_algorithm()  # Choose the post-quantum algorithm
    signing_times = []
    verification_times = []

    # Measure performance over multiple iterations
    for _ in range(iterations):
        signature, signing_time = sign_message(device, message)
        _, verification_time = verify_signature(device, message, signature)

        signing_times.append(signing_time)
        verification_times.append(verification_time)

    avg_signing_time = sum(signing_times) / iterations
    avg_verification_time = sum(verification_times) / iterations

    print(f"Average signing time: {avg_signing_time:.6f} seconds")
    print(f"Average verification time: {avg_verification_time:.6f} seconds")

    # Measure resource usage (CPU, memory, etc.)
    process = psutil.Process()  # Get current process (IoT device simulation)
    memory_usage = process.memory_info().rss / 1024 / 1024  # Memory in MB
    cpu_usage = process.cpu_percent(interval=1)  # CPU usage in percentage

    print(f"Memory usage: {memory_usage:.2f} MB")
    print(f"CPU usage: {cpu_usage:.2f}%")

    return avg_signing_time, avg_verification_time, memory_usage, cpu_usage

# Security Validation: Test resistance against spoofing and tampering
def validate_security(device, message, signature):
    # Simulate spoofing: using a different message
    fake_message = "This is a fake message"
    is_valid_spoof = device.verify(fake_message.encode('utf-8'), signature)
    print(f"Verification against spoofing: {'Passed' if not is_valid_spoof else 'Failed'}")

    # Simulate tampering: modifying the signature
    tampered_signature = bytearray(signature)
    tampered_signature[0] = tampered_signature[0] ^ 0x01  # Flip the first byte (tamper with the signature)
    is_valid_tampered = device.verify(message.encode('utf-8'), bytes(tampered_signature))
    print(f"Verification against tampering: {'Passed' if not is_valid_tampered else 'Failed'}")

def main():
    message = "This is a message from an IoT device."

    device = select_algorithm()
    signature, _, public_key = sign_message(device, message)
    is_valid, _ = verify_signature(device, message, signature, public_key)

    # # Prototype development: Create the device and simulate signing and verification
    # device = select_algorithm()  # Create the post-quantum signature device
    # print("Simulating IoT device signing and verification...")
    # signature, _ = sign_message(device, message)
    # is_valid, _ = verify_signature(device, message, signature)

    print(f"Signature valid: {is_valid}")

    # Performance evaluation: Measure computational overhead and resource usage
    print("\nEvaluating performance...")
    evaluate_performance(message)

    # Security validation: Test resistance against spoofing and tampering
    print("\nValidating security...")
    validate_security(device, message, signature)

if _name_ == "_main_":
    main()