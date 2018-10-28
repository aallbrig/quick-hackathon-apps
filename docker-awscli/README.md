### Notes

1. First ran `docker run -v $(pwd):/scripts -it python bash -c "cd /scripts && pip install awscli; pip freeze > requirements.txt"` to populate a `requirements.txt` with `awscli` dependency
1. Created `Dockerfile` afterwards; based on `python:latest` and filled with basic commands to install from `requirements.txt`
1. Ran `docker build . -t aallbrig/docker-awscli` to build out image
1. Test main command `pip freeze` in `Dockerfile`

    ```bash
    docker run aallbrig/docker-awscli
    ```
1. Enjoy!

That concludes the initial "set up" instructions