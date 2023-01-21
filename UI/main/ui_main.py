# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 10))
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "QPushButton{\n" "	border: 2px solid gray\n" "	border-radius: 50px\n" "}\n" ""
        )
        self.verticalLayout_16 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setSpacing(8)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.main_grid_layout = QFrame(self.centralwidget)
        self.main_grid_layout.setObjectName("main_grid_layout")
        self.main_grid_layout.setFrameShape(QFrame.StyledPanel)
        self.main_grid_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_grid_layout)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.size_grip_top = QFrame(self.main_grid_layout)
        self.size_grip_top.setObjectName("size_grip_top")
        self.size_grip_top.setFrameShape(QFrame.StyledPanel)
        self.size_grip_top.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_top, 0, 1, 1, 1)

        self.size_grip_bottom = QFrame(self.main_grid_layout)
        self.size_grip_bottom.setObjectName("size_grip_bottom")
        self.size_grip_bottom.setFrameShape(QFrame.StyledPanel)
        self.size_grip_bottom.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_bottom, 2, 1, 1, 1)

        self.size_grip_left = QFrame(self.main_grid_layout)
        self.size_grip_left.setObjectName("size_grip_left")
        self.size_grip_left.setFrameShape(QFrame.StyledPanel)
        self.size_grip_left.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_left, 1, 0, 1, 1)

        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName("window_layout")
        self.header_container = QFrame(self.main_grid_layout)
        self.header_container.setObjectName("header_container")
        self.header_container.setMinimumSize(QSize(0, 32))
        self.header_container.setMaximumSize(QSize(16777215, 24))
        self.header_container.setFrameShape(QFrame.NoFrame)
        self.header_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.header_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header_container)
        self.header_left.setObjectName("header_left")
        self.header_left.setMinimumSize(QSize(10, 10))
        self.header_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.header_left.setFrameShape(QFrame.NoFrame)
        self.header_left.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.header_left)

        self.header_center = QFrame(self.header_container)
        self.header_center.setObjectName("header_center")
        self.header_center.setMinimumSize(QSize(160, 0))
        self.header_center.setFrameShape(QFrame.NoFrame)
        self.header_center.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.header_center)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.header_center)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setStyleSheet('font: 90 16pt "Times New Roman";')

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.header_center)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(24, 24))
        self.label_4.setMaximumSize(QSize(24, 24))
        self.label_4.setPixmap(QPixmap(":/logo/logo/logo small v2.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_4.addWidget(self.header_center)

        self.header_right = QFrame(self.header_container)
        self.header_right.setObjectName("header_right")
        self.header_right.setFrameShape(QFrame.NoFrame)
        self.header_right.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.header_right)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header_right)
        self.frame_2.setObjectName("frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.button_minimize = QPushButton(self.header_right)
        self.button_minimize.setObjectName("button_minimize")
        self.button_minimize.setStyleSheet("")
        icon = QIcon()
        icon.addFile(":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon)
        self.button_minimize.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_minimize)

        self.button_maximize = QPushButton(self.header_right)
        self.button_maximize.setObjectName("button_maximize")
        self.button_maximize.setStyleSheet("")
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_maximize.setIcon(icon1)
        self.button_maximize.setCheckable(True)
        self.button_maximize.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_maximize)

        self.button_exit = QPushButton(self.header_right)
        self.button_exit.setObjectName("button_exit")
        self.button_exit.setStyleSheet("")
        icon2 = QIcon()
        icon2.addFile(":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon2)
        self.button_exit.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_exit)

        self.horizontalLayout_4.addWidget(self.header_right)

        self.window_layout.addWidget(self.header_container)

        self.body_container = QFrame(self.main_grid_layout)
        self.body_container.setObjectName("body_container")
        self.body_container.setFrameShape(QFrame.NoFrame)
        self.body_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.body_container)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_container = QFrame(self.body_container)
        self.sidebar_container.setObjectName("sidebar_container")
        self.sidebar_container.setMinimumSize(QSize(56, 0))
        self.sidebar_container.setMaximumSize(QSize(56, 16777215))
        self.sidebar_container.setFrameShape(QFrame.NoFrame)
        self.sidebar_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.sidebar_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebaar_button_container = QFrame(self.sidebar_container)
        self.sidebaar_button_container.setObjectName("sidebaar_button_container")
        self.sidebaar_button_container.setFrameShape(QFrame.NoFrame)
        self.sidebaar_button_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.sidebaar_button_container)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 48, 0, 0)
        self.button_go_to_home = QPushButton(self.sidebaar_button_container)
        self.button_go_to_home.setObjectName("button_go_to_home")
        self.button_go_to_home.setMinimumSize(QSize(0, 56))
        self.button_go_to_home.setStyleSheet("border-radius : 50")
        icon3 = QIcon()
        icon3.addFile(":/icons/icons/homeX64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_home.setIcon(icon3)
        self.button_go_to_home.setIconSize(QSize(24, 24))
        self.button_go_to_home.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_home)

        self.button_go_to_analytics = QPushButton(self.sidebaar_button_container)
        self.button_go_to_analytics.setObjectName("button_go_to_analytics")
        self.button_go_to_analytics.setMinimumSize(QSize(0, 56))
        self.button_go_to_analytics.setStyleSheet("border-radius : 50")
        icon4 = QIcon()
        icon4.addFile(":/icons/icons/chart-histogram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_analytics.setIcon(icon4)
        self.button_go_to_analytics.setIconSize(QSize(24, 24))
        self.button_go_to_analytics.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_analytics)

        self.button_go_to_settings = QPushButton(self.sidebaar_button_container)
        self.button_go_to_settings.setObjectName("button_go_to_settings")
        self.button_go_to_settings.setMinimumSize(QSize(0, 56))
        self.button_go_to_settings.setStyleSheet("border-radius : 50")
        icon5 = QIcon()
        icon5.addFile(":/icons/icons/settings (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_settings.setIcon(icon5)
        self.button_go_to_settings.setIconSize(QSize(24, 24))
        self.button_go_to_settings.setAutoDefault(False)
        self.button_go_to_settings.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_settings)

        self.frame_3 = QFrame(self.sidebaar_button_container)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.sidebaar_button_container)

        self.sidebar_footer = QFrame(self.sidebar_container)
        self.sidebar_footer.setObjectName("sidebar_footer")
        self.sidebar_footer.setFrameShape(QFrame.NoFrame)
        self.sidebar_footer.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.sidebar_footer)

        self.horizontalLayout_2.addWidget(self.sidebar_container)

        self.body_container_2 = QFrame(self.body_container)
        self.body_container_2.setObjectName("body_container_2")
        self.body_container_2.setFrameShape(QFrame.NoFrame)
        self.body_container_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.body_container_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.body_container_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_3 = QVBoxLayout(self.page_home)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_home_header = QFrame(self.page_home)
        self.page_home_header.setObjectName("page_home_header")
        self.page_home_header.setMaximumSize(QSize(16777215, 125))
        self.page_home_header.setFrameShape(QFrame.NoFrame)
        self.page_home_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.page_home_header)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.page_home_header_left = QFrame(self.page_home_header)
        self.page_home_header_left.setObjectName("page_home_header_left")
        self.page_home_header_left.setFrameShape(QFrame.NoFrame)
        self.page_home_header_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.page_home_header_left)

        self.page_home_header_center = QFrame(self.page_home_header)
        self.page_home_header_center.setObjectName("page_home_header_center")
        self.page_home_header_center.setMinimumSize(QSize(0, 100))
        self.page_home_header_center.setFrameShape(QFrame.NoFrame)
        self.page_home_header_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.page_home_header_center)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QLabel(self.page_home_header_center)
        self.label_5.setObjectName("label_5")
        font = QFont()
        font.setFamilies(["Lucida Calligraphy"])
        font.setPointSize(28)
        self.label_5.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_5, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_19 = QLabel(self.page_home_header_center)
        self.label_19.setObjectName("label_19")
        font1 = QFont()
        font1.setFamilies(["MS UI Gothic"])
        font1.setPointSize(24)
        self.label_19.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_19)

        self.horizontalLayout_9.addWidget(self.page_home_header_center)

        self.page_home_header_right = QFrame(self.page_home_header)
        self.page_home_header_right.setObjectName("page_home_header_right")
        self.page_home_header_right.setFrameShape(QFrame.NoFrame)
        self.page_home_header_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.page_home_header_right)

        self.verticalLayout_3.addWidget(self.page_home_header)

        self.page_home_body = QFrame(self.page_home)
        self.page_home_body.setObjectName("page_home_body")
        self.page_home_body.setMinimumSize(QSize(0, 300))
        self.page_home_body.setFrameShape(QFrame.NoFrame)
        self.page_home_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.page_home_body)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.page_home_body_left = QFrame(self.page_home_body)
        self.page_home_body_left.setObjectName("page_home_body_left")
        self.page_home_body_left.setFrameShape(QFrame.NoFrame)
        self.page_home_body_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.page_home_body_left)

        self.page_home_body_center = QFrame(self.page_home_body)
        self.page_home_body_center.setObjectName("page_home_body_center")
        sizePolicy.setHeightForWidth(self.page_home_body_center.sizePolicy().hasHeightForWidth())
        self.page_home_body_center.setSizePolicy(sizePolicy)
        self.page_home_body_center.setFrameShape(QFrame.NoFrame)
        self.page_home_body_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.page_home_body_center)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QLabel(self.page_home_body_center)
        self.label.setObjectName("label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(":/logo/logo/logo v1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label, 0, Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.page_home_body_center)

        self.page_home_body_right = QFrame(self.page_home_body)
        self.page_home_body_right.setObjectName("page_home_body_right")
        self.page_home_body_right.setFrameShape(QFrame.NoFrame)
        self.page_home_body_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.page_home_body_right)

        self.verticalLayout_3.addWidget(self.page_home_body)

        self.page_home_footer = QFrame(self.page_home)
        self.page_home_footer.setObjectName("page_home_footer")
        self.page_home_footer.setFrameShape(QFrame.NoFrame)
        self.page_home_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.page_home_footer)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.page_home_footer_left = QFrame(self.page_home_footer)
        self.page_home_footer_left.setObjectName("page_home_footer_left")
        self.page_home_footer_left.setFrameShape(QFrame.NoFrame)
        self.page_home_footer_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.page_home_footer_left)

        self.page_home_footer_center = QFrame(self.page_home_footer)
        self.page_home_footer_center.setObjectName("page_home_footer_center")
        self.page_home_footer_center.setMinimumSize(QSize(310, 160))
        self.page_home_footer_center.setMaximumSize(QSize(310, 160))
        self.page_home_footer_center.setFrameShape(QFrame.NoFrame)
        self.page_home_footer_center.setFrameShadow(QFrame.Raised)
        self.button_activate_deactivate_main_loop = QPushButton(self.page_home_footer_center)
        self.button_activate_deactivate_main_loop.setObjectName("button_activate_deactivate_main_loop")
        self.button_activate_deactivate_main_loop.setGeometry(QRect(60, 30, 151, 41))
        font2 = QFont()
        font2.setFamilies(["Times New Roman"])
        font2.setPointSize(14)
        self.button_activate_deactivate_main_loop.setFont(font2)
        self.button_activate_deactivate_main_loop.setAutoFillBackground(False)
        self.button_activate_deactivate_main_loop.setStyleSheet("QPushButton{\n" "	border: 2px solid gray;\n" "	border-radius: 20px;\n" "\n" "}")
        icon6 = QIcon()
        iconThemeName = "applications-games"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile("../../../../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.button_activate_deactivate_main_loop.setIcon(icon6)
        self.button_activate_deactivate_main_loop.setCheckable(True)
        self.button_activate_deactivate_main_loop.setFlat(True)
        self.label_points_home = QLabel(self.page_home_footer_center)
        self.label_points_home.setObjectName("label_points_home")
        self.label_points_home.setGeometry(QRect(110, 10, 61, 21))

        self.horizontalLayout_10.addWidget(self.page_home_footer_center)

        self.page_home_footerright = QFrame(self.page_home_footer)
        self.page_home_footerright.setObjectName("page_home_footerright")
        self.page_home_footerright.setFrameShape(QFrame.NoFrame)
        self.page_home_footerright.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.page_home_footerright)

        self.verticalLayout_3.addWidget(self.page_home_footer)

        self.stackedWidget.addWidget(self.page_home)
        self.page_analytics = QWidget()
        self.page_analytics.setObjectName("page_analytics")
        self.horizontalLayout_12 = QHBoxLayout(self.page_analytics)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.page_analytics_window_container = QFrame(self.page_analytics)
        self.page_analytics_window_container.setObjectName("page_analytics_window_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.page_analytics_window_container.sizePolicy().hasHeightForWidth())
        self.page_analytics_window_container.setSizePolicy(sizePolicy2)
        self.page_analytics_window_container.setFrameShape(QFrame.NoFrame)
        self.page_analytics_window_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.page_analytics_window_container)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_analytics_window_container)
        self.frame_4.setObjectName("frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMaximumSize(QSize(16777215, 120))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(10, 0, 221, 51))
        font3 = QFont()
        font3.setFamilies(["MS Sans Serif"])
        font3.setPointSize(22)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet('font: 22pt "MS Sans Serif";')

        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName("frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 146, 38))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName("label_15")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.comboBox_date = QComboBox(self.frame_13)
        self.comboBox_date.setObjectName("comboBox_date")

        self.horizontalLayout_18.addWidget(self.comboBox_date)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName("frame_14")
        self.frame_14.setGeometry(QRect(190, 10, 146, 38))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName("label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.comboBox_type = QComboBox(self.frame_14)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.setEditable(False)

        self.horizontalLayout_19.addWidget(self.comboBox_type)

        self.verticalLayout_7.addWidget(self.frame_8)

        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_analytics_window_container)
        self.frame_5.setObjectName("frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea_window_records = QScrollArea(self.frame_5)
        self.scrollArea_window_records.setObjectName("scrollArea_window_records")
        self.scrollArea_window_records.setMinimumSize(QSize(420, 300))
        self.scrollArea_window_records.setMaximumSize(QSize(12321, 600))
        self.scrollArea_window_records.setFrameShape(QFrame.NoFrame)
        self.scrollArea_window_records.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_window_records.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_window_records.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 528, 465))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy5)
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.scroll_area_contents_layout = QVBoxLayout()
        self.scroll_area_contents_layout.setObjectName("scroll_area_contents_layout")

        self.verticalLayout_17.addLayout(self.scroll_area_contents_layout)

        self.scrollArea_window_records.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea_window_records)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.horizontalLayout_12.addWidget(self.page_analytics_window_container)

        self.page_analytic_points_container = QFrame(self.page_analytics)
        self.page_analytic_points_container.setObjectName("page_analytic_points_container")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(4)
        sizePolicy6.setVerticalStretch(4)
        sizePolicy6.setHeightForWidth(self.page_analytic_points_container.sizePolicy().hasHeightForWidth())
        self.page_analytic_points_container.setSizePolicy(sizePolicy6)
        self.page_analytic_points_container.setFrameShape(QFrame.NoFrame)
        self.page_analytic_points_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.page_analytic_points_container)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_14 = QLabel(self.page_analytic_points_container)
        self.label_14.setObjectName("label_14")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy7)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet('font: 22pt "MS Sans Serif";')

        self.verticalLayout_14.addWidget(self.label_14)

        self.point_graph_container = QFrame(self.page_analytic_points_container)
        self.point_graph_container.setObjectName("point_graph_container")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(9)
        sizePolicy8.setHeightForWidth(self.point_graph_container.sizePolicy().hasHeightForWidth())
        self.point_graph_container.setSizePolicy(sizePolicy8)
        self.point_graph_container.setStyleSheet("")
        self.point_graph_container.setFrameShape(QFrame.Box)
        self.point_graph_container.setFrameShadow(QFrame.Raised)
        self.point_graph_container.setLineWidth(1)
        self.verticalLayout_19 = QVBoxLayout(self.point_graph_container)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.point_graph_container_layout = QVBoxLayout()
        self.point_graph_container_layout.setObjectName("point_graph_container_layout")

        self.verticalLayout_19.addLayout(self.point_graph_container_layout)

        self.verticalLayout_14.addWidget(self.point_graph_container)

        self.frame_6 = QFrame(self.page_analytic_points_container)
        self.frame_6.setObjectName("frame_6")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(4)
        sizePolicy9.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy9)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName("label_17")

        self.verticalLayout_15.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName("label_18")

        self.verticalLayout_15.addWidget(self.label_18)

        self.verticalLayout_14.addWidget(self.frame_6)

        self.horizontalLayout_12.addWidget(self.page_analytic_points_container)

        self.stackedWidget.addWidget(self.page_analytics)
        self.page_settings = QWidget()
        self.page_settings.setObjectName("page_settings")
        self.horizontalLayout_13 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.page_settings_pages_container = QFrame(self.page_settings)
        self.page_settings_pages_container.setObjectName("page_settings_pages_container")
        self.page_settings_pages_container.setMinimumSize(QSize(100, 0))
        self.page_settings_pages_container.setMaximumSize(QSize(160, 16777215))
        self.page_settings_pages_container.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.page_settings_pages_container)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.page_settings_pages_container_top = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_top.setObjectName("page_settings_pages_container_top")
        self.page_settings_pages_container_top.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.page_settings_pages_container_top)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.button_settings_general = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_general.setObjectName("button_settings_general")
        self.button_settings_general.setMinimumSize(QSize(100, 40))
        font4 = QFont()
        font4.setPointSize(10)
        self.button_settings_general.setFont(font4)
        self.button_settings_general.setStyleSheet("border-radius : 50")
        self.button_settings_general.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_general)

        self.button_settings_window = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_window.setObjectName("button_settings_window")
        self.button_settings_window.setEnabled(True)
        self.button_settings_window.setMinimumSize(QSize(100, 40))
        self.button_settings_window.setFont(font4)
        self.button_settings_window.setStyleSheet("border-radius : 50")
        self.button_settings_window.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_window)

        self.frame_9 = QFrame(self.page_settings_pages_container_top)
        self.frame_9.setObjectName("frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.button_settings_about = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_about.setObjectName("button_settings_about")
        self.button_settings_about.setMinimumSize(QSize(100, 40))
        self.button_settings_about.setFont(font4)
        self.button_settings_about.setStyleSheet("border-radius : 50")
        self.button_settings_about.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_about)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_top)

        self.page_settings_pages_container_center = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_center.setObjectName("page_settings_pages_container_center")
        self.page_settings_pages_container_center.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_center.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_center)

        self.page_settings_pages_container_bot = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_bot.setObjectName("page_settings_pages_container_bot")
        self.page_settings_pages_container_bot.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_bot.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_bot)

        self.horizontalLayout_13.addWidget(self.page_settings_pages_container)

        self.page_settings_stacked_widget_container = QFrame(self.page_settings)
        self.page_settings_stacked_widget_container.setObjectName("page_settings_stacked_widget_container")
        sizePolicy10 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.page_settings_stacked_widget_container.sizePolicy().hasHeightForWidth())
        self.page_settings_stacked_widget_container.setSizePolicy(sizePolicy10)
        self.page_settings_stacked_widget_container.setFrameShape(QFrame.NoFrame)
        self.page_settings_stacked_widget_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.page_settings_stacked_widget_container)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.page_settings_stacked_widget = QStackedWidget(self.page_settings_stacked_widget_container)
        self.page_settings_stacked_widget.setObjectName("page_settings_stacked_widget")
        self.page_settings_stacked_widget_page_general = QWidget()
        self.page_settings_stacked_widget_page_general.setObjectName("page_settings_stacked_widget_page_general")
        self.verticalLayout_9 = QVBoxLayout(self.page_settings_stacked_widget_page_general)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.page_general_header = QFrame(self.page_settings_stacked_widget_page_general)
        self.page_general_header.setObjectName("page_general_header")
        self.page_general_header.setMinimumSize(QSize(0, 80))
        self.page_general_header.setMaximumSize(QSize(16777215, 80))
        self.page_general_header.setFrameShape(QFrame.NoFrame)
        self.page_general_header.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.page_general_header)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, -10, 221, 51))
        self.label_2.setStyleSheet('font: 22pt "MS Sans Serif";')

        self.verticalLayout_9.addWidget(self.page_general_header)

        self.page_general_footer = QFrame(self.page_settings_stacked_widget_page_general)
        self.page_general_footer.setObjectName("page_general_footer")
        self.page_general_footer.setFrameShape(QFrame.NoFrame)
        self.page_general_footer.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.page_general_footer)
        self.frame_10.setObjectName("frame_10")
        self.frame_10.setGeometry(QRect(50, 10, 403, 146))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName("label_8")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_8.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_8)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName("frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_16.addWidget(self.label_9)

        self.line_edit_point_threshold_break = QLineEdit(self.frame_11)
        self.line_edit_point_threshold_break.setObjectName("line_edit_point_threshold_break")
        self.line_edit_point_threshold_break.setInputMethodHints(Qt.ImhDigitsOnly | Qt.ImhPreferNumbers)

        self.horizontalLayout_16.addWidget(self.line_edit_point_threshold_break)

        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName("frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_17.addWidget(self.label_10)

        self.line_edit_point_threshold_warning = QLineEdit(self.frame_12)
        self.line_edit_point_threshold_warning.setObjectName("line_edit_point_threshold_warning")

        self.horizontalLayout_17.addWidget(self.line_edit_point_threshold_warning)

        self.verticalLayout_12.addWidget(self.frame_12)

        self.verticalLayout_9.addWidget(self.page_general_footer)

        self.page_settings_stacked_widget.addWidget(self.page_settings_stacked_widget_page_general)
        self.page_settings_stacked_widget_page_window = QWidget()
        self.page_settings_stacked_widget_page_window.setObjectName("page_settings_stacked_widget_page_window")
        self.verticalLayout_10 = QVBoxLayout(self.page_settings_stacked_widget_page_window)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.page_window_header_2 = QFrame(self.page_settings_stacked_widget_page_window)
        self.page_window_header_2.setObjectName("page_window_header_2")
        self.page_window_header_2.setMinimumSize(QSize(0, 80))
        self.page_window_header_2.setMaximumSize(QSize(16777215, 80))
        self.page_window_header_2.setFrameShape(QFrame.NoFrame)
        self.page_window_header_2.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.page_window_header_2)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(10, -10, 221, 51))
        self.label_6.setStyleSheet('font: 22pt "MS Sans Serif";')

        self.verticalLayout_10.addWidget(self.page_window_header_2)

        self.page_window_footer_2 = QFrame(self.page_settings_stacked_widget_page_window)
        self.page_window_footer_2.setObjectName("page_window_footer_2")
        self.page_window_footer_2.setFrameShape(QFrame.NoFrame)
        self.page_window_footer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.page_window_footer_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_15 = QFrame(self.page_window_footer_2)
        self.frame_15.setObjectName("frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.button_add_windows = QPushButton(self.frame_15)
        self.button_add_windows.setObjectName("button_add_windows")
        self.button_add_windows.setGeometry(QRect(10, 20, 75, 23))
        self.button_add_windows.setFlat(True)

        self.verticalLayout_18.addWidget(self.frame_15)

        self.scrollArea = QScrollArea(self.page_window_footer_2)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 47, 20))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.add_window_contents_layout = QVBoxLayout()
        self.add_window_contents_layout.setObjectName("add_window_contents_layout")

        self.verticalLayout_21.addLayout(self.add_window_contents_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.verticalLayout_10.addWidget(self.page_window_footer_2)

        self.page_settings_stacked_widget.addWidget(self.page_settings_stacked_widget_page_window)
        self.page_settings_stacked_widget_page_about = QWidget()
        self.page_settings_stacked_widget_page_about.setObjectName("page_settings_stacked_widget_page_about")
        self.verticalLayout_11 = QVBoxLayout(self.page_settings_stacked_widget_page_about)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.page_about_header_3 = QFrame(self.page_settings_stacked_widget_page_about)
        self.page_about_header_3.setObjectName("page_about_header_3")
        self.page_about_header_3.setMinimumSize(QSize(0, 80))
        self.page_about_header_3.setMaximumSize(QSize(16777215, 80))
        self.page_about_header_3.setFrameShape(QFrame.NoFrame)
        self.page_about_header_3.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.page_about_header_3)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(10, -10, 221, 51))
        self.label_7.setStyleSheet('font: 22pt "MS Sans Serif";')

        self.verticalLayout_11.addWidget(self.page_about_header_3)

        self.page_about_body_3 = QFrame(self.page_settings_stacked_widget_page_about)
        self.page_about_body_3.setObjectName("page_about_body_3")
        self.page_about_body_3.setFrameShape(QFrame.NoFrame)
        self.page_about_body_3.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.page_about_body_3)
        self.frame_16.setObjectName("frame_16")
        self.frame_16.setGeometry(QRect(0, 30, 141, 101))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.button_link_to_twitter = QPushButton(self.frame_16)
        self.button_link_to_twitter.setObjectName("button_link_to_twitter")
        self.button_link_to_twitter.setFlat(True)

        self.verticalLayout_13.addWidget(self.button_link_to_twitter)

        self.button_link_to_github = QPushButton(self.frame_16)
        self.button_link_to_github.setObjectName("button_link_to_github")
        self.button_link_to_github.setFlat(True)

        self.verticalLayout_13.addWidget(self.button_link_to_github)

        self.label_11 = QLabel(self.page_about_body_3)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(10, 10, 151, 20))
        self.label_11.setFont(font5)
        self.label_11.setFrameShape(QFrame.NoFrame)
        self.label_12 = QLabel(self.page_about_body_3)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(50, 150, 351, 61))
        self.label_12.setWordWrap(True)
        self.button_link_to_youtube_video = QPushButton(self.page_about_body_3)
        self.button_link_to_youtube_video.setObjectName("button_link_to_youtube_video")
        self.button_link_to_youtube_video.setGeometry(QRect(20, 220, 131, 31))
        self.button_link_to_youtube_video.setFlat(True)
        self.button_link_to_youtube_channel = QPushButton(self.page_about_body_3)
        self.button_link_to_youtube_channel.setObjectName("button_link_to_youtube_channel")
        self.button_link_to_youtube_channel.setGeometry(QRect(10, 250, 161, 31))
        self.button_link_to_youtube_channel.setFlat(True)
        self.label_20 = QLabel(self.page_about_body_3)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(10, 310, 151, 20))
        self.label_20.setFont(font5)
        self.label_20.setFrameShape(QFrame.NoFrame)
        self.label_21 = QLabel(self.page_about_body_3)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(40, 330, 351, 41))
        self.label_21.setWordWrap(True)
        self.button_link_to_github_repository = QPushButton(self.page_about_body_3)
        self.button_link_to_github_repository.setObjectName("button_link_to_github_repository")
        self.button_link_to_github_repository.setGeometry(QRect(0, 400, 171, 23))
        self.button_link_to_github_repository.setFlat(True)

        self.verticalLayout_11.addWidget(self.page_about_body_3)

        self.page_settings_stacked_widget.addWidget(self.page_settings_stacked_widget_page_about)

        self.horizontalLayout_14.addWidget(self.page_settings_stacked_widget)

        self.horizontalLayout_13.addWidget(self.page_settings_stacked_widget_container)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_3.addWidget(self.stackedWidget)

        self.grip_down_left = QFrame(self.body_container_2)
        self.grip_down_left.setObjectName("grip_down_left")
        self.grip_down_left.setMinimumSize(QSize(10, 10))
        self.grip_down_left.setMaximumSize(QSize(10, 10))
        self.grip_down_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.grip_down_left.setFrameShape(QFrame.NoFrame)
        self.grip_down_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.grip_down_left, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.body_container_2)

        self.window_layout.addWidget(self.body_container)

        self.gridLayout.addLayout(self.window_layout, 1, 1, 1, 1)

        self.size_grip_right = QFrame(self.main_grid_layout)
        self.size_grip_right.setObjectName("size_grip_right")
        self.size_grip_right.setFrameShape(QFrame.StyledPanel)
        self.size_grip_right.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_right, 1, 2, 1, 1)

        self.size_grip_top_left = QFrame(self.main_grid_layout)
        self.size_grip_top_left.setObjectName("size_grip_top_left")
        self.size_grip_top_left.setFrameShape(QFrame.StyledPanel)
        self.size_grip_top_left.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_top_left, 0, 0, 1, 1)

        self.size_grip_top_right = QFrame(self.main_grid_layout)
        self.size_grip_top_right.setObjectName("size_grip_top_right")
        self.size_grip_top_right.setFrameShape(QFrame.StyledPanel)
        self.size_grip_top_right.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_top_right, 0, 2, 1, 1)

        self.size_grip_bottom_right = QFrame(self.main_grid_layout)
        self.size_grip_bottom_right.setObjectName("size_grip_bottom_right")
        self.size_grip_bottom_right.setFrameShape(QFrame.StyledPanel)
        self.size_grip_bottom_right.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_bottom_right, 2, 2, 1, 1)

        self.size_grip_bottom_left = QFrame(self.main_grid_layout)
        self.size_grip_bottom_left.setObjectName("size_grip_bottom_left")
        self.size_grip_bottom_left.setFrameShape(QFrame.StyledPanel)
        self.size_grip_bottom_left.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.size_grip_bottom_left, 2, 0, 1, 1)

        self.verticalLayout_16.addWidget(self.main_grid_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_go_to_settings.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.page_settings_stacked_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "PyTrack", None))
        self.label_4.setText("")
        self.button_minimize.setText("")
        self.button_maximize.setText("")
        self.button_go_to_home.setText("")
        self.button_go_to_analytics.setText("")
        self.button_go_to_settings.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", "PyTrack", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", " Is Active", None))
        self.label.setText("")
        self.button_activate_deactivate_main_loop.setText(QCoreApplication.translate("MainWindow", "Deactivate", None))
        self.label_points_home.setText(QCoreApplication.translate("MainWindow", "Points: 450", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", "Windows", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", "Date:", None))
        self.comboBox_date.setCurrentText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", "Type", None))
        self.comboBox_type.setCurrentText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", "Points Graph", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", "Minimum Points", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", "Maximum Points", None))
        self.button_settings_general.setText(QCoreApplication.translate("MainWindow", "General", None))
        self.button_settings_window.setText(QCoreApplication.translate("MainWindow", "Window", None))
        self.button_settings_about.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "General", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", "App", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Point Treshold(Break)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", "Point Treshold(warning)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Window", None))
        self.button_add_windows.setText(QCoreApplication.translate("MainWindow", "Add Window", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.button_link_to_twitter.setText(QCoreApplication.translate("MainWindow", "Twitter", None))
        self.button_link_to_github.setText(QCoreApplication.translate("MainWindow", "Github", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", "Socials", None))
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                "I made this application as my year end project and my goal is to make a video out of it and post to youtube. If you would want to watch the video the link will be below.",
                None,
            )
        )
        self.button_link_to_youtube_video.setText(QCoreApplication.translate("MainWindow", "Youtube Video", None))
        self.button_link_to_youtube_channel.setText(QCoreApplication.translate("MainWindow", "Youtube Channel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", "Contribute", None))
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", "This project is open source if you want to contribute you can using GitHub. Link Below", None)
        )
        self.button_link_to_github_repository.setText(QCoreApplication.translate("MainWindow", "GitHub Repository", None))

    # retranslateUi
