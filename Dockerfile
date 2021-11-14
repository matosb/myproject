# Image de base
FROM ubuntu:20.04

# Mise à jour et installation pip3
RUN apt-get update && apt-get install -y python3-pip

# Création arborescence
RUN mkdir /app
WORKDIR /app

# Copie des fichiers
COPY requirements.txt /app
COPY predict.py /app
COPY clf.pkl /app
COPY test.csv /app

# Création de l'environnement
RUN pip3 install --no-cache-dir -r requirements.txt
