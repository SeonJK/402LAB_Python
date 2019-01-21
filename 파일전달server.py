import socketserver
from os.path import exists
from os import walk

HOST = ''
PORT = 9009


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('[%s] 연결됨' % self.client_address[0])

    def fileTransfer(self):
        choice = "다운로드 받을 파일이름을 입력하세요:"
        self.request.send(choice.encode())

        data_transferred = 0
        filename = self.request.recv(1024)  # 클라이언트로 부터 파일이름을 전달받음
        filename = filename.decode()  # 파일이름 이진 바이트 스트림 데이터를 일반 문자열로 변환

        if not exists(filename):  # 파일이 해당 디렉터리에 존재하지 않으면
            return  # handle()함수를 빠져 나온다.

        print('파일[%s] 전송 시작...' % filename)
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024)  # 파일을 1024바이트 읽음
                while data:  # 파일이 빈 문자열일때까지 반복
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)

        print('전송완료[%s], 전송량[%d]' % (filename, data_transferred))

    def dirPrint(self):
        path_dir = 'D:\git\Python\server'
        file_list = []

        # file_list = file_list.sort()

        for (path, dir, files) in walk(path_dir):
            for file in files:
                file_list.append(file)

        self.request.send(file_list)

    def msgHandler(self, username, msg): # 전송한 msg를 처리하는 부분

        # conn, addr = username
        msg = self.request.recv(1024)
        while msg:
            # if msg != '1' or '2 'or '0':  # 보낸 메세지의 첫문자가 약속된 숫자가 아니면
            #     msg = "0, 1, 2 중에 숫자를 선택해주세요."
            #     self.request.send(msg.encode())
            #     return

            if msg == '1':  # 보낸 메세지가 '1'이면
                self.dirPrint()
                return 1

            if msg == '2':  # 보낸 메세지가 '2'이면
                self.fileTransfer()
                return 2

            if msg == '0':  # 보낸 메세지가 '0'이면
                self.request.close()
                return -1


def runServer():
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")

    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++파일 서버를 종료합니다.++++++')
        server.shutdown()
        server.server_close()


runServer()