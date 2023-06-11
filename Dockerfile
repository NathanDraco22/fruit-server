FROM python:alpine

RUN mkdir -p /nathan/app

WORKDIR /nathan

COPY app ./app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD uvicorn app.main:app --host 0.0.0.0 --port 80
