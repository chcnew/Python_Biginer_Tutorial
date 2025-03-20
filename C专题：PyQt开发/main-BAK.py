import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QMessageBox, QDialog, QLineEdit, QHeaderView, QPushButton, QComboBox, QHBoxLayout, QLabel, QFileDialog, QFormLayout


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("正在进入...")
        self.setFixedSize(300, 150)

        layout = QFormLayout(self)
        self.username_input = QLineEdit(self)
        layout.addRow("VIVO工号:", self.username_input)

        # 登录按钮
        login_button = QPushButton("进入", self)
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

    def handle_login(self):
        username = self.username_input.text()
        if username.isdigit() \
                and len(username) == 8:
            self.accept()  # 登录成功，接受对话框
        else:
            QMessageBox.warning(self, "输入错误", "工号只能全为数字组成且长度为8，请重新输入！")


class UploadFileDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件上传")
        self.setFixedSize(500, 300)

        layout = QVBoxLayout(self)

        # 上半部分：浏览文件按钮和拖拽区域
        self.file_table = QTableWidget(0, 2)  # 文件路径和操作列
        self.file_table.setHorizontalHeaderLabels(["文件路径", "操作"])

        self.browse_button = QPushButton("浏览文件")
        self.browse_button.clicked.connect(self.browse_files)

        self.drag_area = QLabel("将文件拖拽到此区域上传")
        self.drag_area.setAlignment(Qt.AlignCenter)
        self.drag_area.setAutoFillBackground(True)
        self.drag_area.setStyleSheet("background-color: lightgray; border: 2px dashed black; padding: 20px;")

        self.drag_area.setAcceptDrops(True)
        self.drag_area.dragEnterEvent = self.dragEnterEvent
        self.drag_area.dropEvent = self.dropEvent

        browse_layout = QHBoxLayout()
        browse_layout.addWidget(self.browse_button)
        browse_layout.addWidget(self.drag_area)

        layout.addLayout(browse_layout)
        layout.addWidget(self.file_table)

        # 下半部分：取消与确认按钮
        buttons_layout = QHBoxLayout()

        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.reject)

        confirm_button = QPushButton("确认")
        confirm_button.clicked.connect(self.accept)

        buttons_layout.addWidget(cancel_button)
        buttons_layout.addWidget(confirm_button)

        layout.addLayout(buttons_layout)

    def browse_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "选择文件", "", "所有文件 (*)")
        for file_path in file_paths:
            self.add_file(file_path)

    def add_file(self, file_path):
        # 在表格中添加文件路径
        row_position = self.file_table.rowCount()
        self.file_table.insertRow(row_position)

        file_path_item = QTableWidgetItem(file_path)
        file_path_item.setToolTip(file_path)
        self.file_table.setItem(row_position, 0, file_path_item)

        delete_button = QPushButton("删除")
        delete_button.clicked.connect(lambda: self.delete_file(row_position))
        self.file_table.setCellWidget(row_position, 1, delete_button)

    def delete_file(self, row):
        # 删除指定行
        self.file_table.removeRow(row)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.add_file(file_path)
        event.acceptProposedAction()


