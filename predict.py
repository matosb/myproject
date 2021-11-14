import pandas as pd
import numpy as np
import os

test = pd.read_csv('test.csv')

test = test.drop(['Name', 'Ticket', 'Cabin'], axis=1)

test['Embarked'] = test['Embarked'].fillna(test['Embarked'].mode())

data = [test]
for dataset in data:
    mean = dataset['Age'].mean()
    std = dataset['Age'].std()
    is_null = dataset['Age'].isnull().sum()
    age_slice = dataset['Age'].copy()
    rand_age = np.random.randint(mean-std, mean+std, size=is_null)
    age_slice[np.isnan(age_slice)] = rand_age
    dataset['Age'] = age_slice
    dataset['Age'] = test['Age'].astype(int)

features = [ 'Sex', 'SibSp', 'Parch', 'Pclass', 'Age']
test = pd.get_dummies(test[features])

import joblib
rf_cl = joblib.load('clf.pkl')

y_pred = rf_cl.predict(test)
#print(y_pred)
test['y'] = y_pred
test.to_csv('result.csv')
