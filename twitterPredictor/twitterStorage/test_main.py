#tests pour les fonctions main

import main as tcs

def test_store_tweets1():                           #vérifie qu'un appel de store_tweets pour une lise de liste puis un appel de unstore_tweets renvoie bien une liste de liste
    testlist=[[1,2],[3,4]]
    tcs.store_tweets(testlist,testfile)
    assert tcs.unstore_tweets(testfile)==testlist


# def test_tableau_donnees():
#    assert

def test_json_to_datafram1():
    dico_json={"a":1,"b":[2]}                       #attention!!! il faut que le dictionnaire contienne au moins une liste dans les valeurs sinon la commande dataframe ne fonctionne pas
    assert type(tcs.json_to_dataframe(dico_json))==pandas.core.frame.DataFrame



