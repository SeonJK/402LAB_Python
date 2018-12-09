import re

print("조건에 맞게 정보를 입력해주세요.")                                             #입력부분
#id = input("ID{영문시작, 6~20자, 특수문자X}: ")
#passwd = input("PASSWORD{대문자 1개이상, 숫자, 특수문자를 섞어서 10~20자}: ")
birth = input("BIRTHDAY{XXXX년 XX월 XX일}: ")
print("\n")

# idre = re.compile(r"^[a-z][a-z0-9]{4,18}[a-z0-9]$", re.I)                              #아이디 적합검사
# m1 = idre.search(str(id))
# idre = re.compile(r"[\W]*")
# m2 = idre.search(str(id))
#
# if m1 or not m2:                                                                        #영문으로 시작하고 글자수가 맞거나 특수문자가 없으면
#     pass
# else:
#     print("ID 조건에 맞게 입력하셔야 합니다!")
#     exit(0)
                                                                                          # 비밀번호 적합검사
#pwre = re.compile(r"^[A-Z](\w{9,19})$|^(\w{4,9})[A-Z](\w{5,10})$|^(\w{5,10})[A-Z](\w{4,9})$|^(\w{9,19})[A-Z]$")
# pwre = re.compile(r"(\w|\W){10,20}", re.I)
# m1 = pwre.search(str(passwd))
#
# # pwre = re.compile(r"[A-Z]")
# # m2 = pwre.search(str(passwd))
#
# if m1 and m2:                                                                                    #대문자가 하나들어가고 글자수가 맞으면
#     secure = re.compile(r"(\w|\W)")
#
# else:
#     print("PASSWORD 조건에 맞게 입력하셔야 합니다!")
#     exit(0)
                                                                                          #생일 적합검사
bthre = re.compile(r"(?P<year1>[0-9]{2})(?P<year2>[0-9]{2})[년]\s*(?P<month>[0-9]{1,2})[월]\s*(?P<day>[0-9]{1,2})[일]")
m1 = bthre.search(birth)

#if m1:                                                                                    #형식에 맞게 작성됐으면
#   bthre = re.compile(r"(년|월|일| )")                                                         #가공하기
#   m2 = bthre.sub("", str(m1))
# else:
#     print("BIRTHDAY 조건에 맞게 입력하셔야 합니다!")
#     exit(0)

# if m1.group("month")

#print("ID: ", id)
# print("PASSWORD: ", passwd)
# print("PASSWORD is secured: ", secure.sub("*", str(passwd)))                            #비밀번호 *로 암호화해서 출력
print("BIRTHDAY: ", m1.group(2,3))

