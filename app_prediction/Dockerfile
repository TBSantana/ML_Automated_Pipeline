FROM python:3.6-slim
WORKDIR /app

COPY app_prediction/requirements.txt .

RUN pip install -r requirements.txt

COPY app_prediction .

COPY data ./data
	
CMD ["python3", "./app.py"]