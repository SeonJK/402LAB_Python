import os
while True:
    print("""
--------------------파일탐색--------------------
1. 전체파일 탐색
2. 확장자에 맞게 탐색
0. 종료
""")
    num = int(input("번호를 선택하세요: "))
    if num == 0:
        print("\n파일탐색을 종료합니다.")
        exit(0)

    findPath = input("탐색할 경로를 입력하세요: ")

    if not os.path.exists(findPath):                                    #예외발생
        print("예외 발생!! 존재하지 않는 경로입니다.")

    elif num == 1:                                                      #전체
        if os.path.isdir(findPath):
            for (path, dir, files) in os.walk(findPath):
                for filename in files:
                    full_filename = os.path.join(path, filename)
                    print("탐색파일의 절대경로: {}".format(full_filename))

        if os.path.isfile(findPath):
            print("탐색파일의 절대경로: {}".format(findPath))

    elif num == 2:                                                      #확장자에 맞도록
        findExt = input("확장자를 입력해주세요[예) .exe, .txt 등등]: ")
        if os.path.isdir(findPath):
            for (path, dir, files) in os.walk(findPath):
                for filename in files:
                    ext = os.path.splitext(filename)[-1]
                    if findExt == ext:
                        full_filename = os.path.join(path, filename)
                        print(findExt + "파일: " + full_filename)

        if os.path.isfile(findPath):
            print(findExt + "파일: " + findPath)