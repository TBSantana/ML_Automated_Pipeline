FROM python:3.6-slim
WORKDIR /app

COPY transform_data/requirements.txt .

RUN pip install -r requirements.txt

COPY transform_data .

COPY data ./data

CMD ["python3", "./transform_data.py", "$(pwd)"]