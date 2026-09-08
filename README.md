# Employee Learning Hub

Employee Learning Hub est une application Django de gestion des formations suivies par des employés. Elle permet de créer un catalogue de cours, d'associer des employés aux cours et de consulter ou modifier ces inscriptions dans une interface web.

## Problème traité

Les inscriptions aux formations sont souvent dispersées entre des fichiers ou des échanges informels. Ce projet centralise les divisions, les employés, leurs informations personnelles et les cours dans un modèle relationnel simple.

## Fonctionnalités

- affichage d'une page d'accueil ;
- authentification par adresse e-mail avec django-allauth ;
- liste des cours triée par titre ;
- détail d'un cours et de ses employés inscrits ;
- création, modification et suppression d'un cours ;
- administration des divisions, employés, informations personnelles et cours ;
- interface responsive basée sur Bootstrap et un thème beige/marron.

## Choix techniques

- **Django** fournit le modèle MVC, l'ORM, l'administration et les vues génériques CRUD ;
- **SQLite** est utilisé en développement pour garder une installation légère ;
- **django-allauth** gère la connexion par e-mail et les providers sociaux ;
- **crispy-forms** et Bootstrap 5 rendent les formulaires cohérents ;
- les vues CRUD utilisent `LoginRequiredMixin` afin qu'un visiteur anonyme ne puisse pas modifier les formations.

L'application reste volontairement compacte : les vues génériques et l'ORM suffisent, sans ajouter de couches services ou repositories artificielles.

## Installation locale

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
python manage.py migrate
python manage.py runserver
```

Ouvrir ensuite `http://127.0.0.1:8000/`.

Pour la production, utiliser `config.settings.production` et fournir les variables décrites dans `.env` à partir de la configuration locale de l'environnement. Aucun secret ne doit être ajouté à Git.

## Tests

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Les tests vérifient notamment la protection des vues CRUD, le tri des cours et l'affichage des employés associés.

## Organisation

- `config/settings/` contient les configurations de base, développement et production ;
- `employee_learning/` contient les modèles, vues, URLs et tests de l'application ;
- `templates/` contient les gabarits HTML ;
- `static/` contient les styles personnalisés ;
- `requirements/` sépare les dépendances de développement et de production.

## Limites et améliorations possibles

Le projet ne gère pas encore les rôles métier détaillés, l'historique des inscriptions, les notifications ou les pièces jointes de formation. Une prochaine évolution pourrait ajouter des permissions par division, une recherche multi-critères et une base PostgreSQL pour la production.

## Licence

Ce projet est distribué sous licence MIT.
