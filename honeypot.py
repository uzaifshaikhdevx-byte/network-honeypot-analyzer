import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222
LOG_FILE = "attacks.log"

def record_attack(ip, username, password):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {ip} | User: {username} | Pass: {password}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def run_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print("=" * 50)
        print(f"[*] Decoy Honeypot active on port {PORT}")
        print("[*] Waiting for incoming connections...")
        print("=" * 50)

        while True:
            client, addr = server.accept()
            attacker_ip = addr[0]
            print(f"\n[!] Unauthorized connection detected from: {attacker_ip}")

            try:
                client.send(b"Ubuntu 22.04 LTS - Internal Gateway\r\nLogin: ")
                username = client.recv(1024).decode('utf-8', errors='ignore').strip()

                client.send(b"Password: ")
                password = client.recv(1024).decode('utf-8', errors='ignore').strip()

                client.send(b"\r\nAuthentication Failed. Access Denied.\r\n")
                client.close()

                print(f"    └── Captured: User='{username}' | Pass='{password}'")
                record_attack(attacker_ip, username, password)

            except Exception as e:
                print(f"[-] Connection error: {e}")
                client.close()

    except KeyboardInterrupt:
        print("\n[*] Shutting down honeypot listener.")
    finally:
        server.close()

if __name__ == "__main__":
    run_honeypot()
