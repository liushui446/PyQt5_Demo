from PyQt5.QtWidgets import QMainWindow
from MainWindow import Ui_MainWindow  # 导入 uiDemo4.py 中的 Ui_MainWindow 界面类
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类

