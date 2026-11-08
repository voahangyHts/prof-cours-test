"""
Séance S01 - 01a : découvrir les données de taxis avec pandas
=============================================================
Version miniature du notebook 01a_decouvrir_pyspark du cours.
Même logique (lire, regarder, filtrer, joindre, agréger, tracer),
mais avec pandas et un petit fichier de 40 courses.

COMMENT TRAVAILLER
- Ne modifie PAS ce fichier : copie-le d'abord dans mon_travail/S01/.
- Chaque "# %%" est une cellule. Dans VS Code, clique sur "Run Cell"
  au-dessus, ou lance tout le fichier : python mon_travail/S01/01a_decouvrir_pandas.py
- Remplace chaque "# TODO" par ton code, un exercice à la fois.
"""

# %% Cellule 0 - Préparation (déjà faite, ne pas modifier)
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Dossier data/raw, retrouvé à partir de l'emplacement de ce fichier
RAW = Path(__file__).resolve().parents[2] / "data" / "raw"
print("Dossier des données :", RAW)


# %% Exercice 1 - Lire les courses
# But : charger data/raw/courses_taxi_2025-01.csv dans un DataFrame nommé "courses".
# Indice : pd.read_csv(RAW / "nom_du_fichier.csv")
# TODO


# %% Exercice 2 - Regarder les données
# a) Afficher les 5 premières lignes            (équivalent Spark : .show(5))
# b) Afficher le nombre de lignes et de colonnes (équivalent Spark : .count())
# c) Afficher le type de chaque colonne          (équivalent Spark : .printSchema())
# TODO


# %% Exercice 3 - Véracité : repérer les lignes douteuses
# Le fichier contient volontairement quelques erreurs.
# a) Combien de courses ont une distance égale à 0 ?
# b) Combien de courses ont un montant total négatif ?
# c) Combien de courses ont commencé AVANT le 1er janvier 2025 ?
# d) Créer "courses_ok" qui ne garde que les courses valides.
# TODO


# %% Exercice 4 - Ajouter une colonne calculée
# Ajouter à courses_ok une colonne "pourboire_pct" = tip_amount / fare_amount * 100
# (équivalent Spark : .withColumn())
# TODO


# %% Exercice 5 - Joindre les zones
# a) Lire data/raw/taxi_zone_lookup.csv dans "zones"
# b) Joindre courses_ok et zones pour obtenir le quartier (Borough) et le nom (Zone)
#    de la zone de DÉPART (PULocationID <-> LocationID)
#    Indice : courses_ok.merge(zones, left_on=..., right_on=..., how="left")
# TODO


# %% Exercice 6 - Agréger par quartier
# Pour chaque Borough de départ : nombre de courses, total_amount moyen, distance moyenne.
# Trier du plus grand nombre de courses au plus petit.
# (équivalent Spark : .groupBy().agg())
# TODO


# %% Exercice 7 - Tracer un graphique
# Diagramme en barres du nombre de courses par Borough de départ,
# avec un titre et des noms d'axes. L'enregistrer dans mon_travail/S01/courses_par_quartier.png
# TODO
