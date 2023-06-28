# What is sg_converter

sg_converter는 선택한 jpg 이미지 시퀀스를 mp4로 컨버팅하고 

선택한 shotgrid tasks의 versions 필드에 upload 해주는 도구입니다.

# How to use sg_converter

1. sg_converter_module.py를 연다.
2. shotgrid SERVER_PATH / SCRIPT_NAME / SCRIPT_KEY 을 입력한다.
```
SERVER_PATH = ""
SCRIPT_NAME = ""
SCRIPT_KEY = ""
```
3. sg_converter_controller.py를 실행한다.
4. Project를 선택한다.
5. Shots을 선택한다.
6. Sequences를 선택한다.
7. Tasks를 선택한다.
8. convert & upload 할 파일을 선택한다.
9. Convert And Upload 버튼을 눌러 jpg 시퀀스 파일을 mp4로 컨버팅하고 shotgrid의 tasks-versions 필드에 업로드 한다. 
