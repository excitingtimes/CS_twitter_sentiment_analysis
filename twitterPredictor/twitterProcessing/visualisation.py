#fonctionnalité (5?)-6

import pandas as pd
import matplotlib.pyplot as plt

def graphe(list_abs,list_ord,name_abs,name_ord,title):
    title=title+" x: "+name_abs+" y:"+name_ord
    array=pd.Series(data=list_abs,index=list_ord)
    array.plot(figsize=(16,8), label=title,
    plt.show()                                              #fonction inachevée
