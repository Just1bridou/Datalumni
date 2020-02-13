# Datalumni - coding tests
## Test Javascript
### Règles du jeu
- Vous utiliserez uniquement du **Javascript vanilla** et Vue.js : `vue` ([CDN ici](https://cdnjs.com/libraries/vue))
- La seule dépendance autorisée est `axios` ([CDN ici](https://cdnjs.com/libraries/axios))
- Vous considérerez que l'utilisateur utilise un navigateur moderne et à jour
- Pas de prérequis pour le rendu esthétique, vous utiliserez votre framework CSS préféré

### Livrable attendu
Pour cet exercice, il vous est demandé de compléter le fichier `javascript/index.html`, qui contiendra l'ensemble de votre code (remarque : le CSS peut être stocké à part).

Vous devez créer une app affichant la liste des employés d'une société. Les informations proviennent d'un SIRH fictif et sont rendues disponibles à travers une API REST.

L'application contient les fonctionnalités suivantes :
- Les données relatives aux employés sont récupérables [via une API REST](http://dummy.restapiexample.com/)
- Les employés sont listés dans un tableau, avec les informations suivantes :
    - `ID` (fourni par l'API)
    - `Full name` (fourni par l'API)
    - `Email`: **(à calculer)** Exemple pour John Doe => "j.doe@email.com"
    - `Monthly salary`: **(à calculer)**
    - `Year of birth`: **(à calculer)**
    - Une colonne d'`Actions` contenant des boutons d'actions (voir plus bas)
- Le **décompte des employés** est affichée en-pied de la colonne `ID`
- La **total mensuel des salaires** est affiché en-pied de la colonne `Monthly salary`
- Un bouton d'action permet de **dupliquer** un employé dans le tableau
- Un bouton d'action permet de **supprimer** un employé du tableau
- Pour ces boutons d'actions, il n'est pas nécessaire de coder les requêtes associées vers l'API (`POST`, `DELETE`). Ne manipulez que les données du tableau.
- Un **bouton de tri** dans l'en-tête de colonne `Monthly salary` permet le tri croissant / décroissant des valeurs de cette colonne
- Si aucun employé n'est dans la liste, un message signale l'absence d'informations dans le tableau

#### Exemple de rendu
![Exemple datalumni-test-vue](https://github.com/waldeck-dev/datalumni-test/blob/master/javascript/datalumni-test-vue.png?raw=true)


---

## Test Python
### Règles du jeu
- Vous utiliserez Python 3.7+
- Vous n'utiliserez pas de modules tiers, seulement les modules Python natifs

### Livrables attendus
#### livrable n°1
Pour cet exercice, il vous est demandé de compléter le fichier `python/number.py`.

Vous recherchez un nombre en 1 et 1000. Un seul nombre nombre correspond à la description suivante :
- Le nombre est un nombre premier
- Le nombre est composé de deux chiffres ou plus
- Le nombre ne contient pas de 1, ni de 7
- La somme de ses chiffres est inférieure ou égale 10
- Les deux premiers chiffres donne un nombre impair quand on les additionne
- L'avant dernier chiffre est un 4
- Le dernier chiffre est égal au nombre de chiffre composant le nombre

#### livrable n°2
Pour cet exercice, il vous est demandé de compléter le fichier `python/student.py`. Les consignes concernant les différents scripts à produire sont notés en commentaire dans ce fichier.

---

## Livraison
Pour livrer votre travail :
- Vous effectuerez un fork de ce repository [`waldeck-dev/datalumni-test`](https://github.com/waldeck-dev/datalumni-test)
- Vous nous transmettrez le lien vers votre repository contenant votre travail
