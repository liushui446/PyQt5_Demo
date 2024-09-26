import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from gui.MainWindow import Ui_MainWindow  # 导入 uiDemo4.py 中的 Ui_MainWindow 界面类
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer, pyqtSlot, Qt
from gui.GPSManager import GPSManager  # 假设你已经有了 GPSManager.py 文件
import folium

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类

        # 调用高德地图http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}
        Map = folium.Map(location=[34.2634, 109.0432],
                         zoom_start=16,
                         control_scale=True,
                         tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
                         attr='default')

        Map.add_child(folium.LatLngPopup())  # 显示鼠标点击点经纬度
        Map.add_child(folium.ClickForMarker(popup='Waypoint'))  # 将鼠标点击点添加到地图上

        # 标记一个实心圆
        folium.CircleMarker(
            location=[34.2634, 109.0432],
            radius=1,
            popup='popup',
            color='#DC143C',  # 圈的颜色
            fill=True,
            fill_color='#6495E'  # 填充颜色
        ).add_to(Map)
        Map.save("save_map.html")

        self.gpsManager = GPSManager()
        self.timer = QTimer(self)

        # Connect signals to slots
        self.gpsManager.gpsUpdated.connect(self.onGpsUpdated)
        self.gpsManager.routeDrawn.connect(self.onRouteDrawn)
        self.gpsManager.speedLimitReceived.connect(self.onSpeedLimitReceived)

        self.webEngineView = QWebEngineView(self)  # 创建 QWebEngineView 实例
        # self.webEngineView.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        # 设置网页在窗口中显示的位置和大小
        self.webEngineView.setGeometry(0, 0, 960, 600)
        # self.webEngineView.setUrl(QUrl("/qrc/map.html"))  # 设置 URL
        # self.Layout_map.addWidget(self.webEngineView)

        self.label_gps.setGeometry(1000, 100, 200, 100)
        self.label_speed.setGeometry(1000, 300, 200, 100)
        self.pushButton_draw.setGeometry(1000, 500, 200, 100)

        # 在QWebEngineView中加载网址
        path = "file:\\" + os.getcwd() + "\\save_map.html"
        path = path.replace('\\', '/')
        self.webEngineView.load(QUrl(path))


        # Setup timer
        self.timer.timeout.connect(self.onTimerTimeout)
        self.timer = QTimer(self)  # 创建定时器
        self.timer.setInterval(5000)  # 设置间隔为 5000 毫秒

        # Example of connecting a button's click event
        self.pushButton_draw.clicked.connect(self.on_pushButton_clicked)

    def onGpsUpdated(self, latitude, longitude):
        # 更新 GPS 位置的逻辑
        print(f"GPS Updated: Latitude = {latitude}, Longitude = {longitude}")

    def onRouteDrawn(self):
        # 处理路线绘制完成的逻辑
        print("Route has been drawn.")

    def onSpeedLimitReceived(self, limit):
        # 处理接收到的限速信息
        print(f"Speed limit received: {limit} km/h")

    def on_pushButton_clicked(self):
        # 处理按钮点击事件
        print("Button clicked!")

    def onTimerTimeout(self):
        # 定时器超时处理逻辑
        print("Timer timeout!")
