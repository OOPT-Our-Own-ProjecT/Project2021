# 명령어 정리

## _1. GIT_
---
- git branch [브랜치명] : 브랜치 생성
- git checkout [브랜치명] : 브랜치 이동
- git checkout -b [브랜치명] [연결하고 싶은 브랜치 - 기본 값 main] : 브랜치 생성 후 checkout
- git remote update : 로컬 저장소 브랜치 업데이트
---
- git pull origin [브랜치명] : 해당 브랜치 원격 저장소 데이터 가져오기
- git status : 로컬 저장소 상태 확인
- git add . : 바뀐 상태 저장
- git commit -m "커밋 메세지" : 커밋
- git push origin [브랜치명] : 해당 브랜치 원격 저장소 값 변경
---

## _2. Frontend (Vue.js)_
---
- npm i : pakage.json을 통해 필요한 모듈 설치
- npm run serve : 프론트엔드 서버 열기
- npm run build : 배포 패키지 생성 (dist 폴더 생성)
---
## _3. Backend (Django)_
---
- cd env : env 폴더로 이동
- Scripts\activate.bat : windows 운영체제 기반 가상 환경 들어가기
- (env) C:\users\~~ : 가상환경 접속 시 보이는 화면 (확인 필수)
---
- pip freeze > requirements.txt : 설치한 모듈 문서화
- pip install -r requirements.txt : 필요 모듈 설치
- python manage.py makemigrations : db 테이블 변경 시 해당 app 단의 migrations을 변경하는 작업
- python manage.py migrate : 최신 버전 migrations 을 통해 db 단 변경
- python manage.py runserver : 백엔드 서버 열기
- python manage.py startapp [app명] : app 단위 만들기
---
