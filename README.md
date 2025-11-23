# YOLO-JAEM (MVP)

자산(Stock, HYSA, 부동산)의 수익률 비교 및 시뮬레이션을 제공하는 풀스택 프로젝트의 초기 스캐폴드입니다.

## 구성
- frontend: Next.js(App Router, TypeScript) 기반 UI
- backend: FastAPI 기반 API, 시뮬레이션 엔진, Redis 캐시, TimescaleDB(PostgreSQL) 대상
- docker-compose: 개발용 Redis, TimescaleDB

## 빠른 시작
1) Docker 리소스 기동
```bash
docker compose up -d
```

2) Backend (가상환경 권장)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

3) Frontend
```bash
cd frontend
npm install
npm run dev
```

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



