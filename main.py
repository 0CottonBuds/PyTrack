from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Qt
from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtCharts import QChartView, QChart, QLineSeries

import pygetwindow

from UI.main.ui_main import Ui_MainWindow
from UI.WindowRecordUi.window_record import Ui_Window_Record
from UI.AddWindowUi.add_window import UiAddWindow

from PytrackUtils.config_helper import edit_config, read_config
from PytrackUtils.window_record_reader import *
from PytrackUtils.window_type import *
from PytrackUtils.webbrowser_helper import *
from PytrackUtils.stylesheet_helper import change_stylesheet, get_themes

from PytrackUtils.PyTrackWorker import PyTrackWorker

import sys

class PytrackMainWindow(QMainWindow, Ui_MainWindow):
    main_loop_active : bool
    pytrack_worker : PyTrackWorker

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pytrack")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # type: ignore

        self.pytrack_worker = PyTrackWorker(self)

        self.main_loop_active = False

        self.place_holder_text_init()
        self.combo_box_items_init()
        self.charts_init()
        self.timers_init()

        self.buttons_init()
        self.text_edit_init()
        self.combo_box_signals_init()

        # set stylesheet as the first one on the list by default
        change_stylesheet(self, read_config("config.ini", "App", "theme"), app)
        
        self.show()

    ###INIT FUNCTIONS ###

    def place_holder_text_init(self):
        # setting text and placeholder texts
        self.button_activate_deactivate_main_loop.setText("Activate")
        self.line_edit_point_threshold_break.setPlaceholderText(str(self.pytrack_worker.point_tracker.threshold_break))
        self.line_edit_point_threshold_warning.setPlaceholderText(str(self.pytrack_worker.point_tracker.threshold_warning))

    def combo_box_items_init(self):
        # set combo box items
        combo_box_date_items = ["today", "yesterday", "this week", "this month", "all"]
        self.comboBox_date.addItems(combo_box_date_items)
        combo_box_type_items = ["all", "bad", "good"]
        self.comboBox_type.addItems(combo_box_type_items)
        self.get_records("today", "all")
        combo_box_theme_items = get_themes()
        self.comboBox_theme.addItems(combo_box_theme_items)
    
    def charts_init(self):
        # set Charts
        self.point_line_series = QLineSeries()
        self.point_line_series.append(0, self.pytrack_worker.point_tracker.points / 10)
        chart = QChart()
        chart.addSeries(self.point_line_series)
        chart.setTitle("Points Over Time")

        self.chart_view = QChartView()
        self.chart_view.setChart(chart)
        self.point_graph_container_layout.addWidget(self.chart_view)

    def timers_init(self):
        # set timers
        self.main_loop_timer = QTimer()
        self.point_graph_timer = QTimer()

        # set timer signals to slots
        self.main_loop_timer.timeout.connect(self.pytrack_worker.main_loop)  # type: ignore
        self.point_graph_timer.timeout.connect(self.add_point_to_point_graph)

    def buttons_init(self):
        # setting the button signals to slots
        self.button_go_to_home.clicked.connect(self.go_to_home_page)  # type: ignore
        self.button_go_to_analytics.clicked.connect(self.go_to_analytics_page)  # type: ignore
        self.button_go_to_settings.clicked.connect(self.go_to_settings_page)  # type: ignore
        self.button_activate_deactivate_main_loop.clicked.connect(self.activate_deactivate_main_loop)  # type: ignore
        self.button_settings_general.clicked.connect(self.go_to_settings_general)  # type: ignore
        self.button_settings_window.clicked.connect(self.go_to_settings_window)  # type: ignore
        self.button_settings_about.clicked.connect(self.go_to_settings_about)  # type: ignore
        self.button_link_to_twitter.clicked.connect(go_to_link_twitter)  # type: ignore
        self.button_link_to_github.clicked.connect(go_to_link_github)  # type: ignore
        self.button_link_to_youtube_video.clicked.connect(go_to_link_youtube_video)  # type: ignore
        self.button_link_to_youtube_channel.clicked.connect(go_to_link_youtube_channel)  # type: ignore
        self.button_link_to_github_repository.clicked.connect(go_to_link_github_repository)  # type: ignore
        self.button_add_windows.clicked.connect(self.add_windows)  # type: ignore
        self.button_exit.clicked.connect(lambda q: sys.exit())
        self.button_minimize.clicked.connect(lambda m: self.showMinimized())

    def text_edit_init(self):
        # setting the text edit signals to slots
        self.line_edit_point_threshold_break.editingFinished.connect(self.edit_point_threshold_break)  # type: ignore
        self.line_edit_point_threshold_warning.editingFinished.connect(self.edit_point_threshold_warning)  # type: ignore

    def combo_box_signals_init(self):
        # set combo box signals to slots
        self.comboBox_date.currentTextChanged.connect(self.combo_box_date_updates)  # type: ignore
        self.comboBox_type.currentTextChanged.connect(self.combo_box_type_updates)  # type: ignore
        self.comboBox_theme.currentTextChanged.connect(self.combo_box_theme_updates) # type: ignore

    ### PYTRACK FUNCTIONS ###
    
    def activate_deactivate_main_loop(self):
        if not self.main_loop_active:
            print("Activated")
            time_to_loop = 5000  # msec(5 secs)
            self.main_loop_timer.start(time_to_loop)
            self.point_graph_timer.start(time_to_loop)
            self.main_loop_active = True
            self.button_activate_deactivate_main_loop.setText("Deactivate")
        elif self.main_loop_active:
            print("Deactivated")
            self.main_loop_timer.stop()
            self.point_graph_timer.stop()
            self.main_loop_active = False
            self.button_activate_deactivate_main_loop.setText("Activate")

    def get_records(self, query_date: str, query_type: str):
        """Fetches records by query date and type using the window record fetcher class and updates the scroll area contents

        Parameters:
            query_date: (string) date to query ex. today, yesterday, etc
            query_type: (string) type to query ex. good, bad, all"""

        print("getting records")
        records: list[WindowRecord] = []
        fetcher = WindowRecordFetcher()
        dates = fetcher.get_dates(query_date)
        fetcher.format_records(fetcher.retrieve_all_raw_records_by_many_dates(dates))
        fetcher.filter_formatted_records_by_type(query_type)
        records = fetcher.formatted_records
        records = get_time_of_each_window(records)
        records = get_percentage_of_time_of_each_window(records)
        self.update_scroll_area_contents(records)

    ### NAVIGATION FUNCTIONS ###

    def go_to_home_page(self):
        print("to home page")
        self.stackedWidget.setCurrentWidget(self.page_home)

    def go_to_analytics_page(self):
        print("to analytics page")
        self.stackedWidget.setCurrentWidget(self.page_analytics)

    def go_to_settings_page(self):
        print("go to settings page")
        self.stackedWidget.setCurrentWidget(self.page_settings)

    def go_to_settings_general(self):
        print("go to general settings")
        self.page_settings_stacked_widget.setCurrentWidget(self.page_settings_stacked_widget_page_general)

    def go_to_settings_window(self):
        print("go to window settings")
        self.page_settings_stacked_widget.setCurrentWidget(self.page_settings_stacked_widget_page_window)

    def go_to_settings_about(self):
        print("go to about settings")
        self.page_settings_stacked_widget.setCurrentWidget(self.page_settings_stacked_widget_page_about)

    ### CONFIG FUNCTIONS ###

    def edit_point_threshold_break(self):
        """edit the point threshold of break"""

        value = self.line_edit_point_threshold_break.text()
        if value == "":
            value: str = str(self.pytrack_worker.point_tracker.threshold_break)  # type: ignore bypass formatting

        if value.isnumeric():
            print(f"changing point threshold for break to {value}")

            edit_config("./config.ini", "App", "break_threshold", value)
            self.pytrack_worker.point_tracker.read_settings_config_file()

            # Set line edit placeholder text.
            self.line_edit_point_threshold_break.setPlaceholderText(str(self.pytrack_worker.point_tracker.threshold_break))
            self.line_edit_point_threshold_break.clear()
        else:
            print(f"tried to input {value} but it is not numeric.")

            # Set line edit placeholder text.
            self.line_edit_point_threshold_break.setPlaceholderText(str(self.pytrack_worker.point_tracker.threshold_break))
            self.line_edit_point_threshold_break.clear()

    def edit_point_threshold_warning(self):
        """edit the point threshold of warning"""

        value: str = self.line_edit_point_threshold_warning.text()
        if value == "":
            value = str(self.pytrack_worker.point_tracker.threshold_warning)  # type: ignore bypass formatting

        if value.isnumeric():
            print(f"changing point threshold for warning to {value}")

            edit_config("./config.ini", "App", "warning_threshold", value)
            self.pytrack_worker.point_tracker.read_settings_config_file()

            # Set line edit placeholder text.
            self.line_edit_point_threshold_warning.setPlaceholderText(str(self.pytrack_worker.point_tracker.threshold_warning))
            self.line_edit_point_threshold_warning.clear()
        else:
            print(f"tried to input {value} but it is not numeric.")

            # Set line edit placeholder text.
            self.line_edit_point_threshold_warning.setPlaceholderText(str(self.pytrack_worker.point_tracker.threshold_warning))
            self.line_edit_point_threshold_warning.clear()

    ### UI FUNCTIONS ###

    def combo_box_date_updates(self, text):
        print(f"signal: {text}")
        self.get_records(self.comboBox_date.currentText(), self.comboBox_type.currentText())

    def combo_box_type_updates(self, text):
        print(f"signal: {text}")
        self.get_records(self.comboBox_date.currentText(), self.comboBox_type.currentText())

    def combo_box_theme_updates(self, text):
        change_stylesheet(self, text, app)
        edit_config("config.ini", "App", "theme", text)

    def add_point_to_point_graph(self):
        count = self.point_line_series.count()
        points = self.pytrack_worker.point_tracker.points / 10  # points divided by 10
        self.point_line_series.append(count, points)
        self.update_chart_view()
        print(f"adding points: {count}, {points}")

    def update_chart_view(self):
        chart = QChart()
        chart.addSeries(self.point_line_series)
        chart.setTitle("Points Over Time")
        self.chart_view.setChart(chart)

    def update_scroll_area_contents(self, records: list[WindowRecord]):
        """Updates the scroll area contents by the list of window records that is passed

        Parameters:
            records: (list[WindowRecord]) list of window records that contains the data to update the contents of the scroll area"""

        # clears the scroll area
        for i in reversed(range(self.scroll_area_contents_layout.count())):
            self.scroll_area_contents_layout.itemAt(i).widget().setParent(None)  # type: ignore

        print("updating contents")
        for record in records:
            obj = Ui_Window_Record()
            obj.label_name.setText(record.window_short_name)
            obj.label_total_time.setText(str(record.window_time_elapsed.get_time()))
            obj.progressBar.setValue(int(record.window_time_elapsed.percentage))

            self.scroll_area_contents_layout.addWidget(obj)
            self.scroll_area_contents_layout.setAlignment(obj, Qt.AlignmentFlag.AlignTop)

    def add_windows(self):
        """this function spawns add window ui in the add ui scroll area"""
        window_filter = WindowFilter(pygetwindow.getAllWindows())
        window_filter.full_filter()

        # clear the add window contents layout
        for i in reversed(range(self.add_window_contents_layout.count())):
            self.add_window_contents_layout.itemAt(i).widget().setParent(None)  # type: ignore

        for window in window_filter.windows:
            add_window_ui = UiAddWindow(window.title)
            self.add_window_contents_layout.addWidget(add_window_ui)

    ### WINDOW FUNCTIONS ###

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), self.mapToGlobal(self.movement).y(), self.width(), self.height())
            self.start = self.end

    def mouseReleaseEvent(self, event):
        self.pressing = False


if __name__ == "__main__":
    app = QApplication()

    window = PytrackMainWindow()
    app.exec()
