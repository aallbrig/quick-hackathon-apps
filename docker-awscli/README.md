### Notes

##### Getting Started
1. First ran `docker run -v $(pwd):/scripts -it python bash -c "cd /scripts && pip install awscli; pip freeze > requirements.txt"` to populate a `requirements.txt` with `awscli` dependency
1. Created `Dockerfile` afterwards; based on `python:latest` and filled with basic commands to install from `requirements.txt`
1. Ran `docker build . -t aallbrig/docker-awscli` to build out image
1. Test main command `pip freeze` in `Dockerfile`

    ```bash
    docker run aallbrig/docker-awscli
    ```
1. Enjoy!

That concludes the initial "set up" instructions

##### Running AWSCLI
Plenty has changed since the initial "getting started" `Dockerfile`. To work with this new container, build it up then...

... _ASSUMING_ you have a ~/.aws config profile and you have awscli installed on your host machine...

Set these variables
```bash
AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id) \
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key) \
AWS_DEFAULT_REGION=$(aws --profile default configure get region) \
AWS_DEFAULT_OUTPUT=$(aws --profile default configure get output)
```

Run run the docker container while passing those values in
```bash
docker run -it --rm \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
  -e AWS_DEFAULT_OUTPUT=$AWS_DEFAULT_OUTPUT\
  aallbrig/docker-awscli bash
```