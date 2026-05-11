# 📖 Data Dictionary — HR BI Project

## TABLE : employees.csv (→ FactHR + DimEmployee)

| Colonne | Type | Description | Valeurs | Notes |
|---------|------|-------------|---------|-------|
| EmployeeID | Text | Identifiant unique employé | EMP001 à EMP300 | Clé primaire |
| Name | Text | Nom de l'employé | Employee_1... | Anonymisé |
| Age | Integer | Âge en années | 22–60 | — |
| Gender | Text | Genre | Male, Female, Non-binary | — |
| Department | Text | Département | 8 valeurs | Clé vers DimDepartment |
| JobRole | Text | Intitulé de poste | 40 rôles | — |
| Salary | Integer | Salaire annuel brut (€) | 50K–150K | — |
| HireDate | Date | Date d'embauche | 2018–2023 | Clé vers DimDate |
| ExitDate | Date | Date de départ (null si actif) | 2018–2024 ou NULL | NULL = actif |
| PerformanceRating | Integer | Score de performance | 1–5 | 1=faible, 5=excellent |

**Colonnes créées en Power Query :**

| Colonne | Type | Formule | Description |
|---------|------|---------|-------------|
| IsActive | Text | ExitDate = null → "Active" sinon "Left" | Statut employé |
| Tenure_Years | Decimal | (ExitDate ou Today - HireDate) / 365 | Ancienneté en années |
| SalaryBand | Text | Tranches de salaire | Entry/Mid/Senior/Executive |

---

## TABLE : hr_analytics.csv (→ FactHR via Merge)

| Colonne | Type | Description | Valeurs | Notes |
|---------|------|-------------|---------|-------|
| EmployeeID | Text | Clé de jointure | EMP001–EMP300 | Foreign key |
| satisfaction_level | Decimal | Niveau de satisfaction | 0.09–0.99 | 0=très insatisfait, 1=très satisfait |
| last_evaluation | Decimal | Score dernière évaluation | 0.36–0.99 | 0=mauvais, 1=excellent |
| number_project | Integer | Nb de projets assignés | 2–7 | — |
| average_monthly_hours | Integer | Heures travaillées/mois en moyenne | 140–310 | >220 = risque surcharge |
| time_spend_company | Integer | Ancienneté en années (entier) | 1–10 | Redondant avec Tenure_Years |
| work_accident | Binary | Accident de travail | 0=non, 1=oui | — |
| left | Binary | L'employé a-t-il quitté ? | 0=non, 1=oui | Variable cible attrition |
| promotion_last_5years | Binary | Promu dans les 5 dernières années | 0=non, 1=oui | — |
| Department | Text | Département (format différent) | sales, hr... | Ne pas importer (doublon) |
| salary | Text | Niveau de salaire | low, medium, high | Ne pas importer (moins précis) |

---

## STAR SCHEMA — Rôles des tables

| Table | Type | Rôle | Clé |
|-------|------|------|-----|
| FactHR | Fact | Contient les métriques | EmployeeID + DeptKey + DateKey |
| DimEmployee | Dimension | Attributs des employés | EmployeeID |
| DimDepartment | Dimension | Attributs des départements | DeptKey |
| DimDate | Dimension | Calendrier complet | DateKey (Date) |
| _Measures | Vide | Contient toutes les mesures DAX | — |

---

## SEUILS MÉTIER RH (Benchmarks)

| KPI | Seuil Alerte | Seuil Critique | Source |
|-----|-------------|----------------|--------|
| Attrition Rate | >15% | >25% | Benchmark industrie |
| Satisfaction Level | <0.65 | <0.50 | Standard RH |
| Avg Monthly Hours | >200h | >220h | Risque burnout |
| Performance Rating | <2.5 | <2.0 | Seuil PIP |
| Promotion Rate | <5%/5ans | <2%/5ans | Équité interne |
