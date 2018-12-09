# -*- coding: utf-8 -*-
import time, datetime

while True:
    now = datetime.datetime.today()
    print("어떤 것을 기준으로 하시겠습니까?")
    choice = input("1.타임스탬프 2.년도 3.월 4.일 5.주(week): ")

    if choice == '1':
        try:
            stamp = int(input("타임스탬프 값을 입력해주세요: "))
        except ValueError:
             print("숫자를 입력해주세요.")
             exit(0)

        td = datetime.timedelta(seconds=int(stamp))
        addDate = now + td
        subDate = addDate - now
        print("{0}년 {1}월 {2}일 {3}:{4}:{5}".format(addDate.year, addDate.month, addDate.day, addDate.hour, addDate.minute, addDate.second))
        print("{0}년 {1}월 {2}일까지 {3}일 남았습니다.".format(addDate.year, addDate.month, addDate.day, subDate.days))
        print("\n\n")

    elif choice == '2':
        try:
            Year = int(input("년도를 입력해주세요: "))
        except ValueError:
             print("숫자를 입력해주세요.")
             exit(0)

        Year = Year * 365
        td = datetime.timedelta(days=int(Year))
        addDate = now + td
        subDate = addDate - now
        print(
            "{0}년 {1}월 {2}일 {3}:{4}:{5}".format(addDate.year, addDate.month, addDate.day, addDate.hour, addDate.minute,
                                                addDate.second))
        print("{0}년 {1}월 {2}일까지 {3}일 남았습니다.".format(addDate.year, addDate.month, addDate.day, subDate.days))
        print("\n\n")

    elif choice == '3':
        try:
            Month = int(input("월을 입력해주세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            exit(0)

        Month = Month * 30
        td = datetime.timedelta(days=int(Month))
        addDate = now + td
        subDate = addDate - now
        print(
            "{0}년 {1}월 {2}일 {3}:{4}:{5}".format(addDate.year, addDate.month, addDate.day, addDate.hour, addDate.minute,
                                                addDate.second))
        print("{0}년 {1}월 {2}일까지 {3}일 남았습니다.".format(addDate.year, addDate.month, addDate.day, subDate.days))
        print("\n\n")

    elif choice == '4':
        try:
            Day = int(input("일을 입력해주세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            exit(0)

        td = datetime.timedelta(days=int(Day))
        addDate = now + td
        subDate = addDate - now
        print(
            "{0}년 {1}월 {2}일 {3}:{4}:{5}".format(addDate.year, addDate.month, addDate.day, addDate.hour, addDate.minute,
                                                addDate.second))
        print("{0}년 {1}월 {2}일까지 {3}일 남았습니다.".format(addDate.year, addDate.month, addDate.day, subDate.days))
        print("\n\n")

    elif choice == '5':
        try:
            Week = int(input("주(week)를 입력해주세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            exit(0)

        td = datetime.timedelta(weeks=int(Week))
        addDate = now + td
        subDate = addDate - now
        print(
            "{0}년 {1}월 {2}일 {3}:{4}:{5}".format(addDate.year, addDate.month, addDate.day, addDate.hour, addDate.minute,
                                                addDate.second))
        print("{0}년 {1}월 {2}일까지 {3}일 남았습니다.".format(addDate.year, addDate.month, addDate.day, subDate.days))
        print("\n\n")