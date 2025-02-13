import PySimpleGUI as sg
import os
from git_commands import (
    git_status, git_log, git_add, git_commit,
    git_remote_list, git_push, git_pull, git_detailed_log
)

# 현재 폴더를 기본 Git 저장소 경로로 설정
repo_path = os.getcwd()

# GUI 레이아웃 설정
layout = [
    [sg.Text("Git Repository Path:"), sg.InputText(repo_path, key='-REPO-', size=(50, 1))],
    [sg.Button("Git Status"), sg.Button("Git Log"), sg.Button("Detailed Log")],
    [sg.Button("Add & Commit"), sg.Button("Git Push"), sg.Button("Git Pull"), sg.Button("Remote List")],
    [sg.Multiline(size=(80, 20), key='-OUTPUT-')],
]

# 윈도우 생성
window = sg.Window("Simple Git GUI", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    repo_path = values['-REPO-']  # 입력된 Git 저장소 경로 사용
    
    if event == "Git Status":
        output = git_status(repo_path)
    elif event == "Git Log":
        output = git_log(repo_path)
    elif event == "Detailed Log":
        output = git_detailed_log(repo_path)
    elif event == "Add & Commit":
        git_add(repo_path)
        output = git_commit(repo_path, "Auto commit")
    elif event == "Git Push":
        output = git_push(repo_path)
    elif event == "Git Pull":
        output = git_pull(repo_path)
    elif event == "Remote List":
        output = git_remote_list(repo_path)
    
    window['-OUTPUT-'].update(output)

window.close()
