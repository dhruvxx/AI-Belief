import pandas as pd
import numpy as np
import json
import time

with open('dataset.json') as f:
    data = json.load(f)

df = pd.read_csv('users_data.csv')
SETS = ["1", "2", "3", "4", "5"]
DESCRIPTION = """
Hello, thank you for voluteering to help us with our research.
We are trying to analyse the trust of people in artificial intelligence by looking at the predictions of a machine learning model.
We will show you a confession of a person and you will have to decide if you trust the model or not.
At every time step, we have a model with a certain accuracy and you will decide whether you agree with that prediction or not.
If you agree, please type 'y' and if you disagree, please type 'n' for each confession the game shows you.
"""

print(DESCRIPTION)
time.sleep(5)

temp_dict = {}

name = str(input("Please enter your name: "))
temp_dict['Name'] = name
age = int(input("Please enter your age: "))
temp_dict['Age'] = age
print("For your gender, when the options shows up enter either M or F")
time.sleep(1)
gender = str(input("Please enter your gender: "))
temp_dict['Gender'] = gender

SET_NUMBER = np.random.choice(SETS)
print()
print("You will be playing with set number: ", SET_NUMBER)

DESCRIPTION = """
Now, we need you to tell us about your experience and understanding of Machine Learning.
1: I have no idea what Machine Learning is.
2: I have heard about Machine Learning but I don't know much about it.
3: I have a basic understanding of Machine Learning.
4: I have a good understanding of Machine Learning.
5: I am an expert in Machine Learning.
"""

print(DESCRIPTION)
time.sleep(5)

ml_exp = int(input("Please enter your experience with Machine Learning (select a number from above): "))
print()
temp_dict['ML Experience'] = ml_exp

DESCRIPTION = """
We will now show you a confession of a person and you will have to decide if you trust the model or not.
At every time step, we have a model with a certain accuracy which will try to predict the gender of the confessor. You will have to tell us if you agree or not.
"""

print(DESCRIPTION)
time.sleep(5)
print()

question_bank = data[SET_NUMBER]
answers = []
for question in question_bank.keys():
    print("The confession is shown below: ")
    print()
    print(question_bank[question]['sentence'])
    print()
    time.sleep(3)
    print("The model predicts the gender of the confessor to be: ", question_bank[question]['gender'])
    print()
    time.sleep(2)
    print("The accuracy of the model is: ", str(int(float(question) * 100)) + "%")
    print()
    time.sleep(2)
    print("Do you agree with the prediction? Please enter either 'y' or 'n'")
    inp = str(input("Type y if you think the model is right else n: ")).lower()
    print()
    answers.append(inp)

temp_dict['Zero Percentage'] = answers[0]
temp_dict['Twenty Five Percentage'] = answers[1]
temp_dict['Fifty Percentage'] = answers[2]
temp_dict['Seventy Five Percentage'] = answers[3]
temp_dict['Hundred Percentage'] = answers[4]

new_df = pd.DataFrame(temp_dict, index=[0])
final_df = pd.concat([df, new_df])

final_df.drop(final_df.columns[final_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

final_df.to_csv('users_data.csv')

print("Thank you for playing the game. Your data has been saved.")