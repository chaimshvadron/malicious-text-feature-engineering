

# Malicious Text Feature Engineering

This project analyzes hostile tweets and performs feature engineering for malicious text detection.

## Local Run

1. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
2. Set environment variables in `.env`:
	```env
	MONGODB_CONNECTION_STRING=...
	MONGODB_DBNAME=...
	```
3. Run the application:
	```bash
	uvicorn app.main:app --reload
	```

## Run with Docker

1. Build the image:
	```bash
	docker build -t malicious-text .
	```
2. Run the container:
	```bash
	docker run --rm -p 8000:8000 -e MONGODB_CONNECTION_STRING=... -e MONGODB_DBNAME=... malicious-text
	```

## Main Files
- `app/` — Application code
- `infra/` — Kubernetes/OpenShift deployment files
- `data/weapon_list.txt` — Weapon list

---
For questions, contact the project maintainer.
