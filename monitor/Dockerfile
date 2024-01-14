FROM ubuntu:latest

LABEL authors="corentinlaval"

RUN apt-get update && \
    apt-get install -y python3 python3-pip nodejs npm && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN npm install
RUN npm run build

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "monitor.wsgi:application"]

