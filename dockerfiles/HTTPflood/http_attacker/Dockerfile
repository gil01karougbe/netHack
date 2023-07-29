FROM ubuntu:latest

WORKDIR /app

# Mise à jour et installation des dépendances nécessaires
RUN apt-get update \
    && apt-get install -y git curl build-essential
COPY notes.txt /app/notes.txt
# Installation de Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && /root/.cargo/bin/rustup update

# Clonage du référentiel lor-axe
RUN git clone https://github.com/ajmwagar/lor-axe.git \
    && cd lor-axe

# Compilation et installation de lor-axe
RUN /root/.cargo/bin/cargo install --path lor-axe

COPY notes.txt /app/lor-axe/notes.txt
# Exécution de lor-axe avec les paramètres spécifiés
CMD ["/root/.cargo/bin/loraxe", "192.168.2.10", "-p", "8080", "-s", "200"]

