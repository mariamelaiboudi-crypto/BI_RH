# 📊 Projet Business Intelligence (BI)

## 🎯 Présentation du Projet
Ce dépôt contient les travaux réalisés dans le cadre du module **Business Intelligence**. L'objectif est de mettre en place une solution décisionnelle complète, de la collecte des données brutes jusqu'à la création d'un tableau de bord interactif pour l'aide à la décision.

**Sujet choisi :** `[Insérer le nom de votre sujet ici]`

---

## 👥 Équipe de Projet
* **ZAKARIAE EL HADDOUCHI** - *Développement ETL & Modélisation*
* **OUSSAMA Lebyed** - *Analyse de Données & KPIs*
* **Oualid Boutayeb** - *Visualisation & Dashboard*
* **Meryam El Aiboudi** - *Analyse & Documentation BI*

---

## 🛠️ Stack Technique
* **Extraction & Transformation (ETL) :** [Ex: Power Query / Python Pandas]
* **Stockage/Modélisation :** [Ex: SQL Server / PostgreSQL / MySQL]
* **Visualisation :** Power BI
* **Gestion de version :** Git & GitHub

---

## 🚀 Méthodologie (Cycle de vie BI)

### 1. Analyse des Besoins & KPIs
Nous avons défini les indicateurs clés de performance (KPIs) suivants :
* **[KPI 1]** : *Ex: Chiffre d'affaires mensuel*
* **[KPI 2]** : *Ex: Taux de croissance des ventes*
* **[KPI 3]** : *Ex: Analyse géographique des clients*

### 2. Collecte et Préparation des Données
* **Source :** [Lien vers le dataset ou description de la source]
* **Nettoyage :** Traitement via Python/Power Query (Gestion des valeurs manquantes, suppression des doublons et formatage).

### 3. Modélisation (Schéma Décisionnel)
Conception d'un **Schéma en Étoile (Star Schema)** comprenant :
* **Table de Fait :** `Ventes` (ou autre)
* **Tables de Dimensions :** `Temps`, `Produits`, `Géographie`, etc.

### 4. Dashboarding & Visualisation
Création d'un rapport interactif Power BI permettant de répondre aux questions stratégiques de l'entreprise.

---

## 📁 Structure du Repository
```text
├── Data/               # Données brutes (Raw) et nettoyées (Processed)
├── SQL/                # Scripts de création de base de données et requêtes
├── Models/             # Fichiers Power BI (.pbix)
├── Scripts/            # Scripts Python pour l'ETL et l'automatisation
├── Notebooks/          # Analyses exploratoires (Jupyter Notebooks)
├── Documentation/      # Rapport final et dictionnaire des données
└── README.md           # Présentation du projet