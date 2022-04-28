# Урок 24. Типизация и дополнительные темы. Домашнее задание

Привет! Это Саша. Сегодня потренируемся использовать регулярные выражения, писать код с тайпингами и датаклассами. В задаче ниже нужно **дополнить домашнее задание с предыдущего урока**.

![Снимок экрана 2021-12-21 в 17.34.23.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c6a2ccf-b133-45e8-84d6-5c20c4f67717/Снимок_экрана_2021-12-21_в_17.34.23.png)

## Задача

Усовершенствовать язык программирования и добавить команду — regex.

## Регулярные выражения

Допустим, у вас есть лог-файл работы веб-сервера:

```python
1.181.2.178 [17/May/2015:20:05:36] "GET / HTTP/1.1" 200
1.125.2.148 [17/May/2015:20:05:19] "GET /?flav=rss20 HTTP/1.1" 200
1.170.2.204 [17/May/2015:20:05:03] "POST /?flav=atom HTTP/1.1" 200
1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200
1.163.30.77 [17/May/2015:20:05:37] "GET /blog/dot.html HTTP/1.1" 200
```

Рассмотрим команду **cmd1=regex value1=<regex>**

Команда regex принимает в качестве аргумента регулярное выражение, по которой нужно будет фильтровать строки входных данных. В результате выполнения команды **cmd1=regex value1=images\/\w+\.png** (запросы в виде images/*.png, то есть получить запросы на картинки png) должно быть выведено:

```python
1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200
```

## Типизация

После выполнения предыдущего пункта нужно внедрить типизацию в ваш проект. Необходимо добиться, чтобы команда mypy выполнялась без ошибок.

Исходное состояние проекта при запуске mypy:

```python
lesson24_project_solution % mypy app.py
app.py:12: error: Function is missing a type annotation
app.py:37: error: Function is missing a return type annotation
Found 2 errors in 1 file (checked 1 source file)
```

Исходное состояние:

```python
lesson24_project_solution % mypy app.py
app.py:12: error: Function is missing a type annotation
app.py:37: error: Function is missing a return type annotation
Found 2 errors in 1 file (checked 1 source file)
```

## Шаблон для выполнения задания

[https://github.com/skypro-008/lesson24_project_source](https://github.com/skypro-008/lesson24_project_source)

## Проверьте себя

- [ ]  Добавлена команда regex.
- [ ]  Запрос возвращает только логи получения картинок png.
- Ниже подсказка. Скрипт, который правильно отправляет данные. Ваш сервер должен принимать такой запрос
    
    ```python
    import requests
    url = "http://127.0.0.1:5000/perform_query"
    payload = {
       'file_name': 'apache_logs.txt',
       'cmd1': 'regex',
       'value1': 'images/\\w+\\.png',
       'cmd2': 'sort',
       'value2': 'asc'
    }
    response = requests.request("POST", url, data=payload)
    print(response.text)
    ```
    
    100.43.83.137 - - [17/May/2015:12:05:05 +0000] "GET /images/proofsocietyisdoomed.png HTTP/1.1" 304 - "-" "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    
    100.43.83.137 - - [17/May/2015:16:05:53 +0000] "GET /presentations/logstash-puppetconf-2012/images/trollface.png HTTP/1.1" 304 - "-" "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)
    
- [ ]  Команда **mypy app.py** выполняется без ошибок.