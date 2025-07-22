# Usa un'immagine base Python
FROM python:3.12-slim-bullseye

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Imposta le variabili d'ambiente (buona pratica)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Aggiorna i pacchetti e installa gli strumenti di compilazione E le intestazioni di sviluppo di Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia i file di dipendenza e installali
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice del progetto Django nel container
COPY . /app/

# Espone la porta su cui Gunicorn ascolterà (la porta interna al container)
EXPOSE 8000

# Comando per avviare l'applicazione con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]