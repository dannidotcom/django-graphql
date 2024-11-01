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
