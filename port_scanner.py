import socket


def scan_port(target, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout so the program doesn't wait too long
        sock.settimeout(1)

        # Try to connect to the port
        result = sock.connect_ex((target, port))

        # Check connection result
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

        # Close the socket
        sock.close()

    except socket.gaierror:
        print("Error: Unable to find the target host.")

    except socket.error:
        print("Error: Could not connect to the target.")


# Get target from user
target = input("Enter target host (example: 127.0.0.1): ")

# Convert hostname to IP address
try:
    target_ip = socket.gethostbyname(target)
    print(f"\nScanning target: {target_ip}")
    print("-" * 30)

    # Scan ports 1 to 100
    for port in range(1, 101):
        scan_port(target_ip, port)

except socket.gaierror:
    print("Invalid hostname or IP address.")