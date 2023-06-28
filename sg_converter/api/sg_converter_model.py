import os
import re

import shotgun_api3

SERVER_PATH = ""
SCRIPT_NAME = ""
SCRIPT_KEY = ""

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


class SgData:

    def __init__(self):
        self._get_projects = None
        self._get_seqs = None
        self._get_shots = None
        self._get_tasks = None
        self._upload_projects = None
        self._upload_path = None

        self.output_path = None
        self.converted_file = ""

    def get_project(self):
        if not self._get_projects:
            self._get_projects = sg.find("Project", filters=[["sg_status", "is", "Active"]], fields=["name", "id"])
        return self._get_projects

    def get_seq(self, project_id=None):
        seq_filters = [["project", "is", {"type": "Project", "id": project_id}]]
        self._get_seqs = sg.find("Sequence", seq_filters, fields=["code", "id"])
        return self._get_seqs

    def get_shot(self, seq_id=None):
        shot_filters = [["sg_sequence", "is", {"type": "Sequence", "id": seq_id}]]
        self._get_shots = sg.find("Shot", shot_filters, fields=["code", "id"])
        return self._get_shots

    def get_task(self, shot_id=None):
        task_filters = [["entity", "is", {"type": "Shot", "id": shot_id}]]
        self._get_tasks = sg.find("Task", task_filters, fields=["content", "id"])
        return self._get_tasks

    def upload_project(self, proj_id=None):
        self._upload_projects = sg.find_one("Project", filters=[["id", "is", proj_id]], fields=["name", "id", "type"])
        return self._upload_projects

    def upload_path(self, upload_id=None):
        upload_filters = [["id", "is", upload_id]]
        self._upload_path = sg.find_one("Task", upload_filters, fields=["content", "id", "entity"])
        return self._upload_path

    def path_file_list(self, input_path=None):
        file_list = []
        files_list = []
        if input_path != '':
            for file in os.listdir(input_path):
                if os.path.isfile(os.path.join(input_path, file)):
                    file_list.append(file)
            if len(file_list) == 0:
                print("File not found")
            else:
                for files in file_list:
                    if files.endswith(".jpg"):
                        path_files = os.path.join(input_path, files)  # 파일 리스트
                        files_list.append(path_files)
                        files_list.sort(key=lambda x: int(re.search(r"\d+", x).group(0)))
                return files_list

    def converting(self, input_path=None):
        # converted 폴더 생성
        self.output_path = os.path.join(os.path.dirname(input_path), os.path.basename(input_path) + '_converted')
        os.makedirs(self.output_path, exist_ok=True)
        # converted 파일 생성
        self.converted_file = os.path.join(self.output_path, os.path.basename(self.output_path) + '.mp4')
        os.system(f'ffmpeg -framerate 25 -i "{input_path}/_%04d.jpg" -c:v libx264 -pix_fmt yuv420p {self.converted_file}')

    def sg_upload(self, proj_id=None, shot_id=None, task_id=None):
        selected_upload_file = self.upload_path(task_id)
        data = {
            "code": selected_upload_file["entity"]["name"],
            "project": self.upload_project(proj_id),
            "sg_path_to_movie": self.output_path,
            "sg_task": selected_upload_file,
            "entity": {"type": "Shot", "id": shot_id},
        }
        version = sg.create("Version", data)
        sg.upload("Version", version["id"], self.converted_file, "sg_uploaded_movie")


def main():
    sgd = SgData()


if __name__ == '__main__':
    main()
