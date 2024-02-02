# FileFlattener-and-Restorer

이 프로젝트는 다양한 경로에 퍼져있는 파일들을 단순화하고 정리하는 파이썬 스크립트를 제공합니다. 스크립트는 파일 이름을 변경하고, 지정된 출력 디렉토리로 파일을 이동시키며, 작업 로그를 기록합니다.
또한 원래 경로로 복원이 가능한 스크립트를 제공합니다.

## 기능

- **파일 평탄화 및 이동**: 지정된 디렉토리 내의 모든 파일을 스캔하고, 파일 이름을 변경하여 지정된 출력 디렉토리로 이동시킵니다.
- **원본 경로 복원**: 변경된 파일 이름을 사용하여 원본 디렉토리 구조로 파일을 복원합니다.
- **로그 기록**: 모든 작업에 대한 로그를 `Logs` 디렉토리에 기록합니다.

## 사용 방법

<p align="center">
  <img src="https://github.com/EcchiClone/FileFlattener-and-Restorer/assets/21221633/e139cf7c-7ffe-41dc-85c0-6b369c52e2d3"> ▷ flatten_and_move ▷ <img src="https://github.com/EcchiClone/FileFlattener-and-Restorer/assets/21221633/a2f1d53c-b836-4093-9039-6b4b5be3cfc4"> ▷ restore_files ▷ <img src="https://github.com/EcchiClone/FileFlattener-and-Restorer/assets/21221633/77e02d17-a942-4de4-84eb-97942cb7f164">
</p>

이 리포지토리를 클론하거나 직접 압축파일을 다운로드 받아 파일정리를 원하는 곳으로 위치시킨 후에 실행시켜 사용합니다.

> **폴더 경로의 구분자(\) 를 언더바(_)로 치환하여 바뀌어질 파일이름으로 사용하기 때문에**

> **원래의 파일명에 언더바가 섞여있는 경우 오작동을 일으킬 가능성이 매우 크며, 특히 원래 경로로 복원이 어렵습니다!!!**

_(현재 구현하지는 않았으나, 로그파일을 참조하는 방식으로 위 문제를 해결 할 수 있을 것으로 보입니다)_

![image](https://github.com/EcchiClone/FileFlattener-and-Restorer/assets/21221633/0969a1db-eae3-4cec-b1e5-d471ef2d72b3)

위와 같이 해당 폴더의 주소창에 cmd를 입력하여 명령 프롬프트를 실행합니다.

### 파일 평탄화 및 이동

`flatten_and_move.py` 스크립트를 실행하여, 현재 디렉토리 및 하위 디렉토리에 있는 모든 파일을 `flatten` 디렉토리로 이동시키고 이름을 변경합니다.

```
python flatten_and_move.py
```

### 원본 경로로 파일 복원

`restore_files.py` 스크립트를 실행하여, `flatten` 디렉토리에 있는 파일을 원래의 디렉토리 구조로 복원합니다.

```
python restore_files.py
```

## 기여 방법

풀 리퀘스트 또는 이슈 등록 환영합니다.
