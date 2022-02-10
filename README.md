#скачать и разархивировать проект из репозитория в локальную директорию и войти в нее

# открыть командную строку и убедиться, что установлен pip:
$ pip --version

# если pip не установлен, то в командной строке ввести:
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py

# после установки скопировать путь к установленному pip из командной строки в PATH

# убедиться, что pip установлен:
$ pip help

# установить виртуальное окружение pipenv:
$ pip install pipenv

# запустить pipenv:
$ pipenv shell

# установить django и иные необходимые библиотеки:
$ pipenv install django
$ pipenv install pillow
$ pipenv install taggit
$ pipenv install ...

#запустить проект
