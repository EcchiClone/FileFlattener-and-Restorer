import os
import shutil
from datetime import datetime

# 설정
OUTPUT_DIR = 'flatten'  # 이동될 디렉토리
LOG_DIR = 'Logs'        # 로그를 저장할 디렉토리
EXCLUDE_DIRS = [OUTPUT_DIR, LOG_DIR]  # 제외할 디렉토리 목록
EXCLUDE_FILES = ['flatten_and_move.py', 'restore_files.py']  # 제외할 파일 목록

def log_message(log_file, message):
    with open(log_file, 'a') as file:
        file.write(message + "\n")
    print(message)

def flatten_and_move_files(base_dir):
    log_file_path = os.path.join(base_dir, LOG_DIR, f'log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    output_path = os.path.join(base_dir, OUTPUT_DIR)
    os.makedirs(output_path, exist_ok=True)

    for root, dirs, files in os.walk(base_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]  # 제외할 디렉토리 건너뜀
        
        for file in files:
            if file in EXCLUDE_FILES:
                continue  # 제외할 파일 건너뜀

            original_path = os.path.join(root, file)
            new_file_name = os.path.relpath(original_path, base_dir).replace(os.sep, '_')
            new_file_path = os.path.join(output_path, new_file_name)
            
            shutil.move(original_path, new_file_path)
            log_message(log_file_path, f"FilePath: {original_path}\nFlatten: {file} -> {new_file_name}\nMoved: {root} -> {output_path}\n")

if __name__ == "__main__":
    base_dir = '.'  # 이 스크립트의 위치
    flatten_and_move_files(base_dir)
