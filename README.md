# Simple telegram-bot uses django-rest-framework API:

`
https://github.com/kheeva/otus_fs_dz7_django_rest_framework
`

The bot connects to DRF api o the project repo I wrote
upper.
The bot knows `/price` command, it agregates and returns avg price + photo.


# How to install on ubuntu linux

At first you need to download and install python3 if you already haven't: http://python.org .
```buildoutcfg
apt install python3
apt install pip3
```

Install virtualenv:
```buildoutcfg
pip3 install virtualenv 
```
Install git:
```buildoutcfg
apt install git
```

Clone this repo:
```buildoutcfg
cd ~/your_projects_dir
git clone https://github.com/kheeva/otus_telegram_bot_uses_drf
```

Make a virtual env:
```bash
mkdir otus_telegram_bot_uses_drf
cd otus_telegram_bot_uses_drf
virtualenv venv
source venv/bin/activate
```

Install all the modules:
```
pip install -r requirements.txt
```

Create .env file in the root of your_project_dir.
Customize your settings inside .env:
```
DJANGO_SECRET_KEY=your_secret_key
```
Also you can move database settings from settings.py to the .env file.

After that your django software should work.
```buildoutcfg
./manage.py migrate
./manage.py createsuperuser
```

# How to use
Read the documentation and customize settings.

# Testing

Run your DRF server

```
python manage.py runserver 0.0.0.0:8000
```

Connect to telegram

```buildoutcfg
t.me/otus_kheevas_drf_bot
```

Try to get some info

```buildoutcfg
/price python
/price javascript
```

# Project Goals

The code is written for educational purposes. Training courses: otus.ru)
