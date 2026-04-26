# Task Manager API
REST API для управления задачами с авторизацией пользователей.

## 🚀 Функциональность
  - регистрация пользователей
  - JWT-аутентификация
  - CRUD задач
  - доступ только к своим задачам
  - фильтрация (status, priority)
  - поиск
  - сортировка
  - пагинация

## 🛠 Стек
  - Python
  - Django
  - Django REST Framework
  - SQLite / PostgreSQL
  - JWT

## ⚙️ Запуск

  ```bash
  git clone <repo>
  cd project
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

