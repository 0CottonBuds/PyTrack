# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 10))
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName(u"window_layout")
        self.header_container = QFrame(self.centralwidget)
        self.header_container.setObjectName(u"header_container")
        self.header_container.setMinimumSize(QSize(0, 32))
        self.header_container.setMaximumSize(QSize(16777215, 24))
        self.header_container.setFrameShape(QFrame.NoFrame)
        self.header_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.header_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header_container)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setMinimumSize(QSize(10, 10))
        self.header_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.header_left.setFrameShape(QFrame.NoFrame)
        self.header_left.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.header_left)

        self.header_center = QFrame(self.header_container)
        self.header_center.setObjectName(u"header_center")
        self.header_center.setMinimumSize(QSize(160, 0))
        self.header_center.setFrameShape(QFrame.NoFrame)
        self.header_center.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.header_center)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.header_center)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setStyleSheet(u"font: 90 16pt \"Times New Roman\";")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.header_center)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(24, 24))
        self.label_4.setMaximumSize(QSize(24, 24))
        self.label_4.setPixmap(QPixmap(u":/logo/logo/logo small v2.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.header_center)

        self.header_right = QFrame(self.header_container)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.NoFrame)
        self.header_right.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.header_right)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_right)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.frame)

        self.button_minimize = QPushButton(self.header_right)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setStyleSheet(u"border-radius : 50")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon)
        self.button_minimize.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_minimize)

        self.button_maximize = QPushButton(self.header_right)
        self.button_maximize.setObjectName(u"button_maximize")
        self.button_maximize.setStyleSheet(u"border-radius : 50")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_maximize.setIcon(icon1)
        self.button_maximize.setCheckable(True)
        self.button_maximize.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_maximize)

        self.button_exit = QPushButton(self.header_right)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setStyleSheet(u"border-radius : 50")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon2)
        self.button_exit.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_exit)


        self.horizontalLayout_4.addWidget(self.header_right)


        self.window_layout.addWidget(self.header_container)

        self.body_container = QFrame(self.centralwidget)
        self.body_container.setObjectName(u"body_container")
        self.body_container.setFrameShape(QFrame.NoFrame)
        self.body_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.body_container)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_container = QFrame(self.body_container)
        self.sidebar_container.setObjectName(u"sidebar_container")
        self.sidebar_container.setMinimumSize(QSize(56, 0))
        self.sidebar_container.setMaximumSize(QSize(56, 16777215))
        self.sidebar_container.setFrameShape(QFrame.NoFrame)
        self.sidebar_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.sidebar_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebaar_button_container = QFrame(self.sidebar_container)
        self.sidebaar_button_container.setObjectName(u"sidebaar_button_container")
        self.sidebaar_button_container.setFrameShape(QFrame.NoFrame)
        self.sidebaar_button_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.sidebaar_button_container)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 48, 0, 0)
        self.button_go_to_home = QPushButton(self.sidebaar_button_container)
        self.button_go_to_home.setObjectName(u"button_go_to_home")
        self.button_go_to_home.setMinimumSize(QSize(0, 56))
        self.button_go_to_home.setStyleSheet(u"border-radius : 50")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/homeX64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_home.setIcon(icon3)
        self.button_go_to_home.setIconSize(QSize(24, 24))
        self.button_go_to_home.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_home)

        self.button_go_to_analytics = QPushButton(self.sidebaar_button_container)
        self.button_go_to_analytics.setObjectName(u"button_go_to_analytics")
        self.button_go_to_analytics.setMinimumSize(QSize(0, 56))
        self.button_go_to_analytics.setStyleSheet(u"border-radius : 50")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/chart-histogram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_analytics.setIcon(icon4)
        self.button_go_to_analytics.setIconSize(QSize(24, 24))
        self.button_go_to_analytics.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_analytics)

        self.button_go_to_settings = QPushButton(self.sidebaar_button_container)
        self.button_go_to_settings.setObjectName(u"button_go_to_settings")
        self.button_go_to_settings.setMinimumSize(QSize(0, 56))
        self.button_go_to_settings.setStyleSheet(u"border-radius : 50")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_settings.setIcon(icon5)
        self.button_go_to_settings.setIconSize(QSize(24, 24))
        self.button_go_to_settings.setAutoDefault(False)
        self.button_go_to_settings.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_settings)

        self.frame_2 = QFrame(self.sidebaar_button_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.sidebaar_button_container)

        self.sidebar_footer = QFrame(self.sidebar_container)
        self.sidebar_footer.setObjectName(u"sidebar_footer")
        self.sidebar_footer.setFrameShape(QFrame.NoFrame)
        self.sidebar_footer.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.sidebar_footer)


        self.horizontalLayout_2.addWidget(self.sidebar_container)

        self.body_container_2 = QFrame(self.body_container)
        self.body_container_2.setObjectName(u"body_container_2")
        self.body_container_2.setFrameShape(QFrame.NoFrame)
        self.body_container_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.body_container_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.body_container_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_3 = QVBoxLayout(self.page_home)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_home_header = QFrame(self.page_home)
        self.page_home_header.setObjectName(u"page_home_header")
        self.page_home_header.setMaximumSize(QSize(16777215, 125))
        self.page_home_header.setFrameShape(QFrame.NoFrame)
        self.page_home_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.page_home_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.page_home_header_left = QFrame(self.page_home_header)
        self.page_home_header_left.setObjectName(u"page_home_header_left")
        self.page_home_header_left.setFrameShape(QFrame.NoFrame)
        self.page_home_header_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.page_home_header_left)

        self.page_home_header_center = QFrame(self.page_home_header)
        self.page_home_header_center.setObjectName(u"page_home_header_center")
        self.page_home_header_center.setMinimumSize(QSize(0, 100))
        self.page_home_header_center.setFrameShape(QFrame.NoFrame)
        self.page_home_header_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.page_home_header_center)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.page_home_header_center)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Lucida Calligraphy"])
        font.setPointSize(28)
        self.label_5.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.page_home_header_center)

        self.page_home_header_right = QFrame(self.page_home_header)
        self.page_home_header_right.setObjectName(u"page_home_header_right")
        self.page_home_header_right.setFrameShape(QFrame.NoFrame)
        self.page_home_header_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.page_home_header_right)


        self.verticalLayout_3.addWidget(self.page_home_header)

        self.page_home_body = QFrame(self.page_home)
        self.page_home_body.setObjectName(u"page_home_body")
        self.page_home_body.setMinimumSize(QSize(0, 300))
        self.page_home_body.setFrameShape(QFrame.NoFrame)
        self.page_home_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.page_home_body)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.page_home_body_left = QFrame(self.page_home_body)
        self.page_home_body_left.setObjectName(u"page_home_body_left")
        self.page_home_body_left.setFrameShape(QFrame.NoFrame)
        self.page_home_body_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.page_home_body_left)

        self.page_home_body_center = QFrame(self.page_home_body)
        self.page_home_body_center.setObjectName(u"page_home_body_center")
        sizePolicy.setHeightForWidth(self.page_home_body_center.sizePolicy().hasHeightForWidth())
        self.page_home_body_center.setSizePolicy(sizePolicy)
        self.page_home_body_center.setFrameShape(QFrame.NoFrame)
        self.page_home_body_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.page_home_body_center)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.page_home_body_center)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(u":/logo/logo/logo v1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.page_home_body_center)

        self.page_home_body_right = QFrame(self.page_home_body)
        self.page_home_body_right.setObjectName(u"page_home_body_right")
        self.page_home_body_right.setFrameShape(QFrame.NoFrame)
        self.page_home_body_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.page_home_body_right)


        self.verticalLayout_3.addWidget(self.page_home_body)

        self.page_home_footer = QFrame(self.page_home)
        self.page_home_footer.setObjectName(u"page_home_footer")
        self.page_home_footer.setFrameShape(QFrame.NoFrame)
        self.page_home_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.page_home_footer)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.page_home_footer_left = QFrame(self.page_home_footer)
        self.page_home_footer_left.setObjectName(u"page_home_footer_left")
        self.page_home_footer_left.setFrameShape(QFrame.NoFrame)
        self.page_home_footer_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.page_home_footer_left)

        self.page_home_footer_center = QFrame(self.page_home_footer)
        self.page_home_footer_center.setObjectName(u"page_home_footer_center")
        self.page_home_footer_center.setFrameShape(QFrame.NoFrame)
        self.page_home_footer_center.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.page_home_footer_center)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 20, 151, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"border-color: rgb(43, 43, 43);\n"
