FROM python:3.10-alpine
# коппируем все из текущей папки в /app контейнера
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
# переменные среды
ENV PYTHONUNBUFFERED=1

# обозначить порт в контенере
EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000