import socket

HOST = 'localhost'
PORT = 9009

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((HOST, PORT))
    # sock.sendall(filename.encode())

def getFileFromServer(msg):
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # sock.sendall(filename.encode())

        if msg == '1':
            data = sock.recv(1024)
            print(data.decode())

        if msg == '2':
            choice = input("다운로드 받을 파일이름을 입력하세요: ")
            sock.send(choice.encode())

            data = sock.recv(1024)
            if not data:
                print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' % choice)
                return

            with open('D:/git/Python/client/' + choice, 'wb') as f:
                try:
                    while data:
                        f.write(data)
                        data_transferred += len(data)
                        data = sock.recv(1024)
                except Exception as e:
                    print(e)

            print('파일[%s] 전송종료. 전송량 [%d]' % (choice, data_transferred))



def runChat():
    print("""
**********************
1. 서버 파일 리스트 출력
2. 파일 다운받기
0. 끝내기""")
    msg = input('어떤 것을 하고 싶습니까?: ')
    # sock.send(msg.encode())
    if msg == '0':
        exit(0)

    if msg == '1' or '2':
        getFileFromServer(msg)

    # data = sock.recv(1024)
    # print(data)
while True:
    runChat()