# Сервер новостного блога.

### Настройка проекта:
- Создать проект на локальном компьютере.
- Склонировать репозиторий
```angular2html
$ git init
$ git clone https://github.com/akorsunov23/news_blog
```
- Перейти в папку склонированного проекта
```angular2html
$ cd news_blog
```
- Добавить в корень проекта файл '.env' и указать в нём переменные согласно инструкциям '.env.template' 
- Запустить контейнеризацию, командой
````
$ docker-compose build 
````
- Запустить проект
````
$ docker-compose up -d #в фоновом режиме
$ docker-compose up    #в детальном режиме 
````
- Для остановки проекта, использовать следующую команду.
````
$ docker-compose down
````

После проделанных действий, проект будет доступен по адресу 'http://localhost:8000/' с использованием web сервера от gunicorn.

#### Проект доступен на удалённом хостинге по адресу http://apptrix.beget.tech

## Доступные АPI методы:

На локальном и удалённом сервере доступны следующие API методы:
- POST (регистрация пользователя)
```angular2html
/api/v1/users/register/
```
- POST (аутентификация пользователя)
```angular2html
/api/v1/users/login/
```
- GET (получения списка всех новостей с пагинацией)
```angular2html
/api/v1/news/
```
- POST (добавление новости для аутентифицированного пользователя)
```angular2html
/api/v1/news/create/
```
- PUT, DELETE (редактирование и удаление новости, с проверкой на наличие прав)
```angular2html
/api/v1/news/<news_id>/
```
- GET (получение списка всех комментариев к новости)
```angular2html
/api/v1/news/<news_id>/comments/
```
- POST (добавление комментариев)
```angular2html
/api/v1/news/comment/create/
```
- DELETE (удаление комментария, с проверкой на наличие прав)
```angular2html
/api/v1/news/<news_id>/comments/<comment_id>/
```
- POST (оценка новости)
````angular2html
/api/v1/news/<news_id>/like/
````

