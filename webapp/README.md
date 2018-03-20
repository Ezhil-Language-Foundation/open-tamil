Open Tamil Web Interface



git clone https://github.com/Ezhil-Language-Foundation/open-tamil.git

cd open-tamil/webapp

sudo pip install -r requirements.txt

python manage.py runserver

# for tamil translation of website

add to template {% trans "this is example" %}

then put - python manage.py makemessages -l "ta"

edit translation file

open-tamil/webapp/locale/ta/LC_MESSAGES/django.po


msgid "this is example"

msgstr "இது எடுத்துக்காட்டு"

then put following command

python manage.py compilemessages
