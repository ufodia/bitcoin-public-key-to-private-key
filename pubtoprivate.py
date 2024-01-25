import argparse
from ecdsa import SECP256k1, VerifyingKey
import random
import time

def subtract_g_times_from_pubkey(pubkey_hex, times):
    curve = SECP256k1.curve
    g = SECP256k1.generator

    # Convert the public key from hex format to a point on the curve
    pubkey = VerifyingKey.from_string(bytes.fromhex(pubkey_hex), curve=SECP256k1).pubkey.point

    # Subtract 'g * times' from the public key
    result_point = pubkey + (-g * times)

    return result_point

# Argument parser setup
parser = argparse.ArgumentParser(description='Subtract G point from a Public Key.')
parser.add_argument('-pb', '--pubkey', type=str, help='Public Key (in hex format)', required=True)
parser.add_argument('-b', '--bit', type=int, help='Bit range', required=True)

args = parser.parse_args()

# Initialize variables based on arguments
bit = args.bit
min_times = 2**(bit - 1)
max_times = 2**bit - 1
pubkey_hex = args.pubkey

start_time = time.time()
total_attempts = 0

# Main loop
while True:
    times = random.randint(min_times, max_times)
    new_point = subtract_g_times_from_pubkey(pubkey_hex, times)
    total_attempts += 1

    # Calculate elapsed time and attempts per second
    elapsed_time = time.time() - start_time
    attempts_per_second = total_attempts / elapsed_time if elapsed_time > 0 else 0

    # Output progress
    print(f"\rTotal Attempts: {total_attempts}, Elapsed Time: {elapsed_time:.2f} seconds, Attempts per Second: {attempts_per_second:.2f} keys/s", end='')

    # Check if a valid point is found
    if new_point.x() is None or new_point.y() is None:
        print(f"\nPrivate Key Decimal: {times}. Public Key Hex: ({pubkey_hex})")
        with open("found.txt", "a") as file:
            file.write(f"Private Key Decimal: {times}, Public Key Hex: ({pubkey_hex})\n")
        break
