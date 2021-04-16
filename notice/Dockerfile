FROM python:3.7.9-stretch

RUN apt-get update
RUN pip install django
RUN pip install mysqlclient
RUN apt-get install -y vim

WORKDIR /mydjango
COPY ./ /mydjango

# RUN python manage.py makemigrations
# RUN python manage.py migrate

#EXPOSE 8000
#
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]