# Décisions du projet — Snake

Ce document rassemble les principales décisions prises concernant le périmètre, l'architecture et l'organisation du projet.

L'objectif est de garder une trace des raisons derrière les choix effectués et d'éviter de revenir plusieurs fois sur les mêmes décisions.

---

## 1. Choix du jeu

### Décision

Le projet sera un jeu de Snake jouable depuis une interface web.

### Raisons

Snake possède une logique suffisamment claire pour être développée dans le temps disponible tout en permettant une séparation des responsabilités entre frontend, backend et analyse.

Le jeu permet également d'avoir plusieurs interactions entre les membres du groupe.

---

## 2. Technologies

### Décision

Le projet utilisera :

* **Python** pour le backend ;
* **HTML** pour la structure du frontend ;
* **CSS** pour la présentation ;
* **JavaScript** pour les interactions et l'affichage dynamique.

### Raisons

Ces technologies correspondent aux compétences disponibles dans le groupe et permettent de séparer clairement le frontend et le backend.

---

## 3. Architecture MVC

### Décision

Le projet suivra une architecture inspirée du modèle MVC :

```text
Frontend / View
       ↓
Controller
       ↓
Model
```

### Model

Le modèle contient :

* l'état du jeu ;
* les règles ;
* le serpent ;
* les fruits ;
* les collisions ;
* le score ;
* les informations liées à la carte.

### Controller

Le contrôleur fait le lien entre les requêtes reçues et le modèle.

### View

Le frontend affiche l'état du jeu et permet au joueur d'interagir avec celui-ci.

---

## 4. Structure simple du projet

### Décision

Le projet conservera une structure volontairement simple.

La structure de base prévue est :

```text
snake-game/
│
├── main/
│   ├── main.py
│   ├── controller.py
│   ├── model.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
│
├── assets/
├── docs/
├── tests/
├── requirements.txt
└── README.md
```

### Raisons

Le projet est réalisé dans un contexte d'apprentissage et plusieurs membres du groupe sont moins familiers avec le développement web.

Une architecture trop complexe rendrait le projet plus difficile à comprendre et à maintenir.

Il n'est donc pas prévu d'ajouter des couches telles que :

* service layer ;
* repository layer ;
* factory classes ;
* base de données ;

sauf si un besoin concret apparaît pendant le développement.

---

## 5. Pas de base de données

### Décision

Aucune base de données ne sera utilisée pour le tableau des scores.

### Raisons

Le cahier des charges demande uniquement de conserver les meilleurs scores pendant la session.

Les scores peuvent donc être conservés en mémoire.

L'utilisation d'une base de données ajouterait une complexité inutile au projet.

---

## 6. Simplification des fonctionnalités

### Décision

Les fonctionnalités essentielles seront développées en priorité.

La première version doit contenir :

* menu principal ;
* quatre niveaux de difficulté ;
* quatre cartes ;
* déplacement du serpent ;
* fruits normaux ;
* croissance du serpent ;
* score ;
* collisions ;
* fin de partie ;
* redémarrage ;
* tableau des dix meilleurs scores.

### Raisons

Le projet doit rester réalisable par l'ensemble du groupe et permettre à chaque membre de travailler sur son rôle.

La complexité technique ne constitue pas l'objectif principal du projet.

---

## 7. Fonctionnalités optionnelles

Les fonctionnalités suivantes sont considérées comme secondaires :

* différents skins de fruits ;
* gros fruits ;
* diminution de la valeur des gros fruits ;
* musique ;
* effets sonores ;
* animations supplémentaires.

### Raisons

Ces fonctionnalités peuvent être intéressantes, mais elles augmentent la quantité de travail sans être nécessaires pour obtenir une première version fonctionnelle.

Elles pourront être ajoutées si les fonctionnalités principales sont terminées.

---

## 8. Boucle de jeu

### Décision

La logique de déplacement doit fonctionner comme une boucle de jeu continue.

Le frontend ne doit pas nécessairement envoyer une requête HTTP au backend pour chaque déplacement du serpent.

### Raisons

Un jeu temps réel générant une requête HTTP pour chaque mouvement ajouterait une complexité et une charge inutiles.

La communication frontend/backend doit principalement servir aux interactions nécessaires entre les deux parties.

La solution exacte pourra être adaptée par les développeurs lors de l'implémentation.

---

## 9. Documentation avant implémentation

### Décision

La structure du projet et les principales spécifications seront préparées avant le développement.

Les méthodes Python pourront être créées avec des docstrings décrivant leur responsabilité, sans fournir directement leur implémentation.

### Raisons

Cela permet aux développeurs de commencer avec une structure claire tout en leur laissant la responsabilité de choisir l'implémentation technique.

La documentation décrit **ce qui doit être fait**, mais ne doit pas nécessairement imposer **comment le coder**.

---

## 10. Répartition des rôles

### Analyste

Responsabilités principales :

* analyse des besoins ;
* règles du jeu ;
* logique fonctionnelle ;
* spécifications ;
* documentation ;
* critères de test ;
* définition des interactions frontend/backend.

L'analyste peut aider les développeurs en cas de difficulté technique, mais n'a pas pour objectif de réaliser leur travail à leur place.

### Backend

Responsabilités principales :

* développement Python ;
* modèle ;
* contrôleur ;
* API ;
* gestion de l'état du jeu ;
* intégration avec le frontend.

### Frontend

Responsabilités principales :

* HTML ;
* CSS ;
* JavaScript ;
* interface ;
* affichage du jeu ;
* interactions avec le joueur.

### Team chef

Responsabilités principales :

* organisation du travail ;
* GitHub ;
* répartition des tâches ;
* suivi de l'avancement ;
* coordination ;
* intégration des différentes parties.

---

## 11. Principe de responsabilité

Chaque membre doit principalement travailler dans le cadre de son rôle.

Les membres peuvent s'entraider et expliquer leurs connaissances aux autres, mais l'objectif n'est pas qu'une seule personne réalise la majorité du travail technique.

Cette organisation doit permettre d'observer et d'analyser le fonctionnement réel du groupe.

---

## 12. Évolution des décisions

Les décisions de ce document ne sont pas nécessairement définitives.

Si une difficulté technique ou organisationnelle apparaît, une décision peut être modifiée.

Dans ce cas, la modification doit être ajoutée à ce document avec une courte explication de la raison du changement.
