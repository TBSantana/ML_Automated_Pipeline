FROM python:3.6-slim
WORKDIR /app

COPY clean_data/requirements.txt .

RUN pip install -r requirements.txt

COPY clean_data .

COPY data ./data

CMD ["python3", "./clean_data.py", "$(pwd)"]
