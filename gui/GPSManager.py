from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QObject, pyqtSignal
import random


class GPSManager(QObject):
    routeDrawn = pyqtSignal()
    speedLimitReceived = pyqtSignal(int)
    gpsUpdated = pyqtSignal(float, float)

    def __init__(self, parent=None):
        super(GPSManager, self).__init__(parent)
        self.currentLatitude = 0.0
        self.currentLongitude = 0.0

    def drawRoute(self, webPage : QWebEnginePage):
        # 在这里触发在 HTML 页面中编写的 JavaScript 代码来绘制路线
        javascript_code = f"drawNewPoint({self.currentLatitude}, {self.currentLongitude});"

        if webPage:
            # 执行 JavaScript 代码
            webPage.runJavaScript(javascript_code)
            print(javascript_code)  # 替代 qDebug 输出

        # 获取限速信息并触发信号
        speed_limit = self.getSpeedLimit(self.currentLatitude, self.currentLongitude)
        self.speedLimitReceived.emit(speed_limit)

        # 触发路线绘制完成的信号
        self.routeDrawn.emit()

    def setGPSLocation(self, latitude, longitude):
        self.currentLatitude = latitude
        self.currentLongitude = longitude
        self.gpsUpdated.emit(latitude, longitude)
        print("setGPSLocation")

    def getSpeedLimit(self, latitude, longitude):
        # 在这里查询限速信息，这是一个示例
        # 实际上，你需要与地图数据提供商的API进行交互来获取限速信息

        # 模拟返回一个随机的限速值
        random_speed_limit = random.randint(30, 109)  # 生成30到109之间的随机整数
        return random_speed_limit