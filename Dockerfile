# Usa un'immagine base Python
FROM python:3.12-slim-bullseye

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Imposta le variabili d'ambiente (buona pratica)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copia i file di dipendenza e installali
# Questo passo è fatto separatamente per sfruttare la cache di Docker
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice del progetto Django nel container
COPY . /app/

# Espone la porta su cui Gunicorn ascolterà (la porta interna al container)
EXPOSE 8000

# Comando per avviare l'applicazione con Gunicorn
# 'mysite.wsgi:application' deve corrispondere al percorso del tuo file wsgi.py
# Se il tuo progetto Django principale si chiama 'mysite', questo è corretto.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]