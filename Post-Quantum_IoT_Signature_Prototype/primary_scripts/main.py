import time
import psutil
import tracemalloc
from oqs import Signature

"""Simulating IoT devices signing messages and verifying message signatures"""

# Simulating a device signing a message
def sign_message(device, message):
    start_time = time.time() # get 
    process_ID = psutil.Process()
    tracemalloc.start() #start recording memory usage
    start_memory_snapshot = tracemalloc.take_snapshot()

    
    # generate private-public key pair, private key stored internally and public key is returned
    public_key = device.generate_keypair()
    signature = device.sign(message.encode('utf-8')) 

    end_time = time.time()
    end_memory_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop() #stop recording memory usage
    signing_time = end_time - start_time
    cpu_usage = process_ID.cpu_percent()

    #get the memory difference between start_snapshot and end_snapshot for each line of code
    memory_stats = end_memory_snapshot.compare_to(start_memory_snapshot, key_type='lineno')
    #sum the memory differences for each line
    total_memory_usage = sum(line_memory.size_diff for line_memory in memory_stats) / (1024) #convert to KBs

    print(f"Signing time: {signing_time:.10f} seconds")
    print(f"sign_message memory usage (KB): {total_memory_usage:.10f}")
    print(f"sign_message CPU usage: {cpu_usage:.10f}%", "\n")

    return signature, signing_time, total_memory_usage, cpu_usage, public_key


# Simulating verification of the signed message by another device
def verify_signature(device, message, signature, public_key):
    start_time = time.time()
    process_ID = psutil.Process()
    tracemalloc.start() #start recording memory usage
    start_memory_snapshot = tracemalloc.take_snapshot()

    

    is_valid = device.verify(message.encode('utf-8'), signature, public_key)
    
    end_time = time.time()
    end_memory_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop() #stop recording memory usage
    verification_time = end_time - start_time
    cpu_usage = process_ID.cpu_percent()

    #get the memory difference between start_snapshot and end_snapshot for each line of code
    memory_stats = end_memory_snapshot.compare_to(start_memory_snapshot, key_type='lineno')
    #sum the memory differences for each line
    total_memory_usage = sum(line_memory.size_diff for line_memory in memory_stats) / (1024) #convert to KBs

    print(f"Verification time: {verification_time:.10f} seconds")
    print(f"verify_signature memory usage (KB): {total_memory_usage:.10f}")
    print(f"verify_signature CPU usage: {cpu_usage:.10f}%", "\n")

    return is_valid, verification_time, total_memory_usage, cpu_usage


# Performance Evaluation: Execution Time, Marginal Memory Usage, and CPU Overhead
def evaluate_performance(message, iterations=100):
    device = Signature("Dilithium5")  # Choose the post-quantum algorithm
    signing_times = []
    verification_times = []
    memory_usage_list = []
    cpu_usage_list = []

    # Generate a keypair once for all iterations
    public_key = device.generate_keypair()

    # Measure performance over multiple iterations
    for i in range(iterations):
        print(f"Iteration {i}:", "\n", "------------------", "\n")
        signature, signing_time, memory_usage, cpu_usage, _ = sign_message(device, message)
        is_valid, verification_time, memory_usage, cpu_usage = verify_signature(device, message, signature, public_key)

        signing_times.append(signing_time)
        verification_times.append(verification_time)
        memory_usage_list.append(memory_usage)
        cpu_usage_list.append(cpu_usage)

    avg_signing_time = sum(signing_times) / iterations
    avg_verification_time = sum(verification_times) / iterations
    avg_memory_usage = sum(memory_usage_list) / iterations
    avg_cpu_usage = sum(cpu_usage_list) / iterations

    print(f"Average signing time: {avg_signing_time:.10f} seconds")
    print(f"Average verification time: {avg_verification_time:.6f} seconds")
    print(f"Average memory usage (KB): {avg_memory_usage:.10f}")
    print(f"Average CPU Usage {avg_cpu_usage:.10f}%")


    return avg_signing_time, avg_verification_time, avg_memory_usage, avg_cpu_usage


# Security Evaluation: Test effectivness of Dilithium5 digital signatures against message spoofing and tampering
def test_security(device, message, signature, public_key):

    # Simulate spoofing: attempting to verify a different message with same signature
    spoof_message = "You have been spoofed!"
    is_valid_spoof = device.verify(spoof_message.encode('utf-8'), signature, public_key)
    print(f"Verification against spoofing: {'Passed' if not is_valid_spoof else 'Failed'}")

    # Simulate tampering: attempting to verify the original messsage with a modified signature
    tampered_signature = bytearray(signature)
    tampered_signature[0] = tampered_signature[0] ^ 0x01  # Flip the first byte (tamper with the signature)
    is_valid_tampered = device.verify(message.encode('utf-8'), bytes(tampered_signature), public_key)
    print(f"Verification against tampering: {'Passed' if not is_valid_tampered else 'Failed'}")

def main():

    message = "Hello from one IoT device to another."

    # Create the device object and simulate signing and verification actions
    device = Signature("Dilithium5")
    print("Simulating IoT device signing and verification...")
    signature, _, _, _, public_key = sign_message(device, message)
    print("Message Received.")
    is_valid, _, _, _, = verify_signature(device, message, signature, public_key)

    print(f"Signature valid: {is_valid}")

    print("\nEvaluating performance...")
    evaluate_performance(message)

    # Security validation: Test resistance against message spoofing and tampering
    print("\nValidating security...")
    test_security(device, message, signature, public_key)

if __name__ == "__main__":
    main()