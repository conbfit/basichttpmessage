import socket
import sys

def send_message(host,port,message):

    # create an ip socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to the server
        print(f"\n[*] connecting to {host}:{port}")
        client_socket.connect((host,port))
        print(f"\n[+] connected")

        # send the message
        print(f"\n[*] sending: {message}")
        client_socket.sendall(message.encode('utf-8'))

        # receive response
        response = client_socket.recv(1024)
        print(f"[Response] {response.decode('utf-8')}")

    except ConnectionRefusedError:
        print(f"\n[!] connection refused")
        sys.exit(1)
    except OSError as e:
        print(f"\n[!] network error: {e}")
        sys.exit(1)
    finally:
        client_socket.close()
        print("\n[*] connection closed")

if __name__ == "__main__":
    print(f"sys.argv={sys.argv}")
    if len(sys.argv) < 2:
        print("incorrect usage")
        sys.exit(1)

    message = sys.argv[1]
    host = sys.argv[2] if len(sys.argv)>2 else "localhost"
    port = int(sys.argv[3]) if len(sys.argv)>3 else 5555

    send_message(host,port, message)