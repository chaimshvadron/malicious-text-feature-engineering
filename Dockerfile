FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY hostile-tweets-ex ./hostile-tweets-ex

CMD ["uvicorn", "hostile-tweets-ex.app.main:app", "--host", "0.0.0.0", "--port", "8000"]