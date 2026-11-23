# Fiche du sujet F16 : Loi d'Okun

| Élément | Contenu |
|---|---|
| Sujet | F16, Loi d'Okun |
| Thème | Relation entre croissance économique et chômage aux États-Unis |
| Tâche | Régression linéaire simple (apprentissage supervisé) |
| Algorithme du support | n° 1 : régression linéaire |
| Intérêt financier | La loi d'Okun relie l'activité au marché du travail, donnée clé pour la politique monétaire, les anticipations de croissance et l'analyse du cycle économique. |
| Question | Dans quelle mesure la croissance du PIB réel permet-elle d'expliquer la variation du taux de chômage aux États-Unis ? |
| Cible Y | ΔUₜ = Uₜ − Uₜ₋₁ : variation trimestrielle du chômage (points de %), Uₜ = moyenne trimestrielle de UNRATE |
| Variable X | gₜ = 100 × (GDPC1ₜ / GDPC1ₜ₋₁ − 1) : croissance trimestrielle du PIB réel (%) |
| Métrique principale | RMSE sur le test chronologique (secondaires : MAE, R²) |
| Référence naïve | DummyRegressor(strategy="mean") : moyenne de ΔU sur l'entraînement |

## Données

| Série | Contenu | Organisme source | Fréquence | URL |
|---|---|---|---|---|
| GDPC1 | PIB réel, Mds de $ enchaînés 2017, taux annuel désaisonnalisé | BEA, via FRED | trimestrielle | https://fred.stlouisfed.org/series/GDPC1 |
| UNRATE | Taux de chômage civil (%), désaisonnalisé | BLS, via FRED | mensuelle | https://fred.stlouisfed.org/series/UNRATE |

Licence et conditions : données publiques d'agences fédérales américaines (BEA, BLS), diffusées par FRED ; voir les conditions d'utilisation de FRED sur https://fred.stlouisfed.org/legal/ (à relire avant la remise). Date d'extraction : voir `data/raw/extraction_log.txt` (écrit par le script de téléchargement) ou à compléter : [JJ/MM/AAAA].

## Protocole d'évaluation

Découpage chronologique : entraînement jusqu'à 2009 T4, validation 2010-2016, test à partir de 2017 T1. Prétraitement (imputation par la médiane) ajusté sur l'entraînement seul via un `Pipeline`. Réajustement sur entraînement + validation, puis un seul passage sur le test. Analyse de sensibilité hors 2020-2021.

## Références

- Okun, A. M. (1962). *Potential GNP: Its Measurement and Significance*. Proceedings of the Business and Economic Statistics Section, American Statistical Association.
- Ball, L., Leigh, D., Loungani, P. (2017). Okun's Law: Fit at 50? *Journal of Money, Credit and Banking*, 49(7).
- Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
- FRED, Federal Reserve Bank of St. Louis : https://fred.stlouisfed.org
