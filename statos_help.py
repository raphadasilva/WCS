def au_carre(nbr):
  if type(nbr)!=int and type(nbr)!=float:
    print("Un nombre en argument s'il vous plaît, et rien d'autre !")
  else:
    return nbr*nbr


def au_cube(nbr):
  if type(nbr)!=int and type(nbr)!=float:
    print("Un nombre en argument s'il vous plaît, et rien d'autre !")
  else:
    return nbr**3

def val_absolue(nbr):
  if type(nbr)!=int and type(nbr)!=float:
    print("Un nombre en argument s'il vous plaît, et rien d'autre !")
  elif nbr<0:
    nbr=-nbr
    return nbr
  else:
    return nbr

def factorielle(nbr):
  resultat=1
  if type(nbr)!=int and type(nbr)!=float:
    print("Un nombre en argument s'il vous plaît, et rien d'autre !")
  else:
    resultat=nbr
    while nbr>2:
      nbr-=1
      resultat*=(nbr)   
  return resultat

def mode_liste(l_nombres):
  # on va ranger dans un dico les différents chiffres en clé, avec comme valeur le nombre de fois où ils apparaissent
  dico_reponses={}
  # ca va se régler avec une boucle
  for i in range(len(l_nombres)):
    if type(l_nombres[i])==int or type(l_nombres[i])==float:
      nombre=l_nombres[i]
      # si ce nombre apparaît déjà comme clé...
      if nombre in dico_reponses:
        #... on ajoute 1 à sa valeur actuelle
        dico_reponses[nombre]+=1
      # sinon, on le crée en lui associant 1 comme valeur de départ
      else:
        dico_reponses[nombre]=1
  # on récupère ensuite la valeur maximale contenu dans le dico
  compteur_max = dico_reponses[max(dico_reponses, key=dico_reponses.get)]
  # cette valeur n'est pas forcément le mode (si plusieurs nombres partagent la valeur maximale), on va donc implémenter une liste avec les clés du dico correspondant à cette valeur max
  l_mode=[]
  for key, value in dico_reponses.items():
    if dico_reponses[key]==compteur_max:
      l_mode.append(key)
  # si cette liste contient plus d'un élément, on n'a pas de mode
  if len(l_mode)>1:
    print("Il n'y a pas de mode particulier dans cette liste...")
  # sinon, on affiche le résultat
  else:
    print("Le mode de cette liste est le chiffre",l_mode[0],"qui apparaît", compteur_max,"fois")

def moyenne_liste(une_liste):
  # on paramètre deux variables locales à zéro
  somme=0
  total=0
  for i in range(len(une_liste)):
    # si l'élément de la liste est un chiffre, on met à jour le compteur d'éléments et la somme totale
    if type(une_liste[i])==int or type(une_liste[i])==float:
      total+=1
      somme+=une_liste[i]
  # plus qu'à calculer en sortie de boucle et retourner le résultat
  return (somme/total)

def mini_liste(une_liste):
  # le premier minimum est donc le premier chiffre de la liste
  minimum = une_liste[0]
  # on boucle sur la longueur restante
  for i in range(1,len(une_liste)):
    # et si le chiffre est inférieur au dernier minimum
     if une_liste[i]<minimum:
       # on met à jour
       minimum=une_liste[i]
  # et on sert en sortie de boucle
  return minimum

def max_liste(une_liste):
  # le premier maximum est donc le premier chiffre de la liste
  maximum = une_liste[0]
  # on boucle sur la longueur restante
  for i in range(1,len(une_liste)):
    # et si le chiffre est supérieur au dernier maximum
     if une_liste[i]>maximum:
       # on met à jour
       maximum=une_liste[i]
  # et on sert en sortie de boucle
  return maximum
