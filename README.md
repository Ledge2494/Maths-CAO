# Maths-CAO
Un outil qui permet de concevoir des énoncés de mathématiques. Pour l'instant, l'outil peux faire des énoncés sur la géométries dans l'espace

# Problèmes connus
L'algorithme de génération d'exercice droite-droite produit beaucoup d'erreur, son utilisation n'est donc pas recommandé

# Utilisation
Pour générer un exercice, il faut éditer le fichier `sujet.py` en modifiant les 2 paramètres de la dernière fonction appelé, soit `enonce`.  
Parmis les paramètres possibles il y a :
- "Point"
- "Vecteur"
- "Droite"
- "Plan"

Puis le programme va générer un exercice permettant d'arriver du 1er objet mathématique au second.  
Un 3ème paramètre est disponible, il s'agit de la seed. Lorsque celle-ci est fournis, il est possible de reproduire à l'identique un exercice générer. 
Il y a donc une seed unique par exercice.

Il est aussi d'importer le programme dans un interpréteur python via la commande : 
```python
from sujet import enonce
```  
Puis d'utiliser la fonction comme expliqué précédement
