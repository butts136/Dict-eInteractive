
# **Application de Pratique des Mots**

Bienvenue dans l'**Application de Pratique des Mots** ! Ce projet est une application web conçue pour aider les enfants à pratiquer l'écriture des mots de la semaine. L'application offre une interface conviviale pour les utilisateurs et une section administrateur sécurisée pour gérer la liste des mots.

---

## 🌟 **Table des Matières**

- [**Fonctionnalités**](#-fonctionnalités)
- [**Aperçu**](#-aperçu)
- [**Prérequis**](#-prérequis)
- [**Installation**](#-installation)
- [**Utilisation**](#-utilisation)
  - [**Exécution avec Docker**](#exécution-avec-docker)
  - [**Accès à l'Application**](#accès-à-lapplication)
- [**Structure du Projet**](#-structure-du-projet)
- [**Configuration**](#-configuration)
- [**Contribuer**](#-contribuer)
- [**Licence**](#-licence)
- [**Contact**](#-contact)

---

## ✨ **Fonctionnalités**

- **Interface Utilisateur Simple** : Une page d'accueil avec deux options principales :
  - **Tester les mots de la semaine**
  - **Accès administrateur**

- **Section Administrateur Sécurisée** :
  - Connexion avec nom d'utilisateur et mot de passe.
  - Ajout et suppression interactive des mots de la liste.
  - Les mots sont présentés dans l'ordre sur la page administrateur.

- **Pratique des Mots pour les Enfants** :
  - Saisie du nom de l'enfant.
  - Pratique interactive de l'écriture des mots.
  - Indication en temps réel des lettres incorrectes (surlignage en rouge).
  - Bouton **"Passer au mot suivant"** une fois le mot réussi.
  - Affichage du nombre de fautes, du nombre de mots passés et restants (e.g., **01 sur 17 mots**).

---

## 🖼️ **Aperçu**

*Étant donné que les images ne peuvent pas être affichées dans ce format, veuillez vous référer à l'application pour voir l'interface utilisateur conviviale et intuitive.*

---

## 🛠️ **Prérequis**

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Docker Desktop** : [Télécharger Docker Desktop](https://www.docker.com/products/docker-desktop)
- **Git** : [Télécharger Git](https://git-scm.com/downloads)

---

## 📥 **Installation**

1. **Cloner le Référentiel GitHub**

   ```bash
   git clone https://github.com/votre_nom_utilisateur/application-de-mots.git
   ```

2. **Naviguer dans le Répertoire du Projet**

   ```bash
   cd application-de-mots
   ```

---

## 🚀 **Utilisation**

### **Exécution avec Docker**

1. **Construire l'Image Docker**

   ```bash
   docker build -t application-de-mots .
   ```

   > *Cette commande construit l'image Docker en utilisant le `Dockerfile` présent dans le répertoire.*

2. **Exécuter le Conteneur Docker**

   ```bash
   docker run -d -p 1010:1010 --name mon_app application-de-mots
   ```

   > *Le conteneur est maintenant en cours d'exécution en arrière-plan et est accessible via le port 1010.*

### **Accès à l'Application**

- **Ouvrez votre navigateur web** et rendez-vous sur :

  ```
  http://localhost:1010
  ```

- Vous verrez la page d'accueil avec les options :

  - **Tester les mots de la semaine**
  - **Accès administrateur**

---

## 📂 **Structure du Projet**

```bash
application-de-mots/
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── admin.html
│   ├── enter_name.html
│   ├── index.html
│   ├── login.html
│   ├── test_complete.html
│   └── test.html
└── words.json
```

- **app.py** : Fichier principal de l'application Flask.
- **Dockerfile** : Fichier pour construire l'image Docker.
- **requirements.txt** : Liste des dépendances Python.
- **templates/** : Dossier contenant les fichiers HTML pour les pages web.
- **words.json** : Fichier JSON pour stocker les mots (créé automatiquement).

---

## ⚙️ **Configuration**

- **Identifiants Administrateur** :

  - **Nom d'utilisateur** : `Butts136`
  - **Mot de passe** : `136Butts`

- **Clé Secrète Flask** :

  - Dans `app.py`, vous pouvez modifier la clé secrète pour sécuriser les sessions :

    ```python
    app.secret_key = 'votre_cle_secrete'
    ```

- **Port d'Écoute** :

  - Par défaut, l'application écoute sur le port `1010`. Vous pouvez le modifier dans `app.py` :

    ```python
    app.run(host='0.0.0.0', port=1010)
    ```

---

## 🤝 **Contribuer**

Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application, veuillez suivre les étapes ci-dessous :

1. **Fork** le projet.
2. **Créez** votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. **Commitez** vos changements (`git commit -m 'Add some AmazingFeature'`).
4. **Poussez** vers la branche (`git push origin feature/AmazingFeature`).
5. **Ouvrez** une Pull Request.

---

## 📄 **Licence**

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 📧 **Contact**

**Votre Nom** - [votre.email@example.com](mailto:votre.email@example.com)

Lien du Projet : [https://github.com/votre_nom_utilisateur/application-de-mots](https://github.com/votre_nom_utilisateur/application-de-mots)

---

## 🎉 **Remerciements**

Merci d'utiliser cette application ! Nous espérons qu'elle sera utile pour aider les enfants à pratiquer l'écriture des mots de manière interactive et amusante.

---

*Note : Pour toute question ou problème, n'hésitez pas à ouvrir une issue sur le référentiel GitHub.*

---

## 🔧 **Commandes Utiles**

- **Arrêter le Conteneur Docker** :

  ```bash
  docker stop mon_app
  ```

- **Redémarrer le Conteneur Docker** :

  ```bash
  docker start mon_app
  ```

- **Supprimer le Conteneur Docker** :

  ```bash
  docker rm mon_app
  ```

- **Supprimer l'Image Docker** :

  ```bash
  docker rmi application-de-mots
  ```

---

## 🌐 **Ressources Supplémentaires**

- **Flask Documentation** : [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **Docker Documentation** : [https://docs.docker.com/](https://docs.docker.com/)

---

## 💡 **Astuces**

- **Gestion des Données Persistantes** :

  - Pour conserver les mots ajoutés même après avoir arrêté le conteneur, utilisez un volume Docker :

    ```bash
    docker run -d -p 1010:1010 -v $(pwd)/words.json:/app/words.json --name mon_app application-de-mots
    ```

- **Sécurité** :

  - Pensez à modifier les identifiants par défaut pour sécuriser l'accès administrateur.
  - Utilisez des variables d'environnement pour stocker les informations sensibles.

---

## 📝 **Changelog**

- **Version 1.0.0**
  - Première version fonctionnelle de l'application.
  - Fonctionnalités principales implémentées.

---

## 📌 **À Faire**

- [ ] Ajouter du style avec CSS pour une meilleure expérience utilisateur.
- [ ] Implémenter une base de données pour une gestion plus robuste des données.
- [ ] Améliorer la gestion des erreurs et les messages d'information.
- [ ] Ajouter des tests unitaires pour assurer la qualité du code.

---

Merci d'avoir lu ce README détaillé. Nous espérons que vous apprécierez l'utilisation de cette application autant que nous avons apprécié sa création !
