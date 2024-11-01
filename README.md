

# API GraphQL de Gestion des Utilisateurs avec Django et JWT

Ce projet est une API GraphQL construite avec Django pour la gestion des utilisateurs. Elle inclut l'inscription, la connexion, la récupération et la réinitialisation de mot de passe, ainsi que la gestion des droits d'accès avec des tokens JWT pour une authentification sécurisée. L'architecture respecte les principes **SOLID** et **Clean Code**, rendant le code modulaire, extensible et maintenable.

## Fonctionnalités Principales

1. **Inscription** : 
   - Permet aux nouveaux utilisateurs de créer un compte en fournissant un nom d'utilisateur, un mot de passe et une adresse e-mail.
   - Génère des tokens JWT pour gérer les sessions utilisateur.

2. **Connexion** : 
   - Authentifie les utilisateurs existants et génère des tokens d'accès JWT pour sécuriser la session.

3. **Mot de passe oublié et réinitialisation** : 
   - Gère l'envoi d'un e-mail de réinitialisation de mot de passe sécurisé via un lien ou un token unique.

4. **Sécurisation des accès** : 
   - Utilise JSON Web Tokens pour contrôler les accès aux ressources, offrant ainsi un moyen sécurisé et efficace de gérer les droits utilisateur.

## Avantages de l'Architecture

- **Respect des principes SOLID** : Assure un code propre, extensible et facile à maintenir.
- **GraphQL pour la flexibilité** : Les clients peuvent spécifier les données exactes nécessaires dans chaque requête, optimisant ainsi les performances.
- **Modularité** : Chaque fonctionnalité (inscription, connexion, etc.) est implémentée dans un module distinct, favorisant la réutilisation et la clarté.

Grâce à l'implémentation de GraphQL, cette API fournit un moyen efficace et flexible de gérer les utilisateurs, adapté aux applications modernes.

---

## Endpoints

### GraphQL Endpoint

L'API utilise un seul endpoint pour toutes les requêtes et mutations GraphQL.

```
POST /graphql/
```

### Requête d'exemple

Toutes les requêtes doivent être envoyées en utilisant le format GraphQL, avec l'en-tête `Authorization: JWT <token>` pour les opérations sécurisées.

---

## Mutations

### 1. `registerUser`

**Description** : Inscription d'un nouvel utilisateur. Génère un token JWT et un token de rafraîchissement.

**Arguments** :
- `username` (String, obligatoire) : Nom d'utilisateur unique.
- `password` (String, obligatoire) : Mot de passe de l'utilisateur.
- `email` (String, obligatoire) : Adresse e-mail unique de l'utilisateur.

**Retourne** :
- `user` : L'utilisateur nouvellement créé.
- `token` : Token JWT pour l'authentification.
- `refresh_token` : Token de rafraîchissement pour prolonger la session.

**Exemple de Mutation** :

```graphql
mutation {
  registerUser(username: "newuser", password: "password123", email: "user@example.com") {
    user {
      id
      username
      email
    }
    token
    refreshToken
  }
}
```

---

### 2. `loginUser`

**Description** : Authentifie un utilisateur et génère un token JWT et un token de rafraîchissement.

**Arguments** :
- `username` (String, obligatoire) : Nom d'utilisateur.
- `password` (String, obligatoire) : Mot de passe.

**Retourne** :
- `token` : Token JWT pour l'authentification.
- `refresh_token` : Token de rafraîchissement.

**Exemple de Mutation** :

```graphql
mutation {
  loginUser(username: "newuser", password: "password123") {
    token
    refreshToken
  }
}
```

---

### 3. `forgotPassword`

**Description** : Envoie un e-mail de réinitialisation du mot de passe à l'utilisateur avec un token de réinitialisation.

**Arguments** :
- `email` (String, obligatoire) : L'adresse e-mail de l'utilisateur.

**Retourne** :
- `success` (Boolean) : Indique si l'e-mail a été envoyé.

**Exemple de Mutation** :

```graphql
mutation {
  forgotPassword(email: "user@example.com") {
    success
  }
}
```

---

### 4. `resetPassword`

**Description** : Permet à un utilisateur de réinitialiser son mot de passe en utilisant un token de réinitialisation.

**Arguments** :
- `reset_token` (String, obligatoire) : Le token de réinitialisation envoyé par e-mail.
- `new_password` (String, obligatoire) : Le nouveau mot de passe de l'utilisateur.

**Retourne** :
- `success` (Boolean) : Indique si le mot de passe a été réinitialisé avec succès.

**Exemple de Mutation** :

```graphql
mutation {
  resetPassword(resetToken: "your-reset-token", newPassword: "newpassword123") {
    success
  }
}
```

---

## Queries

### 1. `users`

**Description** : Retourne la liste de tous les utilisateurs.

**Arguments** : Aucun

**Retourne** :
- Liste d'objets `User`, chacun contenant :
  - `id` : Identifiant de l'utilisateur.
  - `username` : Nom d'utilisateur.
  - `email` : Adresse e-mail de l'utilisateur.
  - `is_active` : Statut actif de l'utilisateur.

**Exemple de Requête** :

```graphql
query {
  users {
    id
    username
    email
    isActive
  }
}
```

---

## Authentification et Autorisation

L'API utilise **JSON Web Tokens (JWT)** pour l'authentification. Les tokens JWT permettent de sécuriser les endpoints et de limiter l'accès aux utilisateurs authentifiés. Pour les requêtes nécessitant une authentification, incluez le token dans l'en-tête de la requête comme suit :

```
Authorization: JWT <token>
```

Les tokens de rafraîchissement peuvent être utilisés pour obtenir un nouveau token JWT lorsque l'actuel expire.

---

## Exemples d'Erreurs

- **Utilisateur non trouvé** : Si un utilisateur n'existe pas ou si les informations d'authentification sont incorrectes, une erreur `GraphQLError` est renvoyée.
- **Token non valide** : Si un token JWT est incorrect ou expiré, l'API retournera une erreur d'authentification.

---

## Configuration et Dépendances

- **Django** : Framework web pour la gestion des utilisateurs.
- **GraphQL** : Fournit un seul endpoint pour les requêtes flexibles.
- **django-graphql-jwt** : Gestion des tokens JWT pour la sécurisation des endpoints.

Assurez-vous que `django-graphql-jwt` est bien installé et configuré dans les paramètres de Django pour permettre la génération et la vérification des tokens.

---

Cette documentation couvre les fonctionnalités principales de l'API. Pour des ajouts spécifiques ou des cas d'utilisation avancés, vous pouvez étendre ce schéma en ajoutant de nouveaux types et mutations dans les modules existants.