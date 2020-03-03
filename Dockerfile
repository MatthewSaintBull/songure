FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
    
COPY ./app ./app
COPY ./test ./test

CMD [ "uvicorn", "app.main:app", "--reload", "--port", "8080", "--host", "0.0.0.0" ]
EXPOSE 8080/tcp