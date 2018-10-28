### Notes
- PyCharm's command line shortcut is `charm`
- PyCharm allows you to add docker so you can debug a script directly. Read more [here](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html)
- You can run one-off commands using generic docker containers (e.g. `python`)
    - `docker run -it -v $(pwd):/scripts aallbrig/docker-python-debug bash -c "python /scripts/test.py"`
    - `docker run -it -v $(pwd):/scripts aallbrig/docker-python-debug bash -c "python /scripts/app.py"`
    - `docker run -it -v $(pwd):/scripts aallbrig/docker-python-debug bash -c "pip install twitter; pip freeze > requirements.txt"`
    - `docker run -it -v $(pwd):/scripts aallbrig/docker-python-debug bash -c "pip install virtualenv; pip freeze >> requirements.txt"`

