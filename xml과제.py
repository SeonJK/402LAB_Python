# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString  # minidom ����� �Ľ� �Լ��� ����Ʈ�մϴ�.
from xml.etree import ElementTree


##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None


#### Menu  implementation
def printMenu():
    print("""
==��带 �������ּ���.==
1. �����ϱ�
2. ���Ϻҷ�����
3. ����
""")


def printSubMenu(menu):
    if menu == '1':
        print("""
==========Menu==========
|       0.��弱��      |
|       1.�Է�          |
|       2.���          |
========================
""")
        Submenu = str(input("���ڸ� �Է����ּ��� : "))
        launcherFunction1(Submenu)
    elif menu == '2':
        print("""
        ==========Menu==========
        |       0.��弱��      |
        |       1.�ҷ�����      |
        |       2.�Է�          |
        |       3.���          |
        |       4.�˻�          |
        |       5.����          |
        ========================
        """)
        Submenu = str(input("���ڸ� �Է����ּ���: "))
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
        print("==========�����Է�==========")
        sex = input("������ �Է����ּ��� : ")
        name = input("�̸��� �Է����ּ��� : ")
        age = int(input("���̸� �Է����ּ��� : "))
        phoneNum = input("��ȭ��ȣ �Է����ּ��� : ")
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
    fileName = str(input("please input file name to load :"))  # �о�� ���ϰ�θ� �Է� �޽��ϴ�.
    global xmlFD

    try:
        xmlFD = open(fileName)  # xml ������ open�մϴ�.
    except IOError:
        print("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)  # XML ������ �Ľ��մϴ�.
        except Exception:
            print("loading fail!!!")
        else:
            print("XML Document loading complete")
            return dom
    return None


def BooksFree():
    if checkDocument():
        BooksDoc.unlink()  # minidom ��ü �����մϴ�.


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()


def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())


def PrintBookList(tags):
    global BooksDoc
    if not checkDocument():  # DOM�� None���� �˻��մϴ�.
        return None

    booklist = BooksDoc.childNodes
    book = booklist[0].childNodes
    for item in book:
        if item.nodeName == "book":  # ������Ʈ�� �� book�� ���� ��� ���ϴ�.
            subitems = item.childNodes  # book�� ��� �ִ� ������ �����ɴϴ�.
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=", atom.firstChild.nodeValue)  # å ����� ��� �մϴ�.


def indent(elem, level=0):
    i = "�n" + level*"  "
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

    # Book ������Ʈ�� ����ϴ�.
    newBook = BooksDoc.createElement('book')
    newBook.setAttribute('ISBN', bookdata['ISBN'])
    # Title ������Ʈ�� ����ϴ�.
    titleEle = BooksDoc.createElement('title')
    # �ؽ�Ʈ ������Ʈ�� ����ϴ�.
    titleNode = BooksDoc.createTextNode(bookdata['title'])
    # �ؽ�Ʈ ���� Title ������Ʈ�� ���� ��ŵ�ϴ�.
    try:
        titleEle.appendChild(titleNode)
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)
    # Title�� book ������Ʈ�� ���� ��ŵ�ϴ�.
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

    # Book ������Ʈ ����Ʈ�� ���� �ɴϴ�.
    bookElements = tree.getiterator("book")
    for item in bookElements:
        strTitle = item.find("title")
        if (strTitle.text.find(keyword) >= 0):
            retlist.append((item.attrib["ISBN"], strTitle.text))

    return retlist


def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    # DOM ��ü�� �����մϴ�.
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # HTML �ֻ��� ������Ʈ�� �����մϴ�.
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)
    # Body ������Ʈ ����
    body = newdoc.createElement('body')
    for bookitem in BookList:
        # Bold ������Ʈ�� �����մϴ�.
        b = newdoc.createElement('b')
        # �ؽ�Ʈ ��带 ����ϴ�.
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)
        body.appendChild(b)

    # <br> �κ��� �����մϴ�.
    br = newdoc.createElement('br')
    body.appendChild(br)
    # title �κ��� �����մϴ�.


    p = newdoc.createElement('p')
    # �ؽ�Ʈ ��带 ����ϴ�.
    titleText = newdoc.createTextNode("Title:" + bookitem[1])
    p.appendChild(titleText)
    body.appendChild(p)
    body.appendChild(br)  # <br> �κ��� �θ� ������Ʈ�� �߰��մϴ�.

    # Body ������Ʈ�� �ֻ��� ������Ʈ�� �߰���ŵ�ϴ�.
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
    menuKey = str(input('���ڸ� �Է����ּ��� :'))
    printSubMenu(menuKey)
else:
    print("Thank you! Good Bye")