"border-radius : 50")
        self.pushButton.setFlat(False)

        self.horizontalLayout_10.addWidget(self.page_home_footer_center)

        self.page_home_footerright = QFrame(self.page_home_footer)
        self.page_home_footerright.setObjectName(u"page_home_footerright")
        self.page_home_footerright.setFrameShape(QFrame.NoFrame)
        self.page_home_footerright.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.page_home_footerright)


        self.verticalLayout_3.addWidget(self.page_home_footer)

        self.stackedWidget.addWidget(self.page_home)
        self.page_analytics = QWidget()
        self.page_analytics.setObjectName(u"page_analytics")
        self.horizontalLayout_12 = QHBoxLayout(self.page_analytics)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_3 = QFrame(self.page_analytics)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 20, 47, 13))

        self.horizontalLayout_12.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_analytics)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_analytics)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_13 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.page_settings_pages_container = QFrame(self.page_settings)
        self.page_settings_pages_container.setObjectName(u"page_settings_pages_container")
        self.page_settings_pages_container.setMinimumSize(QSize(260, 0))
        self.page_settings_pages_container.setMaximumSize(QSize(260, 16777215))
        self.page_settings_pages_container.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.page_settings_pages_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.page_settings_pages_container_top = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_top.setObjectName(u"page_settings_pages_container_top")
        self.page_settings_pages_container_top.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.page_settings_pages_container_top)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_settings_general = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_general.setObjectName(u"button_settings_general")
        self.button_settings_general.setMinimumSize(QSize(160, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.button_settings_general.setFont(font2)
        self.button_settings_general.setStyleSheet(u"border-radius : 50")
        self.button_settings_general.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_general, 0, Qt.AlignLeft)

        self.button_settings_window = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_window.setObjectName(u"button_settings_window")
        self.button_settings_window.setEnabled(True)
        self.button_settings_window.setMinimumSize(QSize(160, 40))
        self.button_settings_window.setFont(font2)
        self.button_settings_window.setStyleSheet(u"border-radius : 50")
        self.button_settings_window.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_window, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.page_settings_pages_container_top)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_5)

        self.button_settings_about = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_about.setObjectName(u"button_settings_about")
        self.button_settings_about.setMinimumSize(QSize(160, 40))
        self.button_settings_about.setFont(font2)
        self.button_settings_about.setStyleSheet(u"border-radius : 50")
        self.button_settings_about.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_about, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.page_settings_pages_container_top)

        self.page_settings_pages_container_center = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_center.setObjectName(u"page_settings_pages_container_center")
        self.page_settings_pages_container_center.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_center.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_center)

        self.page_settings_pages_container_bot = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_bot.setObjectName(u"page_settings_pages_container_bot")
        self.page_settings_pages_container_bot.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_bot.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_bot)


        self.horizontalLayout_13.addWidget(self.page_settings_pages_container)

        self.page_settings_stacked_widget_container = QFrame(self.page_settings)
        self.page_settings_stacked_widget_container.setObjectName(u"page_settings_stacked_widget_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_settings_stacked_widget_container.sizePolicy().hasHeightForWidth())
        self.page_settings_stacked_widget_container.setSizePolicy(sizePolicy2)
        self.page_settings_stacked_widget_container.setFrameShape(QFrame.NoFrame)
        self.page_settings_stacked_widget_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.page_settings_stacked_widget_container)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.page_settings_stacked_widget = QStackedWidget(self.page_settings_stacked_widget_container)
        self.page_settings_stacked_widget.setObjectName(u"page_settings_stacked_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page_settings_stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_settings_stacked_widget.addWidget(self.page_2)

        self.horizontalLayout_14.addWidget(self.page_settings_stacked_widget)


        self.horizontalLayout_13.addWidget(self.page_settings_stacked_widget_container)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_3.addWidget(self.stackedWidget)

        self.grip_down_left = QFrame(self.body_container_2)
        self.grip_down_left.setObjectName(u"grip_down_left")
        self.grip_down_left.setMinimumSize(QSize(10, 10))
        self.grip_down_left.setMaximumSize(QSize(10, 10))
        self.grip_down_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.grip_down_left.setFrameShape(QFrame.NoFrame)
        self.grip_down_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.grip_down_left, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.body_container_2)


        self.window_layout.addWidget(self.body_container)


        self.horizontalLayout.addLayout(self.window_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_go_to_settings.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)
        self.page_settings_stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PyTrack", None))
        self.label_4.setText("")
        self.button_minimize.setText("")
        self.button_maximize.setText("")
        self.button_go_to_home.setText("")
        self.button_go_to_analytics.setText("")
        self.button_go_to_settings.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PyTrack Is Active", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Deactivate", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"page 2", None))
        self.button_settings_general.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.button_settings_window.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.button_settings_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

