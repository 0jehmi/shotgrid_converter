import sys

from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QFileDialog

from python.sg_converter import *


class SgConverterController:
    def __init__(self):
        self.ui = SgConverterUi()
        self.sg_data = SgData()

        self.proj_id = None
        self.seq_id = None
        self.shot_id = None
        self.task_id = None

        self.proj_dict = {}
        self.seq_dict = {}
        self.shot_dict = {}
        self.task_dict = {}

        # 실행
        self.project_combobox_item()
        self.selected_project_id()

        # event handler
        self.ui.path_but.clicked.connect(self.path_but_clicked)
        self.ui.converup_but.clicked.connect(self.converup_but_clicked)

        self.ui.project_combobox.currentIndexChanged.connect(self.selected_project_id)
        self.ui.seq_combobox.currentIndexChanged.connect(self.selected_seq_id)
        self.ui.shot_combobox.currentIndexChanged.connect(self.selected_shot_id)
        self.ui.task_combobox.currentIndexChanged.connect(self.selected_task_id)

    def project_combobox_item(self):
        self.ui.clear_combobox()
        projects = self.sg_data.get_project()
        self.proj_dict = {proj['name']: proj for proj in projects}
        self.ui.project_combobox.addItems(self.proj_dict.keys())

    def selected_project_id(self):
        selected_proj = self.ui.project_combobox.currentText()
        if not selected_proj:
            return
        self.proj_id = self.proj_dict[selected_proj]['id']
        self.seq_combobox_item()

    def seq_combobox_item(self):
        self.ui.clear_combobox(except_proj=True)
        selected_seq = self.sg_data.get_seq(self.proj_id)
        self.seq_dict = {seq['code']: seq for seq in selected_seq}
        self.ui.seq_combobox.addItems(self.seq_dict.keys())

    def selected_seq_id(self):
        selected_seq = self.ui.seq_combobox.currentText()
        if not selected_seq:
            return
        self.seq_id = self.seq_dict[selected_seq]['id']
        self.shot_combobox_item()

    def shot_combobox_item(self):
        self.ui.clear_combobox(except_proj=True, except_seq=True)
        selected_shot = self.sg_data.get_shot(self.seq_id)
        self.shot_dict = {shot['code']: shot for shot in selected_shot}
        self.ui.shot_combobox.addItems(self.shot_dict.keys())

    def selected_shot_id(self):
        selected_shot = self.ui.shot_combobox.currentText()
        if not selected_shot:
            return
        self.shot_id = self.shot_dict[selected_shot]['id']
        self.task_combobox_item()

    def task_combobox_item(self):
        self.ui.clear_combobox(except_proj=True, except_seq=True, except_shot=True)
        selected_task = self.sg_data.get_task(self.shot_id)
        self.task_dict = {task['content']: task for task in selected_task}
        self.ui.task_combobox.addItems(self.task_dict.keys())

    def selected_task_id(self):
        selected_task = self.ui.task_combobox.currentText()
        if not selected_task:
            return
        self.task_id = self.task_dict[selected_task]['id']

    def path_but_clicked(self):
        self.ui.path_line.clear()
        selected_directory = QFileDialog.getExistingDirectory(self.ui, "Select Directory", options=QFileDialog.ShowDirsOnly)
        if not selected_directory:
            return
        self.ui.path_but = selected_directory
        self.ui.path_line.setText(self.ui.path_but)
        self.file_list_view()

    def file_list_view(self):
        self.ui.file_list_view.clear()
        file_list = self.sg_data.path_file_list(self.ui.path_but)
        for list_item in file_list:
            self.ui.file_list_view.addItem(list_item)

    def converup_but_clicked(self):
        self.ui.converup_msg.show()
        QtWidgets.QApplication.processEvents()
        self.sg_data.converting(self.ui.path_but)
        self.sg_data.sg_upload(self.proj_id, self.shot_id, self.task_id)
        self.ui.converup_msg.accept()
        self.ui.completed_msg()


def main():
    app = QtWidgets.QApplication()
    controller = SgConverterController()
    controller.ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()