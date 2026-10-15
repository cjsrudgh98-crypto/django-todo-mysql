# Django Todo (MySQL)

할 일 등록 · 목록 · 수정 · 삭제(CRUD)와 완료 체크 기능을 제공하는 Django + MySQL 프로젝트입니다.

## 기능
- Todo 모델: `title`(필수), `content`(선택), `is_completed`(기본 False), `created_at`(자동)
- 목록에서 체크 버튼으로 완료/미완료 전환, 완료 항목은 취소선 + 배경색 표시
- 등록/수정 시 유효성 검사 및 에러 메시지 출력
- Django admin에서 Todo 관리

## 실행 방법
```bash
pip install -r requirements.txt
cp .env.example .env        # DB 비밀번호 등 값 수정
```
MySQL에서 데이터베이스 생성:
```sql
CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Todo 목록: http://127.0.0.1:8000/
- 관리자: http://127.0.0.1:8000/admin/

> Django 5.2 LTS 사용 (MySQL 8.0 지원). DB 드라이버는 PyMySQL.
