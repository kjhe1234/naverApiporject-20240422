import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from naverSearchApi import *

form_class = uic.loadUiType("ui/search.ui")[0]  # 외부에서 ui 불러오기  내부에서 불러오면 1

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("네이버 뉴스 검색 앱")
        self.setWindowIcon(QIcon("img/newspaper.png"))
        self.statusBar().showMessage("Naver News Search Application v1.0")

        self.search_btn.clicked.connect(self.searchbtn_clicked)

    def searchbtn_clicked(self):
        search = self.search_line.text()  # 사용자가 입력한 검색 키워드 가져오기

        if search == "":
            QMessageBox.warning(self, "입력오류!", "검색어는 피수 입력 사항입니다.")
        else:
            naverApi = NaverApi()  # import 된 naverSearchApi 내의 NaverApi 클래스로 객체 생성
            searchResult = naverApi.getNaverSearch("news", search,1,50)
            #print(searchResult)
            newsResult = searchResult['items']
            self.outputTable(newsResult)

    def outputTable(self, newsResult):  # 뉴스검색결과를 테이블위젯에 출력하는 함수
        self.result_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.result_table.setColumnCount(3)  # 출력되는 테이블을 3열로 설정
        self.result_table.setRowCount(len(newsResult)) # 출력되는 테이블의 행 갯수 설정
        # newsResult 내의 원소 갯수 만큼 줄 갯수를 설정

        # 테이블의 첫 행(열 이름) 설정
        self.result_table.setHorizontalHeaderLabels(["기사제목","기사링크","게시시간"])
        # 각 칼럼의 넓이 지정(총 길이 790을 3등분)
        self.result_table.setColumnWidth(0, 400)
        self.result_table.setColumnWidth(1, 240)
        self.result_table.setColumnWidth(2, 100)
        # 테이블에 출력되는 검색결과 수정 금지 기능 추가
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)









app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())



