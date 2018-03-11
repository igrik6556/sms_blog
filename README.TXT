Для запуска необходим установленный Python 3 (3.4 или выше),
также нужны утилиты "pip".

Чтобы запустить проект, необходимо выполнить следующие шаги:

1. перейти в директорию, где вы хотите сохранить проект (cd ~/prj)
2. выполнить git clone https://github.com/igrik6556/sms_blog.git
3. python3 -m venv sms_blog_env
   source sms_blog_env/bin/activate
4. cd sms_blog
5. pip3 install -r requirements.txt
6. python3 manage.py runserver
7. открыть в браузере http://localhost:8000/
   Заметки: проект django идет со сформированной базой данных.
   Если вы хотите очистить базу данных. необходимо выполнить следующие шаги:
   	1. rm database.sqlite3
   	2. python3 manage.py migrate
   	Создастся новая база данных.

Есть созданный суперпользователь:
login = admin
pass  = 123superpass

Чтобы запустить тесты, необходимо выполнить команду:
   python3 manage.py test blog
