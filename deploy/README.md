# Déploiement Ubuntu / AWS Lightsail

Les fichiers de ce dossier sont des modèles sans secrets. Remplacez `YOUR_STATIC_IP` et `YOUR_DOMAIN` dans la configuration Nginx avant installation.

## Préparer le serveur

Sur l'instance Ubuntu, depuis `/home/ubuntu` :

```bash
sudo apt update
sudo apt install -y python3-venv nginx postgresql postgresql-contrib git

git clone git@github.com:LordBaldwin4/employee-learning.git
cd employee-learning
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/production.txt
```

Créez ensuite `/home/ubuntu/employee-learning/.env` avec des valeurs réelles, sans le committer :

```dotenv
SECRET_KEY=generate-a-long-random-value
ALLOWED_HOSTS=YOUR_STATIC_IP,YOUR_DOMAIN
DATABASE_URL=postgres://project_d_user:CHANGE_THIS_PASSWORD@127.0.0.1:5432/project_d
DEFAULT_FROM_EMAIL=verified@example.com
SENDGRID_API_KEY=CHANGE_THIS_SECRET
```

## PostgreSQL

```bash
sudo -u postgres psql
```

```sql
CREATE USER project_d_user WITH PASSWORD 'CHANGE_THIS_PASSWORD';
CREATE DATABASE project_d OWNER project_d_user;
\q
```

Le mot de passe SQL doit être identique à celui de `DATABASE_URL`. Ne réutilisez pas l'exemple tel quel.

## Django

```bash
source venv/bin/activate
python manage.py migrate --settings=config.settings.production
python manage.py createsuperuser --settings=config.settings.production
sudo mkdir -p /usr/share/nginx/html/static
sudo chown -R ubuntu:www-data /usr/share/nginx/html/static
python manage.py collectstatic --noinput --settings=config.settings.production
```

## Gunicorn et Nginx

```bash
sudo cp deploy/project_d.socket /etc/systemd/system/
sudo cp deploy/project_d.service /etc/systemd/system/
sudo cp deploy/nginx-project_d.conf /etc/nginx/sites-available/project_d
sudo ln -s /etc/nginx/sites-available/project_d /etc/nginx/sites-enabled/project_d
sudo rm -f /etc/nginx/sites-enabled/default
sudo systemctl daemon-reload
sudo systemctl enable --now project_d.socket
sudo systemctl enable --now project_d.service
sudo nginx -t
sudo systemctl reload nginx
```

Contrôles utiles :

```bash
systemctl status project_d.service
journalctl -u project_d.service -n 100 --no-pager
curl -I http://127.0.0.1/
```

## Pare-feu et HTTPS

Autorisez d'abord SSH avant d'activer UFW :

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

Après avoir configuré le DNS vers l'IP statique :

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d YOUR_DOMAIN
sudo certbot renew --dry-run
```

Les clés OAuth GitHub/Google, le domaine du site et les paramètres SendGrid doivent être configurés séparément dans leurs consoles respectives. Ils ne doivent jamais être écrits dans Git.
