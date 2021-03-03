FROM python:3.6-slim
WORKDIR /app

COPY train_model/requirements.txt .

RUN pip install -r requirements.txt

COPY train_model .

COPY data ./data

CMD ["python3", "./train_model.py", "$(pwd)"]