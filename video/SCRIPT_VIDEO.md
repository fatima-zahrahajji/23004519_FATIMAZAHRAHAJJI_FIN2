# Script de la vidéo (60 à 90 s)

À enregistrer par l'étudiante, avec sa voix, en capture d'écran (720p minimum, `.mp4`), puis à déposer ici sous le nom `demonstration.mp4` (ou mettre un lien dans le README).

| Temps | À l'écran | À dire |
|---|---|---|
| 0–20 s | Diapositive 1 | « Bonjour, je m'appelle Fatima Zahra Hajji, groupe [X], sujet F16 : la loi d'Okun. Ma problématique : dans quelle mesure la croissance du PIB réel américain explique-t-elle la variation du taux de chômage ? Mon objectif : estimer le coefficient d'Okun, qui doit être négatif, et battre une référence naïve. » |
| 20–45 s | Notebook : tableau de données, puis découpage train / val / test | « J'utilise deux séries FRED : le PIB réel et le chômage, ramené au trimestre par la moyenne des trois mois. Je travaille en variations : croissance du PIB contre variation du chômage. L'algorithme est une régression linéaire simple, dans un pipeline, avec un découpage chronologique : entraînement jusqu'en 2009, validation de 2010 à 2016, test à partir de 2017, utilisé une seule fois. » |
| 45–75 s | Notebook : section 8.2 (β̂), puis tableau des résultats ou diapositive 5 | « Voici le résultat. Le coefficient est de moins 0,28 : un point de croissance en plus correspond à 0,28 point de chômage en moins. Sur le test complet, la régression fait mieux que la moyenne : RMSE de 1,22 contre 1,69, et R² de 0,47. Mais hors 2020-2021, elle fait moins bien : RMSE de 0,20 contre 0,13. » |
| 75–90 s | Diapositive 6 | « En conclusion : le lien d'Okun existe, mais la prédiction est fragile, car elle est portée par le choc de 2020. Une piste d'amélioration : ajouter la croissance retardée. » |

Conseils : exécuter le notebook avant d'enregistrer, ne pas montrer de mot de passe ni de jeton, chronométrer une fois.
