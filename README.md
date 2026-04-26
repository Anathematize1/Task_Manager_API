# Task Manager API
REST API для управления задачами с авторизацией пользователей.

## 🚀 Функциональность:
  - регистрация пользователей
  - JWT-аутентификация
  - CRUD задач
  - доступ только к своим задачам
  - фильтрация (status, priority)
  - поиск
  - сортировка
  - пагинация

## 🛠 Стек:
  - Python
  - Django
  - Django REST Framework
  - SQLite / PostgreSQL
  - JWT

## ⚙️ Запуск:

  ```bash
  git clone <repo>
  cd project
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
  ```


## 📡 Эндпоинты:
  Регистрация
 
  ```POST /api/auth/register/```
  
  **Body:**
  ```json
  {
    "username": "ivan",
    "email": "ivan@example.com",
    "password": "strongpass123",
    "password2": "strongpass123"
  }
  ```
  Получение токена (логин)
  
  ```POST /api/auth/login/```
  
  Body:
  
  ```{
    "username": "ivan",
    "password": "strongpass123"
  }
  ```
  Обновление токена
  
  ```POST /api/auth/refresh/```

📝 Задачи

Все эндпоинты, кроме register требуют авторизацию
Header:

Authorization: Bearer <access_token>
Получить список задач

```GET /api/tasks/```

Query параметры:

  status - фильтр по статусу
  priority — фильтр по приоритету
  search — поиск по названию и описанию
  ordering — сортировка

Пример:

```GET /api/tasks/?status=done&ordering=-created_at```
Создать задачу

```POST /api/tasks/```

```Body:

{
  "title": "Сделать резюме",
  "description": "Подготовка к стажировке",
  "status": "new",
  "priority": "high"
}
```
Получить задачу

```GET /api/tasks/{id}/```

Обновить задачу (частично)

```PATCH /api/tasks/{id}/```

Удалить задачу

```DELETE /api/tasks/{id}/```

📄 Пагинация

```GET /api/tasks/?page=2```

Пример ответа:

```{
  "count": 20,
  "next": "...",
  "previous": "...",
  "results": [...]
}
```


  📌 Особенности:
  
  - реализовано разграничение доступа
  - используются query params для фильтрации
  - реализована пагинация


