#  Приложение для вывода данных из БД в браузер

## Краткое описание проекта

Приложение выводит данные из БД в браузер в двух форматах: таблица и график

### Технологии

- Python 3.10.6
- Flask 2.0.2
- Jinja2 3.1.2
- SQLAlchemy 1.4.0
- SQLite

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:son13425/data_output_to_the_browser.git
```

```
cd data_output_to_the_browser
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить приложение:

```
flask run
```

### Автор
[Оксана Широкова](https://github.com/son13425)


## Лицензия
Проект выпущен под лицензией [MIT](https://github.com/son13425/data_output_to_the_browser/blob/main/COPYING.txt)