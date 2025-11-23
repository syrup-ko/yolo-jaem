# YOLO-JAEM (Minimum Viable Product)

자산(Stock, HYSA, 부동산)의 수익률 비교 및 시뮬레이션을 제공하는 풀스택 프로젝트의 초기 스캐폴드입니다.

## 구성
- frontend: Next.js(App Router, TypeScript) 기반 UI
- backend: FastAPI 기반 API, 시뮬레이션 엔진, Redis 캐시, TimescaleDB(PostgreSQL) 대상
- docker-compose: 개발용 Redis, TimescaleDB  // MVP 단계에서는 사용 X

## 빠른 시작
1) Backend (가상환경 권장)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

2) Frontend
```bash
cd frontend
npm install
npm run dev
```

3) Docker 리소스 기동 (docker가 설치되어 있어야 함. 25.11.23일 현재는 테스트 안해봄)
```bash
docker compose up -d

# 확인
docker compos ps

# 종료
docker compose down
```
- 해당 명령어 실행 시 Redis 컨테이너 실행, TimescaleDB 컨테이너 실행 됨
- redis://localhost:6379
- postgresql://postgres:yourpassword@localhost:5432/yolo_jaem   (DB명: yolo_jaem, 계정: postgres / yourpassword)
## 환경 변수
루트에 `.env` 또는 각 패키지에 `.env.*` 사용을 권장합니다. 예시는 다음을 참고하세요.
```
cp .env.example .env
```

## 테스트
```bash
cd backend
pytest -q
```

## 폴더 개요
- frontend/src/app: 페이지 엔트리(App Router)
- backend/app: API/서비스/시뮬레이션/데이터/스키마/유틸

