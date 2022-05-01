import os
from typing import Iterator
import re
from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def build_query(it: Iterator, cmd: str, value: str) -> Iterator:
    res = map(lambda v: v.strip(), it)
    if cmd == "filter":
        return filter(lambda v: value in v, it)
    if cmd == "map":
        arg = int(value)
        return map(lambda v: v.split(" ")[value], it)
    if cmd == "unique":
        return iter(set(res))
    if cmd == "sort":
        reverse = value == "desc"
        return iter(sorted(res, reverse=reverse))
    if cmd == "limit":
        return get_limit(it, int(value))
    if cmd == "regex":
        regex = re.compile(value)
        return filter(lambda v: regex.findall(v), it)
    return it


def get_limit(it: Iterator, value: int) -> Iterator:
    i = 0
    for item in it:
        if i < value:
            yield item
        else:
            break
        i += 1


@app.post("/perform_query")
def perform_query() -> str:
    try:
        cmd1 = request.args["cmd1"]
        cmd2 = request.args["cmd2"]
        value1 = request.args["value1"]
        value2 = request.args["value2"]
        file_name = request.args["file_name"]
    except KeyError:
        raise BadRequest

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return str(BadRequest(description=f"{file_name} does not exist"))

    with open(file_path) as fp:
        res = build_query(fp, cmd1, value1)
        res = build_query(res, cmd2, value2)
        content = '\n'.join(res)

    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    return str(app.response_class('', content_type="text/plain"))
