# mystat-sdk-python
Проект # mystat-sdk-python работет на плотформе ITStep. Позволяет получить токен авторизации,оценки и расписание студента.

Описание функционала

Авторизация
Функция get_auth(login, password) — выполняет запрос к API и возвращает токен для дальнейших запросов.
Если авторизация неуспешна — возвращает False.

Получение оценок
Функция get_marks(token) — возвращает список оценок студента по переданному токену. Если данные получить не удалось — возвращает False.

Получение расписания
Функция get_schedule(token, type_) — возвращает расписание на неделю или месяц. Параметр type_ может принимать значения "week" или "month". Если данные получить не удалось — возвращает пустой список или словарь.

