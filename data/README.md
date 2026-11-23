# Données brutes : procédure de téléchargement

Les deux séries sont publiques et légères ; elles sont récupérées depuis l'export CSV de FRED.

| Fichier | Série | URL source |
|---|---|---|
| `GDPC1.csv` | PIB réel (BEA) | https://fred.stlouisfed.org/graph/fredgraph.csv?id=GDPC1 |
| `UNRATE.csv` | Taux de chômage (BLS) | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE |

## Procédure

```
python data/raw/download_fred.py
```

Le script écrit les deux CSV dans ce dossier (colonnes `observation_date` et le code de la série) et consigne la date d'extraction dans `extraction_log.txt`.

**En cas d'échec réseau** : ouvrir la page FRED de chaque série (URL ci-dessus, sans `graph/fredgraph.csv`), cliquer sur « Download » → « CSV », puis déposer les fichiers ici sous les noms `GDPC1.csv` et `UNRATE.csv`.

## Licence

Données publiques de la BEA et du BLS diffusées par FRED ; conditions d'utilisation : https://fred.stlouisfed.org/legal/.
