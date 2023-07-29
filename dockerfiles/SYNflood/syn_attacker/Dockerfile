FROM ubuntu:latest

WORKDIR /app

# Mise à jour et installation des dépendances nécessaires
RUN apt-get update \
    && apt-get install -y git python3 python3-pip

# Clonage du référentiel
RUN git clone https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool.git \
    && cd Python-SYN-Flood-Attack-Tool

# Copie du fichier requirements.txt
COPY requirements.txt /app/Python-SYN-Flood-Attack-Tool/requirements.txt
COPY notes.txt /app/notes.txt

# Installation des dépendances Python
RUN pip3 install --upgrade pip \
    && pip3 install -r /app/Python-SYN-Flood-Attack-Tool/requirements.txt

# Reste de la configuration de votre image Docker

CMD ["/bin/bash"]


