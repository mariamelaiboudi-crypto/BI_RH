# 📊 Projet Business Intelligence (BI) - HR Analytics

## 🎯 Présentation du Projet
Ce dépôt contient une solution BI complète pour l'analyse des ressources humaines (RH). L'objectif est d'analyser l'attrition des employés, leurs performances et la structure salariale afin de fournir des informations exploitables pour la gestion des RH.

**Sujet :** HR Analytics - Employee Attrition & Performance

---

## 👥 Équipe de Projet
* **ZAKARIAE EL HADDOUCHI** - *Développement ETL & Modélisation*
* **OUSSAMA Lebyed** - *Analyse de Données & KPIs*
* **Oualid Boutayeb** - *Visualisation & Dashboard*
* **Meryam El Aiboudi** - *Analyse & Documentation BI*

---

## 🛠️ Stack Technique
* **Extraction & Transformation (ETL) :** Python (Pandas)
* **Stockage/Modélisation :** SQL (Star Schema)
* **Visualisation :** Power BI
* **Gestion de version :** Git & GitHub

---

## 🚀 Méthodologie (Cycle de vie BI)

### 1. Analyse des Besoins & KPIs
Nous avons défini les indicateurs clés de performance (KPIs) suivants :
* **Taux d'Attrition** : Pourcentage d'employés ayant quitté l'entreprise.
* **Salaire Moyen par Département** : Analyse de la répartition des coûts salariaux.
* **Performance vs Ancienneté** : Corrélation entre la note de performance et le temps passé dans l'entreprise.

### 2. Collecte et Préparation des Données
* **Source :** Données synthétiques générées via `Scripts/Python/data_generator.py`.
* **Nettoyage :** Traitement via Python (Gestion des dates, calcul de l'ancienneté, création des tables de dimension).

### 3. Modélisation (Schéma Décisionnel)
Conception d'un **Schéma en Étoile (Star Schema)** comprenant :
* **Table de Fait :** `Fact_EmployeeRecords` (Salaires, Performance, Statut)
* **Tables de Dimensions :** `Dim_Employee`, `Dim_Department`, `Dim_Date`.

### 4. Dashboarding & Visualisation
Les fichiers `.csv` transformés dans `Data/Processed/` sont prêts à être importés dans Power BI pour la création de rapports.

---

## 📁 Structure du Repository
```text
├── Data/               
│   ├── Raw/            # hr_data_raw.csv
│   └── Processed/      # Tables du Schéma en Étoile (Fact & Dim)
├── SQL/                
│   └── Scripts/        # schema_setup.sql (Structure DB)
├── Models/             
│   └── PowerBI/        # Fichiers .pbix (à venir)
├── Scripts/            
│   └── Python/         
│       ├── data_generator.py  # Génération des données
│       └── etl_process.py     # Processus ETL complet
├── Documentation/      
└── README.md           
```

## 🛠️ Comment exécuter le projet
1. Générer les données : `python Scripts/Python/data_generator.py`
2. Lancer l'ETL : `python Scripts/Python/etl_process.py`
3. Les données prêtes sont dans `Data/Processed/`.

## MVP Demo : 
![Demo](assets/image.pdf)


## 📊 Indicateurs Clés de Performance (KPI)

Le projet se concentre sur l'analyse de la performance et de la rétention des employés. Voici les principaux KPI suivis :

| Catégorie | KPI | Description | Formule / Source |
| :--- | :--- | :--- | :--- |
| **Rétention** | **Taux de Turnover** | Pourcentage d'employés ayant quitté l'entreprise. | `(Départs / Effectif Total) * 100` |
| **Rétention** | **Taux de Rétention** | Capacité de l'entreprise à conserver ses talents. | `100 - Taux de Turnover` |
| **Engagement** | **Satisfaction Moyenne** | Niveau de satisfaction global des employés. | `AVG(satisfaction_level)` |
| **Performance** | **Score d'Évaluation** | Note moyenne de la dernière évaluation. | `AVG(last_evaluation)` |
| **Opérationnel** | **Volume de Projets** | Nombre moyen de projets gérés par employé. | `AVG(number_project)` |
| **Opérationnel** | **Heures de Travail** | Moyenne des heures travaillées par mois. | `AVG(average_monthly_hours)` |
| **Évolution** | **Taux de Promotion** | % d'employés promus ces 5 dernières années. | `(Promus / Total) * 100` |
