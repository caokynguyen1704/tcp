import socket

# Địa chỉ IP và cổng của server
SERVER_HOST = '127.0.0.1'  # Địa chỉ IP loopback của server
SERVER_PORT = 12345

# Tên tệp cần gửi
file_name = 'sample.txt'

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"Đã kết nối đến {SERVER_HOST}:{SERVER_PORT}")

# Gửi tên tệp đến server
client_socket.send(file_name.encode())
print(f"Đã gửi tên tệp {file_name} đến server...")

# Mở tệp để đọc và gửi dữ liệu đến server
with open(file_name, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)

print(f"Tệp {file_name} đã được gửi thành công")

# Đóng kết nối
client_socket.close()
