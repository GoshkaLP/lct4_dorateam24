FROM python:3.11-buster

WORKDIR /usr/src/app

EXPOSE 8000

ADD ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . /usr/src/app/

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000