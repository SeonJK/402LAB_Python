import sys
import pickle
import datetime

class  dict_source:
    def __init__(self):
        self.date = ''
        self.menu = ''
        self.price = ''

    def __set__(self, date, menu, price):
        self.date = date
        self.menu = menu
        self.price = price

dict = {}
while True:
    try:
       with open('가계부.txt', 'rb') as f:
           data = pickle.load(f)
           dict.update(data)
    except EOFError:
        pass
    except FileNotFoundError:
        print("***파일이 존재하지 않습니다.***\n")
        key = input("가계부.txt를 [1]생성하시겠습니까? [2]종료하시겠습니까? : ")
        if key == '1':
            f = open('가계부.txt', 'w')
            dict = {1: ['날짜', '내역', '비용']}
        elif key == '2':
            sys.exit()
        else:
            print("제대로 된 값을 입력해주세요.")
            sys.exit()
    else:
        f = open('가계부.txt', 'a')
        f.close()
    s = dict_source()
    s.__init__()
    print("\nQT를 입력하면 프로그램이 종료됩니다.")
    date = input("날짜, 시각을 입력해주세요(미입력시 현재시각 기입됩니다.) : ")
    if date == "QT" :
        with open('가계부.txt', 'wb') as f:
            pickle.dump(dict, f)
        for i in range(1,20):
            if i in dict:
                print(dict.get(i))
            else:
                break
        sys.exit()
    elif date is '':
        now = datetime.datetime.now()
        date = now.strftime('%Y.%m.%d.%A.%H:%M:%S')
    else:
        pass
    menu = input("내역을 입력해주세요 : ")
    price = input("비용을 입력해주세요 : ")
    print("\n")
    s.__set__(date, menu, price)
    for i in range(1, 20):
        if i in dict:
            pass
        else:
            dict[i] = [s.date, s.menu, s.price]
            break