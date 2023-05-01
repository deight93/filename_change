import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QFileDialog, QComboBox
import os
from lib import common

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()

        # 윈도우 창 설정
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("File Explorer")

        # 레이아웃 생성
        layout = QVBoxLayout(self)

        # 파일 경로 라벨 생성
        self.label = QLabel("파일 경로:")
        layout.addWidget(self.label)

        # 파일 경로 입력 위젯 생성
        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        # 폴더 선택 버튼 생성
        self.select_folder_button = QPushButton("폴더 선택")
        layout.addWidget(self.select_folder_button)

        # 버튼 이벤트 연결
        self.select_folder_button.clicked.connect(self.open_folder_dialog)
        
        # 콤보박스 생성 및 아이템 추가
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("출근")
        self.combo_box.addItem("퇴근")
        layout.addWidget(self.combo_box)
        
        # 파일 목록 리스트 박스 생성
        self.file_listbox = QListWidget()
        layout.addWidget(self.file_listbox)

        # 목록 업데이트 버튼 생성
        self.button = QPushButton("목록 업데이트")
        layout.addWidget(self.button)

        # 버튼 이벤트 연결
        self.button.clicked.connect(self.update_file_list)

        self.show()

    def open_folder_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder_path = QFileDialog.getExistingDirectory(self, "폴더 선택", options=options)
        if folder_path:
            self.entry.setText(folder_path)
        
    def update_file_list(self):
        selected_data = self.combo_box.currentText()
        if selected_data == "출근":
            temp = 0
        else:
            temp = 1
        
        self.file_listbox.clear()
        path = self.entry.text()
        new_path = os.getcwd()+"/"+"result_images"
        if os.path.exists(path):
            common.change_name(path, new_path, temp)
            
            for file_name in os.listdir(path):
                self.file_listbox.addItem(file_name)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileExplorer()
    sys.exit(app.exec_())