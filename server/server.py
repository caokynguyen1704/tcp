import socket

# Địa chỉ IP và cổng của server
HOST = '127.0.0.1'  # Địa chỉ IP loopback
PORT = 12345

# Khởi tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liên kết socket với địa chỉ IP và cổng
server_socket.bind((HOST, PORT))

# Lắng nghe kết nối đến socket
server_socket.listen()

print(f"Server đang lắng nghe trên {HOST}:{PORT}...")

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()
print(f"Đã kết nối với {client_address}")

# Nhận tên tệp từ client
file_name = client_socket.recv(1024).decode()
print(f"Đang nhận tệp {file_name}...")

# Nhận dữ liệu từ client và lưu vào tệp
with open(file_name, 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)

print(f"Tệp {file_name} đã được nhận thành công")

# Đóng kết nối
client_socket.close()
server_socket.close()
