# api_yatube
api_yatube
Описание проекта
Yatube API — это бэкенд для социальной сети, позволяющий пользователям создавать посты, комментировать их и взаимодействовать с группами.

Как развернуть
Клонируйте репозиторий.
Создайте и активируйте виртуальное окружение.
Установите зависимости из requirements.txt.
Выполните миграции: python manage.py migrate.
Запустите сервер: python manage.py runserver.

Примеры запросов
Добавление нового поста:

POST /api/v1/posts/
Authorization: Token <ваш_токен>
Content-Type: application/json

{
    "text": "Текст поста",
    "group": 1
}

Ответ:

{
    "id": 1,
    "text": "Текст поста",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
Получение списка всех постов:

GET /api/v1/posts/
Authorization: Token <ваш_токен>
Ответ:

[
    {
        "id": 1,
        "text": "Текст поста 1",
        "author": "anton",
        "group": 1,
        "pub_date": "2021-06-01T08:47:11.084589Z"
    },
    {
        "id": 2,
        "text": "Текст поста 2",
        "author": "ivan",
        "group": 2,
        "pub_date": "2021-06-02T09:00:00.000000Z"
    }
]
Получение информации о посте:

GET /api/v1/posts/1/
Authorization: Token <ваш_токен>
Ответ:

{
    "id": 1,
    "text": "Текст поста 1",
    "author": "anton",
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
Редактирование поста:

PUT /api/v1/posts/1/
Authorization: Token <ваш_токен>
Content-Type: application/json

{
    "text": "Обновленный текст поста",
    "group": 1
}
Ответ:

{
    "id": 1,
    "text": "Обновленный текст поста",
    "author": "anton",
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
Удаление поста:

DELETE /api/v1/posts/1/
Authorization: Token <ваш_токен>
Ответ:

{
    "detail": "Удалено успешно"
}
Получение списка всех групп:

GET /api/v1/groups/
Ответ:

[
    {
        "id": 1,
        "title": "Группа 1",
        "slug": "group-1",
        "description": "Описание группы 1"
    },
    {
        "id": 2,
        "title": "Группа 2",
        "slug": "group-2",
        "description": "Описание группы 2"
    }
]
Получение информации о группе:

GET /api/v1/groups/1/
Ответ:

{
    "id": 1,
    "title": "Группа 1",
    "slug": "group-1",
    "description": "Описание группы 1"
}
Добавление комментария к посту:

POST /api/v1/posts/1/comments/
Authorization: Token <ваш_токен>
Content-Type: application/json

{
    "text": "Это тестовый комментарий"
}
Ответ:

{
    "id": 1,
    "author": "anton",
    "post": 1,
    "text": "Это тестовый комментарий",
    "created": "2021-06-01T10:14:51.388932Z"
}
Получение списка комментариев к посту:

GET /api/v1/posts/1/comments/
Ответ:

[
    {
        "id": 1,
        "author": "anton",
        "post": 1,
        "text": "Это тестовый комментарий",
        "created": "2021-06-01T10:14:51.388932Z"
    },
    {
        "id": 2,
        "author": "ivan",
        "post": 1,
        "text": "Другой комментарий",
        "created": "2021-06-01T10:20:00.000000Z"
    }
]
Редактирование комментария:

PUT /api/v1/posts/1/comments/1/
Authorization: Token <ваш_токен>
Content-Type: application/json

{
    "text": "Обновленный текст комментария"
}
Ответ:

{
    "id": 1,
    "author": "anton",
    "post": 1,
    "text": "Обновленный текст комментария",
    "created": "2021-06-01T10:14:51.388932Z"
}
Удаление комментария:

DELETE /api/v1/posts/1/comments/1/
Authorization: Token <ваш_токен>
Ответ:

{
    "detail": "Удалено успешно"
}