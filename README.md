# helloflask1
## How to run this locally
- clone this repo
- ```cd flask_app```
- ```rm -rf .git/```
- ```python virtualenv.py --no-site-packages venv```

### Install Dependencies
- ```pip install -r requirements.txt``

### Activate Virtual Env
- ```source venv/bin/activate```

### Run app on localhost
- ```python run.py```

---

## Deploying To Heroku
- replace app_name with your project name
  -```heroku create app_name -s cedar```

- push app to heroku
  -```git push heroku master```
  -``` heroku scale web=1```
- check heroku is running
  -```heroku ps```

- view application online
  -```heroku open```
