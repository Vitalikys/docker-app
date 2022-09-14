# docker-app

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru

https://django.fun/tutorials/dokerizaciya-django-s-pomoshyu-postgres-gunicorn-i-nginx/


$ docker compose up -d --build
$ netstat -ntpl  перевірка портів
$ docker-compose down -v, чтобы удалить тома вместе с контейнерами. 
$ docker container prune  # delete all stoped containers


$ docker compose exec MY_web_services_name  python manage.py migrate --noinput 

зайти на PostgresQL
$ docker compose exec db psql --username=postgres --dbname=hello_django_dev
 #psql (14.5 (Debian 14.5-1.pgdg110+1))
 #my_db_hello_django_dev # \l  - List of databases
        #\help
