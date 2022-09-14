# docker-app

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru
https://django.fun/tutorials/dokerizaciya-django-s-pomoshyu-postgres-gunicorn-i-nginx/


#### $ docker compose up -d --build 
#### $ netstat -ntpl  перевірка портів
$ docker-compose down -v, щоб видалити тома вместе с контейнерами. 

$ docker container prune  # delete all stopped containers


#### $ docker compose exec MY_web_services_name  python manage.py migrate --noinput 

зайти на PostgresQL:
#### $ docker compose exec db psql --username=postgres --dbname=hello_django_dev
 ###### команди всередині:
 ###### # psql (14.5 (Debian 14.5-1.pgdg110+1))
 ###### # my_db_hello_django_dev # \l  - List of databases
 ###### #\help


XML, в переводе с англ eXtensible Markup Language — расширяемый язык разметки. Используется для хранения и передачи данных. Так что увидеть его можно не только в API, но и в коде. Этот формат рекомендован Консорциумом Всемирной паутины (W3C), поэтому он часто используется для передачи данных по API.
https://rider-support.jetbrains.com/hc/en-us/articles/207097529-What-is-the-idea-folder-