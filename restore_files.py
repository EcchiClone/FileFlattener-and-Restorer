import os
import shutil
from datetime import datetime

# 설정
INPUT_DIR = 'flatten'  # 파일이 현재 위치하는 디렉토리 이름
LOG_DIR = 'Logs'       # 로그를 저장할 디렉토리
LOG_FILE_PATH = os.path.join(LOG_DIR, f'log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt')

def log_message(message):
    with open(LOG_FILE_PATH, 'a') as file:
        file.write(message + "\n")
    print(message)

def restore_files_to_original_path(base_dir):
    # 로그 디렉토리 생성
    os.makedirs(os.path.join(base_dir, LOG_DIR), exist_ok=True)
    
    input_path = os.path.join(base_dir, INPUT_DIR)
    
    if not os.path.exists(input_path):
        log_message(f"The directory {input_path} does not exist.")
        return

    for file in os.listdir(input_path):
        full_file_path = os.path.join(input_path, file)
        if os.path.isfile(full_file_path):
            parts = file.split('_')
            original_dir_path = os.path.join(base_dir, *parts[:-1])
            original_file_name = parts[-1]
            
            os.makedirs(original_dir_path, exist_ok=True)
            original_file_path = os.path.join(original_dir_path, original_file_name)
            shutil.move(full_file_path, original_file_path)
            log_message(f"FilePath: {full_file_path}\nMoved: {input_path} -> {original_dir_path}\nRestore: {file} -> {original_file_name}\n")

if __name__ == "__main__":
    base_dir = '.'  # 이 스크립트의 위치
    restore_files_to_original_path(base_dir)
