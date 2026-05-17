# 📊 HR Analytics Dashboard — Power BI

> **Projet BI RH complet** : Analyse de l'attrition, satisfaction et performance des employés  
> Construit avec Power BI Desktop · Power Query · DAX · Star Schema

---

## 🎯 Problème Business

Un taux d'attrition de **23%** — bien au-dessus du benchmark industrie de 15%.  
Ce projet identifie les causes profondes et les segments à risque pour orienter les décisions RH.

**Impact estimé** : Réduire l'attrition de 23% → 15% = économie de ~50 000€/an en coûts de recrutement.

---

## 📁 Structure du Projet

```
BI_RH/
├── Data/
│   └── Raw/
│       ├── employees.csv          # 300 employés, 2018-2024
│       └── hr_analytics.csv       # Métriques comportementales RH
├── PowerBI/
│   ├── etl_HR.pbix                # Phase ETL (Power Query)
│   ├── dim__HR.pbix               # Modélisation (Dimensions)
│   └── dax__HR.pbix               # Mesures DAX & Dashboard
├── Screenshots/
│   └── modele_etoile.png          # Architecture du modèle
├── Documentation/
│   ├── data_dictionary.md
│   └── excutiveTheme.json         # Thème JSON pour Power BI
└── README.md
```

---

## 🛠️ Stack Technique

| Outil | Usage |
|-------|-------|
| Power BI Desktop | Environnement principal |
| Power Query (M) | ETL visuel, nettoyage, transformations |
| DAX | Mesures calculées, KPIs |
| Star Schema | Architecture Data Warehouse |

---
## 👥 Équipe de Projet
* **ZAKARIAE EL HADDOUCHI** - *Développement ETL & Modélisation*
* **OUSSAMA Lebyed** - *Analyse de Données & KPIs*
* **Oualid Boutayeb** - *Visualisation & Dashboard*
* **Meryam El Aiboudi** - *Analyse & Documentation BI*


## 🗂️ Architecture des Données

```
         DimDate          DimEmployee       DimDepartment
        (DateKey)        (EmployeeID)         (DeptKey)
            │                  │                  │
            └──────────────────┼──────────────────┘
                               │
                          ⭐ FactHR
                    (DateKey, EmployeeID, DeptKey,
                     Salary, satisfaction_level,
                     last_evaluation, left, IsActive,
                     number_project, Tenure_Years)
```

**Pourquoi Star Schema ?**
- Requêtes DAX 10x plus rapides
- Relations claires et maintenables
- Standard Data Warehouse professionnel

---

## 📐 Mesures DAX Principales

```dax
-- Taux d'attrition
Attrition Rate = 
DIVIDE(
    CALCULATE(DISTINCTCOUNT(FactHR[EmployeeID]), FactHR[left] = 1),
    [Total Employees], 0
)

-- Employés à risque (surcharge horaire)
Overtime Risk Score = 
CALCULATE(
    DISTINCTCOUNT(FactHR[EmployeeID]),
    FILTER(FactHR, FactHR[average_monthly_hours] > 220)
)

-- Taux de rétention
Retention Rate = 1 - [Attrition Rate]
```

**Fonctions DAX utilisées :** CALCULATE · DISTINCTCOUNT · DIVIDE · FILTER · AVERAGE · AVERAGEX · DIVIDE

---

## 📊 Pages du Dashboard

| Page | Question Business | Visuels Clés |
|------|-------------------|--------------|
| 1. Executive Overview | État global du capital humain | 4 KPI Cards, Donut, Bar, Line |
| 2. Attrition Analysis | Qui part, quand, pourquoi ? | Scatter Plot, Stacked Bar |
| 3. Department Insights | Quels depts sont à risque ? | Matrix, Treemap, Gauge |
| 4. Employee Satisfaction | Qu'est-ce qui influence la satisfaction ? | Scatter, Line Chart |
| 5. Salary & Performance | Salaire = performance ? Inégalités ? | Box Plot, Scatter |

---

## 📈 Insights Business Trouvés

1. **Sales = département le plus à risque** : 31% d'attrition vs 14% en Engineering
2. **Surcharge horaire critique** : Employés >220h/mois ont 2.3x plus de risque de départ
3. **Pic d'attrition à 2-3 ans** d'ancienneté (pas en début de carrière)
4. **Top performers sous-rémunérés** partent 2x plus souvent
5. **Satisfaction <0.5** corrèle avec 78% de taux de départ

---

## 🎓 Compétences Démontrées

- ✅ Power Query ETL (M language, Merge, Conditional Columns)
- ✅ Modélisation Star Schema professionnel
- ✅ DAX : CALCULATE, FILTER, DIVIDE, DISTINCTCOUNT, AVERAGEX
- ✅ Time Intelligence (DimDate marquée)
- ✅ Dashboard design & UX (5 pages thématiques)
- ✅ Storytelling Data & présentation business
- ✅ Analyse RH : attrition, satisfaction, performance, équité salariale

---

## 🚀 Reproduire ce Projet

1. Clonez ce repo
2. Placez les CSV dans `Data/Raw/`
3. Ouvrez les fichiers dans `PowerBI/` avec Power BI Desktop
4. Rafraîchissez les données (Home → Refresh)

**Prérequis :** Power BI Desktop (gratuit) — [Télécharger ici](https://powerbi.microsoft.com/desktop)

---

## 👤 Auteur

Projet réalisé dans le cadre d'un apprentissage BI professionnel.  
Approche : pensée analytique senior, bonnes pratiques Data Warehouse, storytelling data.

---

*Star ⭐ ce repo si ce projet vous a été utile !*