FROM python:latest

# use -e in docker cli commands to populate these values
ENV AWS_ACCESS_KEY_ID="N/A"
ENV AWS_SECRET_ACCESS_KEY="N/A"
ENV AWS_DEFAULT_REGION="us-east-1"
ENV AWS_DEFAULT_OUTPUT="text"

# awscli has a hard dependency on something called groff
RUN apt-get update
RUN apt-get install groff -y
# why doesn't awscli take care of this dep on it's own?
# ¯\_(ツ)_/¯

COPY . /scripts
COPY requirements.txt /scripts

WORKDIR /scripts
RUN pip install -r requirements.txt
ADD . /scripts

CMD ["aws", "ec2", "describe-vpcs"]
