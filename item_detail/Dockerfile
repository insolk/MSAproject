FROM python:3.7.9-stretch

RUN apt-get update
RUN pip install django
RUN pip install mysqlclient
RUN apt-get install -y vim
   
COPY /items /items_detail/items
COPY manage.py /items_detail/manage.py
COPY secret.json /items_detail/secret.json
WORKDIR /items_detail

EXPOSE 8000

#CMD ["python", "manage.py","runserver", "172.19.0.3:8000"]