## Este projeto foi feito com:

* [Python 3](https://www.python.org/)
* [Django 3.1.4](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* Docker
* Postgres
* Nginx


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Instale o docker e docker compose.
* Inicie os containers.
* Rode as migrações.

```
git clone https://github.com/jocsakesley/blog-jocsa-kesley.git
cd blog
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker-compose up --build
sudo docker-compose exec web python manage.py migrate
```
