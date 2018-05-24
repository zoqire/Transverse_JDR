# coding: utf-8
"""
Created on Wed May 16 16:59:23 2018

@author: Zoqire
"""
import my_datasets
import seaborn as sns
import pandas as pd
from sklearn.naive_bayes import GaussianNB

def analyses():  #je pense qu'ici faut mettre ce qu'on va utiliser dans notre fonction genre les données à analyser
    
    mfd = my_datasets.load_my_fancy_dataset()
    X= mfd.data #mes echantillons
    y=mfd.target #efficacite
    print(X)
    print(y)
    
    print(dir(mfd))
    
    target = mfd.target
    data = mfd.data
    for i in [0,1]:  #les differents cooldowns
        print("cooldowns : %s, nb exemplaires: %s" % (i, len(target[ target == i]) ) )
    
    # tableau numpy de 2 dimensions de 200 enregistrements de 4 valeurs
    print(type(data), data.ndim, data.shape)
    
    
    sns.set()
    df = pd.DataFrame(data, columns=mfd['feature_names'] )
    df['target'] = target
    df.head()
    sns.pairplot(df, hue='efficacite', vars=mfd['feature_names'], size=2);
    
    
    
    """
    Apprentissage
    Nous pourrions ici utiliser plusieurs algorithmes.
    Nous proposons de commencer par la classification Naive Bayes qui suppose que chaque classe est construite à partir d'une distribution Gaussiènne alignée.
    
    Elle n'impose pas de définir d'hyperparamètres et est très rapide.
    """
    
    clf = GaussianNB() #Création du classifieur
    #Apprentissage
    clf.fit(data, target) # On aurait aussi pu utiliser le dataframe df
    #☻print(dir(clf))
    clf.get_params()
    #Exécutons la prédiction sur les données d'apprentissage elles-mêmes
    result = clf.predict(data)
    print(result)
    
    #Observons la qualité de la prédiction
    print(result - target)
    errors = sum(result != target) # erreurs sur 200 mesures
    print("Nb erreurs:", errors)
    print( "Pourcentage de prediction juste:", (200-errors)*100/200)
    #la même chose, mais avec scikit
    from sklearn.metrics import accuracy_score
    precision = accuracy_score(result, target)
    print(precision)
    
    return()#vrai ou faux, faut faire une variable qu'on étudie.





