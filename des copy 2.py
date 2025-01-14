import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import copy
import telegraph
from config_charm import *
import config_chips
import config_jolyful 
import config
import config_velik
import requests
import json

def addToDB(name, url_new, url_old):
    pass
    """name = str(name)
    url_new = str(url_new)
    url_old = str(url_old)[0:-1]
    data_tuple = (name, url_new, url_old)
    con = sqlite3.connect('manga.sqlite')
    cur = con.cursor()
    sql_quary = """
    '''INSERT INTO manga_link
                          (name, link, original_link)
                          VALUES (?, ?, ?);'''
"""
    cur.execute(sql_quary, data_tuple)
    print('добавлено в бд')
    con.commit()
    con.close()"""

# Функция проверки ссылки на наличие в БД    
''' 
def chek_DB(url_old):
    con = sqlite3.connect('manga.sqlite')
    cur = con.cursor()
    url_old = str(url_old)[0:-1]
    cur.execute("SELECT link FROM manga_link WHERE original_link = ?", (url_old,))
    data=cur.fetchall()
    if len(data)==0:
        return True
    else:
        return False'''
    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 241, 22))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Charmed")
        self.comboBox.addItem("Molly Water")
        self.comboBox.addItem("Revelation")
        self.comboBox.addItem("joyful")
        self.comboBox.addItem("папич")
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(480, 30, 241, 22))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Telegraph")
        self.comboBox_2.addItem("MangaLib")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 20))
        self.label.setObjectName("label")
        self.label.setText("Выберите канал")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 201, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Выберите сайт")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 130, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 161, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Введите ссылки")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 300, 100))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 250, 461, 101))
        self.plainTextEdit_3.setObjectName("plainplainTextEdit_3")
        self.plainTextEdit_3.setReadOnly(True)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Окно информации")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Готовые ссылки")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 420, 471, 171))
        self.plainTextEdit_2.setObjectName("plainplainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 310, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Спарсить")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.get_links)
        self.site_name = str(self.comboBox_2.currentText())

    def get_links(self):
        self.links = self.textEdit.toPlainText().split()
        self.pars()

    def pars(self):
        self.chanel = str(self.comboBox.currentText())
        self.site = str(self.comboBox_2.currentText())
        with open('input.txt', 'w') as file:
            for link in self.links:
                file.write(link + '\n')

        if self.chanel == 'Charmed':
            prefix = PREFIX
            postfix = POSTFIX
            author_link = AUTHOR_LINK
            author_name = AUTHOR_NAME
        elif self.chanel == 'joyful':
            prefix = config_jolyful.PREFIX
            postfix = config_jolyful.POSTFIX
            author_link = config_jolyful.AUTHOR_LINK
            author_name = config_jolyful.AUTHOR_NAME
        elif self.chanel == 'Molly Water':
            prefix = config.PREFIX
            postfix = config.POSTFIX
            author_link = config.AUTHOR_LINK
            author_name = config.AUTHOR_NAME
        elif self.chanel == 'Revelation':
            prefix = config_chips.PREFIX
            postfix = config_chips.POSTFIX
            author_link = config_chips.AUTHOR_LINK
            author_name = config_chips.AUTHOR_NAME
        elif self.chanel == 'папич':
            prefix = config_velik.PREFIX
            postfix = config_velik.POSTFIX
            author_link = config_velik.AUTHOR_LINK
            author_name = config_velik.AUTHOR_NAME
        if self.site == 'Telegraph': 
            tg_channel_parse = ParseTG(self)
            print(tg_channel_parse.start(prefix, postfix, author_link, author_name))
        elif self.site == 'HentaiChan':
            HC_channel_parse = Hent(self)
            print(HC_channel_parse.start(prefix, postfix, author_link, author_name))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.setWindowTitle('Manga TG')
        
class HentaiChan:
    READER_URL = "https://xxxxx.hentaichan.live/online//"
    
    @staticmethod
    def get_slug(url):
        return url.split("/")[-1]

    def get_manga(self, url):
        url = self.READER_URL + self.get_slug(url)
        response = requests.get(url).text

        manga = {
            "title": response.split("<title>")[-1].split("</title>")[0].removesuffix("читать онлайн").strip(),
            "pictures": []
        }
        for pic in json.loads('{"values": ' + response.split('"thumbs": ')[-1].split('"fullimg": [')[0].strip()[:-1].replace("'", '"') + "}")['values']:
            manga['pictures'].append(pic.replace("_thumbs", ""))

        return manga
    
