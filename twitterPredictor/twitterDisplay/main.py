import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Popularité des candidats'),

    html.Div(children='''
        Graphes de comparaison des popularités de chaque candidat".
    '''),


#liste avg_RTS est une liste contennant les retweets moyen pour chaque candidat
#liste avg_FAVS est une liste contennant les favoris moyen pour chaque candidat
#avg_hashtags est une liste contennat le nombre moyen de hashtags pour chaque candidat
#len_tweet est une liste contennant la longueur moyenne des tweets par candidat
#tweet_sentimental est une liste de liste contennant les sentiments pour chaque candidat ( 0 neg, 1 neutre, 2 positif)
#http://127.0.0.1:8050
    dcc.Graph(
        id='example-graphRTS',
        figure={
            'data': [
                {'x': [1], 'y': [avg_RTS[0]], 'type': 'bar', 'name': 'Macron'},
                {'x': [2], 'y': [avg_RTS[1]], 'type': 'bar', 'name': u'Fillon'},
                {'x': [3], 'y': [avg_RTS[2]], 'type': 'bar', 'name': u'Le Pen'},
            ],
            'layout': {
                'title': 'nombre moyen de retweets par candidat '
            }
        }
    ),
    dcc.Graph(
        id='example-graphFAVS',
        figure={
            'data': [
                {'x': [1], 'y': [avg_FAVS[0]], 'type': 'bar', 'name': 'Macron'},
                {'x': [2], 'y': [avg_FAVS[1]], 'type': 'bar', 'name': u'Fillon'},
                {'x': [3], 'y': [avg_FAVS[2]], 'type': 'bar', 'name': u'Le Pen'},
            ],
            'layout': {
                'title': 'nombre moyen de favoris par candidat '
            }
        }
    ),
    dcc.Graph(
        id='example-graphhashtags',
        figure={
            'data': [
                {'x': [1], 'y': [avg_hashtags[0]], 'type': 'bar', 'name': 'Macron'},
                {'x': [2], 'y': [avg_hashtags[1]], 'type': 'bar', 'name': u'Fillon'},
                {'x': [3], 'y': [avg_hashtags[2]], 'type': 'bar', 'name': u'Le Pen'},
            ],
            'layout': {
                'title': 'nombre moyen de hashtags par candidat '
            }
        }
    ),
    dcc.Graph(
        id='example-graphtweets',
        figure={
            'data': [
                {'x': [1], 'y': [len_tweet[0]], 'type': 'bar', 'name': 'Macron'},
                {'x': [2], 'y': [len_tweet[1]], 'type': 'bar', 'name': u'Fillon'},
                {'x': [3], 'y': [len_tweet[2]], 'type': 'bar', 'name': u'Le Pen'},
            ],
            'layout': {
                'title': 'longueur moyenne des tweets par candidat '
            }
        }
    ),
    dcc.Graph(
        id='example-graphsentiments',
        figure={
            'data': [
                {'x': [1,2,3], 'y': [tweet_sentimental[0][0],tweet_sentimental[0][1],tweet_sentimental[0][2]], 'type': 'bar', 'name': 'Macron'},
                {'x': [1,2,3], 'y': [tweet_sentimental[1][0],tweet_sentimental[1][1],tweet_sentimental[1][2]], 'type': 'bar', 'name': u'Fillon'},
                {'x': [1,2,3], 'y': [tweet_sentimental[2][0],tweet_sentimental[2][1],tweet_sentimental[2][2]], 'type': 'bar', 'name': u'Le Pen'},
            ],
            'layout': {
                'title': 'graphe de subjectivité des candidats '
            }
        }
    ),
    html.Div(children='''
        tweets négatifs,neutres positifs.
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)


