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

# Examples

<img width="616" alt="sg_converter_1" src="https://github.com/0jehmi/files_renamer/assets/122579358/54656a0f-8210-4f28-8f3d-b7ec77632ed3">
>구동예시

<img width="225" alt="sg_converter_2" src="https://github.com/0jehmi/files_renamer/assets/122579358/e97bf86b-0f13-487d-b808-0422986a90ca">
>convertin & Uploading 중 messagebox  

<img width="133" alt="sg_converter_3" src="https://github.com/0jehmi/files_renamer/assets/122579358/a453f42c-c518-4338-a2f0-e7ef2d732ab4">
>완료 후 messagebox

<img width="1394" alt="sg_converter_4" src="https://github.com/0jehmi/files_renamer/assets/122579358/611903ba-58a8-44f6-8352-5911ae3f3c1c">
>Result
- ShotGrid 홈페이지의 tasks-versions필드에 upload된 mp4

