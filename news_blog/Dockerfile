# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /news_blog
# Копирует все файлы из нашего локального проекта в контейнер
COPY requirements.txt /news_blog/
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt
# копируем содержимое текущей папки в контейне
COPY . .