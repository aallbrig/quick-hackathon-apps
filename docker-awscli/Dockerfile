FROM python:latest

# awscli has a hard dependency on something called groff
RUN apt-get update
RUN apt-get install groff -y
# why doesn't awscli take care of this dep on it's own?
# ¯\_(ツ)_/¯

COPY . /scripts
COPY requirements.txt /scripts

WORKDIR /scripts
RUN pip install -r requirements.txt

CMD ["aws", "help"]
