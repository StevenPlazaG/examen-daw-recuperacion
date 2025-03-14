# Imagen base
FROM python:3.11

# Crear directorio de la app
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar el código de la app
COPY app/ .

# Instalar supervisor
RUN apt-get update && apt-get install -y supervisor

# Copiar configuración de Supervisor
COPY supervisor/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# Exponer el puerto
EXPOSE 5000

# Comando para iniciar Supervisor
CMD ["/usr/bin/supervisord", "-n"]