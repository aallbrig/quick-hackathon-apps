FROM python:latest

COPY . /scripts
COPY requirements.txt /scripts

WORKDIR /scripts
RUN pip install -r requirements.txt

CMD ["pip", "freeze"]
