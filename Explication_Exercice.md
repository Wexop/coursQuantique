# But de l'exercice : Visualiser l'évolution d'un Qubit

Cet exercice a pour but de créer un pont visuel et artistique entre la mécanique quantique et la 3D.

Voici l'explication étape par étape :

### 1. Qu'est-ce qu'un Qubit et la Sphère de Bloch ?
En informatique classique, un bit vaut soit `0`, soit `1`.
En informatique quantique, un **qubit** peut être dans une superposition d'états : un peu de `0` et un peu de `1` en même temps.

Pour se représenter cela visuellement, les physiciens utilisent la **Sphère de Bloch**.
Imaginez une sphère en 3D :
- Le pôle Nord représente l'état `0`.
- Le pôle Sud représente l'état `1`.
- Tout point à la surface de la sphère représente un état quantique valide (une superposition).

L'état du qubit est donc défini par un vecteur (une flèche) qui part du centre de la sphère et pointe vers la surface. Les coordonnées de la pointe de cette flèche sont notées **(x, y, z)**.

### 2. Le rôle de Qiskit (La partie quantique)
Dans le code, on utilise la bibliothèque d'IBM, `Qiskit`, pour simuler ce qubit.
- On applique des "portes quantiques" (comme `ry` et `rz` dans le code). Ce sont l'équivalent des portes logiques (AND, OR, NOT) mais pour le quantique.
- Ces portes ont pour effet de **faire tourner** le vecteur du qubit sur la sphère de Bloch.
- À chaque étape (chaque frame de l'animation), on calcule les nouvelles coordonnées **(x, y, z)** du qubit. C'est notre trajectoire.

### 3. Le rôle de Blender (La partie visuelle)
L'exercice consiste à prendre ces données purement mathématiques (x, y, z) et à s'en servir pour "piloter" (animer) un objet 3D dans Blender (ici, la tête de singe "Suzanne").

On fait ce qu'on appelle un **Mapping** (une correspondance) :
- **Position :** Les coordonnées `(x, y, z)` du qubit dictent la position `(x, y, z)` de l'objet dans l'espace 3D de Blender. (L'objet se déplace sur la surface d'une sphère invisible).
- **Rotation :** Les coordonnées `(x, y, z)` du qubit dictent la rotation de l'objet (l'objet s'incline en fonction de l'état quantique).
- **Couleur :** Les coordonnées `(x, y, z)` (qui vont de -1 à 1) sont converties en valeurs de couleurs Rouge, Vert, Bleu (RVB) (qui vont de 0 à 1). Ainsi, l'objet change de couleur au fur et à mesure que son état quantique évolue.

### En résumé
L'animation finale que vous voyez n'est pas "animée à la main" par un artiste. Elle est **générée procéduralement par les lois de la mécanique quantique**. Le mouvement, la rotation et la couleur de l'objet sont la traduction directe de l'évolution de l'état d'un qubit dans le temps lorsqu'on lui applique des opérations mathématiques.
