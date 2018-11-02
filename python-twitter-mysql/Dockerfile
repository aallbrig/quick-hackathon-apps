FROM python:latest

ENV TWITTER_TOKEN="N/A"
ENV TWITTER_TOKEN_SECRET="N/A"
ENV TWITTER_CONSUMER_KEY="N/A"
ENV TWITTER_CONSUMER_SECRET="N/A"

ENV DB_HOST="N/A"
ENV DB_PORT="N/A"
ENV DB_USER="N/A"
ENV DB_PASS="N/A"

RUN mkdir -p /scripts
WORKDIR /scripts

COPY ./requirements.txt /scripts/requirements.txt
RUN pip install -r requirements.txt

CMD python app.py