class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.feedbackInput = None
        self.layout = None
        self.mainWidget = None

        self.setWindowTitle("Log自动化解析工具V2.4.3.0")
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        width = screen_geometry.width()
        height = screen_geometry.height()

        x = (width - 1200) // 2
        y = (height - 768) // 2

        self.setGeometry(x, y, 1200, 768)
        self.initUI()
        self.showTable("工模测试项报错")

    @staticmethod
    def get_data_list():
        # 模拟从数据库或外部来源获取数据
        return ["测试项A", "测试项B", "测试项C", "测试项D"]

    def initUI(self):
        self.createMenu()
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout(self.mainWidget)

    def createMenu(self):
        menubar = self.menuBar()

        menu = menubar.addMenu("菜单")
        menu.addAction("AT指令测试错误", lambda: self.showTable("AT指令测试错误"))
        menu.addAction("工模测试项报错", lambda: self.showTable("工模测试项报错"))
        menu.addAction("AT指令发送", lambda: self.showTable("AT指令发送"))

        operation = menubar.addMenu("操作")
        operation.addAction("连接手机558端口", lambda: self.showMessage("连接手机558端口"))
        operation.addAction("设置手机为MTP", lambda: self.showMessage("设置手机为MTP"))
        operation.addAction("Log自动化解析", lambda: self.showMessage("Log自动化解析"))

        about = menubar.addMenu("关于")
        about.addAction("提交优化建议", self.showFeedbackDialog)
        about.addAction("更新日志信息", lambda: self.showMessage("当前工具版本2.4.3.0"))

    def showTable(self, table_type):
        headers = {
            "工模测试项报错": ["工模测试项名称", "问题描述", "概率", "文件", "状态", "问题单链接", "点击创建问题单", "删除"]
        }

        example_data = {
            "工模测试项报错": [
                ["测试项1", "描述1", "低", "file3.jpg", "未解决", "链接3", "创建", "删除"]
            ]
        }

        if self.layout.count() > 0:
            for num in range(self.layout.count()):
                self.layout.itemAt(num).widget().deleteLater()

        table = QTableWidget(len(example_data[table_type]), len(headers[table_type]))
        table.setHorizontalHeaderLabels(headers[table_type])

        for row_index, row_data in enumerate(example_data[table_type]):
            for col_index, item in enumerate(row_data):
                display_text = item[:20]
                table.setItem(row_index, col_index, QTableWidgetItem(display_text))
                table.item(row_index, col_index).setTextAlignment(Qt.AlignCenter)
                table.item(row_index, col_index).setToolTip(item)

                # 如果是“工模测试项名称”列，设置下拉框
                if table_type == "工模测试项报错" and col_index == 0:
                    combo = QComboBox()
                    combo.setStyleSheet(""" 
                        QComboBox {
                            font-size: 14px;
                            padding: 5px;
                        }
                    """)  # 给下拉框添加样式
                    combo.addItems(self.get_data_list())  # 获取下拉框数据
                    table.setCellWidget(row_index, col_index, combo)

                if table_type == "工模测试项报错" and col_index == 3:
                    upload_button = QPushButton("上传文件")
                    upload_button.setStyleSheet("""
                                QPushButton {
                                    font-size: 14px;
                                }
                            """)
                    upload_button.clicked.connect(lambda row=row_index: self.upload_file(row))
                    table.setCellWidget(row_index, col_index, upload_button)

        # 禁用表头交互
        header = table.horizontalHeader()
        header.setSectionsClickable(False)
        header.setSectionsMovable(False)
        header.setStretchLastSection(True)

        for column in range(table.columnCount()):
            if column in [0, ]:
                header.resizeSection(column, 200)
            header.setSectionResizeMode(column, QHeaderView.Interactive)
            header.resizeSection(column, min(header.sectionSize(column), 200))

        table.setStyleSheet(""" 
            QTableWidget {
                border: 1px solid black;
                gridline-color: black;
                font-size: 14px;
                selection-background-color: #A0C4FF;
                selection-color: #000;
            }
            QHeaderView::section {
                background-color: #B3E5FC;
                color: black;
                font-weight: bold;
                padding: 10px;
                text-align: center;
            }
            QTableWidget::item {
                padding: 1px;
                text-align: center;
            }
        """)

        add_button = QPushButton("+ 新建")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 1px;
                font-size: 14px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        add_button.clicked.connect(self.addRow)

        self.layout.addWidget(add_button)
        self.layout.addWidget(table)

        table.itemChanged.connect(self.onItemChanged)

    def upload_file(self, row_index):
        upload_dialog = UploadFileDialog()
        if upload_dialog.exec_() == QDialog.Accepted:
            # 你可以在这里处理上传的文件逻辑，更新表格数据等
            print("上传文件已确认")

    def addRow(self):
        table = self.layout.itemAt(1).widget()
        if table is None:
            return

        row_count = table.rowCount()
        col_count = table.columnCount()
        table.insertRow(row_count)

        for col in range(col_count):
            display_text = ""
            item = QTableWidgetItem(display_text)
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(row_count, col, item)

        if table.horizontalHeaderItem(0).text() == "工模测试项名称" and table.columnCount() > 0:
            combo = QComboBox()
            combo.addItems(self.get_data_list())
            combo.setStyleSheet(""" 
                QComboBox {
                    font-size: 14px;
                    padding: 5px;
                }
            """)
            table.setCellWidget(row_count, 0, combo)

        upload_button = QPushButton("上传文件")
        upload_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
            }
        """)
        upload_button.clicked.connect(lambda row=row_count: self.upload_file(row))
        table.setCellWidget(row_count, 3, upload_button)

    def onItemChanged(self, item):
        table = self.layout.itemAt(1).widget()
        if table is None:
            return

        column = item.column()
        header = table.horizontalHeader()
        current_width = header.sectionSize(column)
        header.resizeSection(column, min(current_width, 200))
        item.setToolTip(item.text())

    def showMessage(self, message):
        QMessageBox.information(self, "信息", message)

    def showFeedbackDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("提优化意见")
        layout = QVBoxLayout(dialog)

        self.feedbackInput = QLineEdit()
        self.feedbackInput.setPlaceholderText("请输入您的意见...")
        layout.addWidget(self.feedbackInput)

        button = QPushButton("提交")
        layout.addWidget(button)

        button.clicked.connect(self.submitFeedback)
        dialog.exec_()

    def submitFeedback(self):
        feedback = self.feedbackInput.text()
        QMessageBox.information(self, "感谢", f"感谢您的反馈：\n{feedback}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        window = MainWindow(username=login_dialog.username_input.text())
        window.show()
    sys.exit(app.exec_())
