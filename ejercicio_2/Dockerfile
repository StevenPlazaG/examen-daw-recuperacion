FROM python:3.11

WORKDIR /app

COPY requeriments.txt requeriments.txt

RUN pip install -r requeriments.txt

COPY /app .

RUN apt-get update && apt-get install -y supervisor

COPY supervisor/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

EXPOSE 5000

CMD ["usr/bin/supervisor", "-n"]