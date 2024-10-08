# Utiliser l'image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY app.py requirements.txt /app/
COPY templates /app/templates

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 1010
EXPOSE 1010

# Démarrer l'application
CMD ["python", "app.py"]
