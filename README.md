## Este projeto foi feito com:

* [Python 3](https://www.python.org/)
* [Django 3.1.4](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Docker]
* [Postgres]
* [Nginx]


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Inicie os containers
* Rode as migrações.

```
git clone https://github.com/jocsakesley/blog-jocsa-kesley.git
cd blog
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
sudo docker-compose up --build
sudo docker-compose exec web python manage.py migrate
```
