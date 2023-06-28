import sys

from PySide2 import QtWidgets, QtGui, QtCore


class SgConverterUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sg converter")
        self.setFixedSize(1200, 600)
        self.screen_resolution = QtGui.QGuiApplication.primaryScreen().geometry()
        x = (self.screen_resolution.width() - self.width()) / 2
        y = (self.screen_resolution.height() - self.height()) / 2
        self.setGeometry(x, y, 1200, 500)

        self.path_but = None
        self.path_line = None
        self.file_list_view = None

        self.converup_but = None
        self.converup_msg = None

        self.project_combobox = None
        self.seq_combobox = None
        self.shot_combobox = None
        self.task_combobox = None
        self.file_list_view = None

        self.main_ui()

    def main_ui(self):
        self.path_but = QtWidgets.QPushButton("...", self)
        self.path_but.setFixedSize(80, 30)
        self.path_but.move(1080, 120)

        self.path_line = QtWidgets.QLineEdit(self)
        self.path_line.setFixedSize(1020, 30)
        self.path_line.move(40, 120)

        self.file_list_view = QtWidgets.QListWidget(self)
        self.file_list_view.setFixedSize(1120, 290)
        self.file_list_view.move(40, 170)

        self.converup_but = QtWidgets.QPushButton("Convert And Upload", self)
        self.converup_but.setFixedSize(1120, 90)
        self.converup_but.move(40, 480)

        self.converup_msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "Information", "Converting & Uploading, please wait...")
        self.converup_msg.setStandardButtons(QtWidgets.QMessageBox.NoButton)

        self.project_combobox = QtWidgets.QComboBox(self)
        self.project_combobox.setFixedSize(310, 30)
        self.project_combobox.move(40, 60)
        self.seq_combobox = QtWidgets.QComboBox(self)
        self.seq_combobox.setFixedSize(240, 30)
        self.seq_combobox.move(400, 60)
        self.shot_combobox = QtWidgets.QComboBox(self)
        self.shot_combobox.setFixedSize(240, 30)
        self.shot_combobox.move(660, 60)
        self.task_combobox = QtWidgets.QComboBox(self)
        self.task_combobox.setFixedSize(240, 30)
        self.task_combobox.move(920, 60)

    def completed_msg(self):
        completed_msg = QtWidgets.QMessageBox()
        completed_msg.setWindowTitle("Conversion Completed")
        completed_msg.setText("completed")
        completed_msg.exec_()

    def clear_combobox(self, except_proj=False, except_seq=False, except_shot=False):
        if not except_proj:
            self.project_combobox.clear()
        if not except_seq:
            self.seq_combobox.clear()
        if not except_shot:
            self.shot_combobox.clear()
        self.task_combobox.clear()


def main():
    app = QtWidgets.QApplication()
    ui = SgConverterUi()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()