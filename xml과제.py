# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString  # minidom 모듈의 파싱 함수를 임포트합니다.
from xml.etree import ElementTree


##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None


#### Menu  implementation
def printMenu():
    print("""
==모드를 선택해주세요.==
1. 연습하기
2. 파일불러오기
3. 종료
""")


def printSubMenu(menu):
    if menu == '1':
        print("""
==========Menu==========
|       0.모드선택      |
|       1.입력          |
|       2.출력          |
========================
""")
        Submenu = str(input("숫자를 입력해주세요 : "))
        launcherFunction1(Submenu)
    elif menu == '2':
        print("""
        ==========Menu==========
        |       0.모드선택      |
        |       1.불러오기      |
        |       2.입력          |
        |       3.출력          |
        |       4.검색          |
        |       5.종료          |
        ========================
        """)
        Submenu = str(input("숫자를 입력해주세요: "))
        launcherFunction2(Submenu)


def launcherFunction1(menu):
    global BooksDoc
    if menu == '0':
        return
    # elif menu == '1':
    #     BooksDoc = LoadXMLFromFile()
    # elif menu == '5':
    #     QuitBookMgr()
    elif menu == '2':
        PrintDOMtoXML()
    # elif menu == 'b':
    #     PrintBookList(["title", ])
    elif menu == '1':
        print("==========정보입력==========")
        sex = input("성별을 입력해주세요 : ")
        name = input("이름을 입력해주세요 : ")
        age = int(input("나이를 입력해주세요 : "))
        phoneNum = input("전화번호 입력해주세요 : ")
        print("===========================")

        ISBN = str(input('insert ISBN :'))
        title = str(input('insert Title :'))
        AddBook({'ISBN': ISBN, 'title': title})
    # elif menu == '4':
    #     keyword = str(input('input keyword to search :'))
    #     printBookList(SearchBookTitle(keyword))
    # elif menu == 'm':
    #     keyword = str(input('input keyword code to the html  :'))
    #     html = MakeHtmlDoc(SearchBookTitle(keyword))
    #     print("-----------------------")
    #     print(html)
    #     print("-----------------------")
    else:
        print("error : unknow menu key")


def launcherFunction2(menu):
    global BooksDoc
    if menu == '0':
        return
    elif menu == '1':
        BooksDoc = LoadXMLFromFile()
    elif menu == '5':
        QuitBookMgr()
    elif menu == '3':
        PrintDOMtoXML()
    # elif menu == 'b':
    #     PrintBookList(["title", ])
    elif menu == '2':
        ISBN = str(input('insert ISBN :'))
        title = str(input('insert Title :'))
        AddBook({'ISBN': ISBN, 'title': title})
    elif menu == '4':
        keyword = str(input('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    # elif menu == 'm':
    #     keyword = str(input('input keyword code to the html  :'))
    #     html = MakeHtmlDoc(SearchBookTitle(keyword))
    #     print("-----------------------")
    #     print(html)
    #     print("-----------------------")
    else:
        print("error : unknow menu key")


#### xml function implementation
def LoadXMLFromFile():
    fileName = str(input("please input file name to load :"))  # 읽어올 파일경로를 입력 받습니다.
    global xmlFD

    try:
        xmlFD = open(fileName)  # xml 문서를 open합니다.
    except IOError:
        print("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)  # XML 문서를 파싱합니다.
        except Exception:
            print("loading fail!!!")
        else:
            print("XML Document loading complete")
            return dom
    return None


def BooksFree():
    if checkDocument():
        BooksDoc.unlink()  # minidom 객체 해제합니다.


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()


def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())


def PrintBookList(tags):
    global BooksDoc
    if not checkDocument():  # DOM이 None인지 검사합니다.
        return None

    booklist = BooksDoc.childNodes
    book = booklist[0].childNodes
    for item in book:
        if item.nodeName == "book":  # 엘리먼트를 중 book인 것을 골라 냅니다.
            subitems = item.childNodes  # book에 들어 있는 노드들을 가져옵니다.
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=", atom.firstChild.nodeValue)  # 책 목록을 출력 합니다.


def indent(elem, level=0):
    i = "굈" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def AddBook(bookdata):
    global BooksDoc
    if not checkDocument():
        return None

    # Book 엘리먼트를 만듭니다.
    newBook = BooksDoc.createElement('book')
    newBook.setAttribute('ISBN', bookdata['ISBN'])
    # Title 엘리먼트를 만듭니다.
    titleEle = BooksDoc.createElement('title')
    # 텍스트 에릴먼트를 만듭니다.
    titleNode = BooksDoc.createTextNode(bookdata['title'])
    # 텍스트 노드와 Title 엘리먼트를 연결 시킵니다.
    try:
        titleEle.appendChild(titleNode)
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)
    # Title를 book 엘리먼트와 연결 시킵니다.
    try:
        newBook.appendChild(titleEle)
        booklist = BooksDoc.firstChild
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook)


def SearchBookTitle(keyword):
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None

    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # Book 엘리먼트 리스트를 가져 옵니다.
    bookElements = tree.getiterator("book")
    for item in bookElements:
        strTitle = item.find("title")
        if (strTitle.text.find(keyword) >= 0):
            retlist.append((item.attrib["ISBN"], strTitle.text))

    return retlist


def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    # DOM 개체를 생성합니다.
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # HTML 최상위 엘리먼트를 생성합니다.
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)
    # Body 엘리먼트 생성
    body = newdoc.createElement('body')
    for bookitem in BookList:
        # Bold 엘리먼트를 생성합니다.
        b = newdoc.createElement('b')
        # 텍스트 노드를 만듭니다.
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)
        body.appendChild(b)

    # <br> 부분을 생성합니다.
    br = newdoc.createElement('br')
    body.appendChild(br)
    # title 부분을 생성합니다.


    p = newdoc.createElement('p')
    # 텍스트 노드를 만듭니다.
    titleText = newdoc.createTextNode("Title:" + bookitem[1])
    p.appendChild(titleText)
    body.appendChild(p)
    body.appendChild(br)  # <br> 부분을 부모 에릴먼트에 추가합니다.

    # Body 엘리먼트를 최상위 엘리먼트에 추가시킵니다.
    top_element.appendChild(body)

    return newdoc.toxml()


def printBookList(blist):
    for res in blist:
        print(res)


def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('숫자를 입력해주세요 :'))
    printSubMenu(menuKey)
else:
    print("Thank you! Good Bye")