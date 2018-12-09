# -*- coding:utf-8 -*-
import random
import time

def game():                                                         #게임 함수
    answerTuple = ()                                                #초기값 설정
    numberTuple = ()
    count = 1

    print("\n게임을 시작합니다!(연속입력)")                            #게임 시작

    for i in range(1, 4):                                           #랜덤 값 생성
        answer = random.randint(1, 9)
        answerTuple = answerTuple + (answer,)
        if i == 3:                                                  #같은 숫자가 들어 있을 경우 다시 실행
            if answerTuple[0] == answerTuple[1] or answerTuple[0] == answerTuple[2] or answerTuple[1] == answerTuple[2]:
                answerTuple = ()
                continue

    while count < 10:                                               #숫자 맞추기
        strike, ball = 0, 0
        print("\n*****{0}번째 시도*****".format(count))
        print("서로 다른 숫자 3자리를 입력해주세요.(숫자 0은 제외)")
        i = 1
        while i <= 3:
            try:
                number = int(input("{0}번째 숫자: ".format(i)))
            except ValueError:                                       #예외처리
                print("1-9사이의 숫자를 입력해주세요.\n")
            else:
                if number < 1 or number > 9:
                    print("1-9사이의 숫자를 입력해주세요.\n")
                    continue
                numberTuple = numberTuple + (number,)
                i = i + 1

        if numberTuple[0] == numberTuple[1] or numberTuple[0] == numberTuple[2] or numberTuple[1] == numberTuple[2]:
            print("서로 다른 숫자를 입력해주세요.\n")                    #같은 값이 들어있을 경우 다시 실행
            continue

        for answer in range(0,3):                                     #스트라이크, 볼 판정
            for number in range(0,3):
                if answerTuple[answer] == numberTuple[number] and answer == number:
                    strike = strike + 1
                if answerTuple[answer] == numberTuple[number] and answer != number:
                    ball = ball + 1

        print("{0}개의 스트라이크!, {1}개의 볼".format(strike, ball))
        count = count + 1

        if strike == 3:                                               #3스트라이크일 경우
            print("""
 ------------
|  YOU WIN!! |
 ------------\n\n""")
        elif count == 10:                                             #10번을 시도했을 경우
            print("""
 ------------
|  YOU LOSE. |
 ------------\n\n""")

        if strike == 3 or count == 10:
            print(">>>>>>정답 공개<<<<<<\n")
            print("3초")
            time.sleep(1)
            print("2초")
            time.sleep(1)
            print("1초\n")
            time.sleep(1)

            print("{0} 입니다.".format(answerTuple))
            exit(0)

def end():                                                             #종료함수
    print("게임을 종료합니다!")
    exit(0)

while True:                                                            #메인 실행문
    print("""
---------------------야구 숫자게임--------------------
    
********메뉴********
  1. 게임 시작
  2. 게임 종료""")
    try:
        menu = int(input("번호를 입력해 주세요 = "))
    except ValueError:                                                 #예외 처리
        print("Error = 다시 입력해주세요! (1번 or 2번)")
    else:
        if menu == 1:
            game()
        elif menu == 2:
            end()
        else:
            print("Error = 다시 입력해주세요! (1번 or 2번)")
            continue