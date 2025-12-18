import socket
import sys

def start_server(host='0.0.0.0',port=5555):

    #create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # allow address reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind socket to port
    try:
        server_socket.bind((host, port))
        print(f"[*] server bound to {host}:{port}")
    except OSError as e:
        print(f"[!] failed to bind to {host}:{port}: {e}")
        sys.exit(1)

    server_socket.listen(5)
    print(f"Listening for incoming connections")

    try:
        while True:
            #accept connection
            client_socket, client_address = server_socket.accept()
            print(f"\n[+] connection from {client_address[0]}:{client_address[1]}")

            #receive data
            data = client_socket.recv(1024)

            if data:
                message = data.decode('utf-8')
                print(f"[Message] {message}")
            else:
                print("[*] disconnected with no data sent")

            response = "Message received!\n"
            client_socket.sendall(response.encode('utf-8'))

            #close server
            client_socket.close()

    except KeyboardInterrupt:
        print("\n[*] closing server")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()