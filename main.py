import pandas as pd
import numpy as np
import json

df = pd.read_csv('comments_final.csv')
df = df.filter(['body', 'subreddit'])
df.rename(columns={'body': 'confession', 'subreddit': 'gender'}, inplace=True)
df.replace({'AskMen': 'male', 'AskWomen': 'female'}, inplace=True)

female_indices = list(df[df['gender'] == 'female'].index)
male_indices = list(df[df['gender'] == 'male'].index)
female_selections = dict(zip(female_indices, [0 for _ in range(len(female_indices))]))
male_selections = dict(zip(male_indices, [0 for _ in range(len(male_indices))]))

def create_random_index(selection):
    values = [key for key in selection.keys() if selection[key] == 0]
    selections = np.random.choice(values, replace=False)
    selection[selections] = 1
    return selections

def sentence_generator():
    probability = np.random.rand()
    if probability < 0.5:
        index = create_random_index(male_selections)
    else:
        index = create_random_index(female_selections)
    return df.iloc[index]['confession'], df.iloc[index]['gender']

final_dict = {
        1: {},
        2: {},
        3: {},
        4: {},
        5: {}
    }

PROBABILITIES = [0, 0.25, 0.5, 0.75, 1]
        
for key in final_dict.keys():
    for probability in PROBABILITIES:
        final_dict[key][probability] = {}
        sentence, gender = sentence_generator()
        final_dict[key][probability]['sentence'] = sentence
        final_dict[key][probability]['gender'] = gender

with open('dataset.json', 'w') as f:
    json.dump(final_dict, f, indent=4)