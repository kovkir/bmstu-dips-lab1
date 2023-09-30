FROM python:3.10-alpine

WORKDIR /person

COPY . /person

RUN pip3.10 install -r requirements.txt

# RUN export $(cat .env | xargs)

EXPOSE 8080

CMD ["python3", "app/main.py"]