class Hent(HentaiChan, Ui_MainWindow):
    def __init__(self, ui):
            self.ui = ui

    def upload_photo(self, url):
        with open('pic.png', 'wb') as f:
            f.write(requests.get(url).content)

        with open('pic.png', 'rb') as f:
            pic = telegraph.upload.upload_file(f)[0]
            print(f"Uploaded picture https://telegra.ph/{pic}")
            curr_text = self.ui.plainTextEdit_3.toPlainText()
            self.ui.plainTextEdit_3.setPlainText(curr_text + '\n'  + f"ЗАГРУЖЕНО ИЗОБРАЖЕНИЕ - {pic}")
            return pic
    
    def start(self, prefix, postfix, author_link, author_name):
        client = telegraph.Telegraph(access_token=config.ACCESS_TOKEN)
        old_urls = [link for link in open("input.txt", "r").readlines() if link.strip()]
        for i, link in enumerate(old_urls):
            manga_object = HentaiChan().get_manga(link)
            print(f"Manga parsed ({manga_object['title']})")

            manga_template = [
                *prefix,
                *[{"tag": "img", "attrs": {"src": self.upload_photo(p)}} for p in manga_object['pictures'] if p.strip()],
                *postfix
            ]

            manga_link = client.create_page(
                manga_object['title'],
                manga_template,
                author_name=author_name,
                author_url=author_link,
            )['url']
            
            with open("output.txt", "a", encoding="utf-8") as f:
                    f.write(manga_link + "\n")

            print(manga_link)
            addToDB(manga_object['title'], manga_link, link)
            curr_text = self.ui.plainTextEdit_2.toPlainText()
            self.ui.plainTextEdit_2.setPlainText(curr_text + '\n'  + f"[{i + 1} of {len(old_urls)}] Page parsed - {manga_link}")
    
             

class Channel:
    def __init__(self, ui):
            self.ui = ui

    def upload_photo(self, path):
        with open(path, 'rb') as file:
            pic = telegraph.upload_file(file)[0]
            return pic

    def get_img(self, elements):
        for el in elements:
            if isinstance(el, dict):
                if el['tag'] == "img":
                    yield el
                elif el.get("children"):
                    for k in self.get_img(el['children']):
                        if k['tag'] == "img":
                            yield k

class ParseTG(Channel, Ui_MainWindow):
    def __init__(self, ui):
        super().__init__(ui)

    def start(self, prefix, postfix, author_link, author_name):
        client = telegraph.Telegraph(access_token=ACCESS_TOKEN)

        old_urls = [link for link in open("input.txt", "r").readlines() if link.strip()]
        target_pages = [link.strip().split("/")[-1] for link in open("input.txt", "r").readlines() if link.strip()]
        for i, page in enumerate(target_pages):
            try:
                if "|" in page:
                    page, alt_cover = page.split("|")
                else:
                    alt_cover = None
                page_data = client.get_page(page, return_html=False)

                # cover = None
                content = []
                for img in self.get_img(page_data['content']):
                    content.append(img)

                if alt_cover:
                    content[0]['attrs']['src'] = self.upload_photo(f"./previews/{alt_cover}")

                content = copy.deepcopy(prefix) + content
                content += copy.deepcopy(postfix)

                link = client.create_page(
                    page_data['title'],
                    content,
                    author_name= author_name,
                    author_url=author_link,
                )['url']
                with open("output.txt", "a", encoding="utf-8") as f:
                    f.write(link + "\n")

                curr_text = self.ui.plainTextEdit_2.toPlainText()
                self.ui.plainTextEdit_2.setPlainText(curr_text + '\n'  + f"[{i + 1} of {len(target_pages)}] Page parsed - {link}")
                addToDB(page_data['title'], link, old_urls[i])
            
            except telegraph.exceptions.TelegraphException:
                curr_text = self.ui.plainTextEdit_3.toPlainText()
                self.ui.plainTextEdit_3.setPlainText(curr_text + '\n'  + f"[{i + 1} of {len(target_pages)}] PAGE CAN'T PARSED! CHEK LINK - {old_urls[i]}")
                curr_text = self.ui.plainTextEdit_2.toPlainText()
                self.ui.plainTextEdit_2.setPlainText(curr_text + '\n'  + f"[{i + 1} of {len(target_pages)}] PAGE CAN'T PARSED! CHEK LINK - {old_urls[i]}")
                continue


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    ui = Ui_MainWindow
    channel = Channel(ui)
    hent = Hent(ui)
    w.show()
    sys.exit(app.exec_())