# Socket Client
import socket

class socket_client():
    def __init__(self, host_ip, port) -> None:
        self.host_ip = host_ip
        self.port = port

    def send_msg(self, msg:str)->None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host_ip, self.port))
            s.sendall(msg.encode())

    def wait_msg(self)->str:
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.host_ip, self.port))
                    data = s.recv(1024)
                    if data:
                        return data.decode()
                    else:
                        continue
            except:
                continue

def start_socket_client():
    HOST = '140.112.14.225'  # 伺服器的 IP 地址
    PORT = 12345        # 伺服器的端口號

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = "我不太游泳，要的話會在游泳池"
        s.sendall(message.encode())

        data = s.recv(1024)
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    client = socket_client('140.112.14.225', 2468)
    text = '佳勳' + '@@' + "我午餐吃了水餃"
    client.send_msg(text)
    print("wait for msg")
    r = client.wait_msg()
    print(r)
