FROM python:3.7-slim

MAINTAINER Thayane Santana <tbdsantana@gmail.com>

COPY . /app_prediction

WORKDIR /app_prediction

RUN apt-get update && \
    apt-get install -y gcc make apt-transport-https \
        ca-certificates \
        cmake \
        build-essential \
        gcc \
        g++ 
	
RUN pip3 install -U scikit-learn scipy matplotlib	
RUN pip install -r --no-cache-dir requirements.txt

# Running Python Application
CMD ["python3", "./app.py"]