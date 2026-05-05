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
