# Imports

import pandas as pd
import numpy as np
import pickle

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import RobustScaler
from xgboost import XGBRegressor
from bayes_opt import BayesianOptimization
from hyperopt import hp, fmin, tpe
from sklearn.datasets import make_regression


def get_model():

    

    departments = ['department_CO',
    'department_CPS',
    'department_DBT',
    'department_DCMS',
    'department_DEFRA',
    'department_DEFRA & DFT',
    'department_DESNZ',
    'department_DFE',
    'department_DFID',
    'department_DFT',
    'department_DHSC',
    'department_DLUHC',
    'department_DSIT',
    'department_DWP',
    'department_FCDO',
    'department_HMLR',
    'department_HMRC',
    'department_HMT',
    'department_HO',
    'department_MOD',
    'department_MOJ',
    'department_NCA',
    'department_NS&I',
    'department_ONS',
    'department_VOA']

class ModelWrapper(BaseEstimator, TransformerMixin):
    def __init__(self, model, departments, scaler):
        self.model = model
        self.departments = departments
        self.scaler = scaler
    
    def transform_input(self, input_department, input_year):
        # Skalieren des input_year
        input_year_scaled = self.scaler.transform([[input_year]])[0][0]
        
        # DataFrame mit der Spalte 'department' erstellen
        df_input = pd.DataFrame({'department': [input_department]})
        
        # Dummy-Variablen für 'department' erstellen
        department_dummy = pd.get_dummies(df_input['department'], prefix='department')
        
        # Sicherstellen, dass alle Departments vorhanden sind
        for department in self.departments:
            if department not in department_dummy.columns:
                department_dummy[department] = 0

        # Spalten in der richtigen Reihenfolge anordnen
        department_dummy = department_dummy[self.departments]

        # Feature-Array erstellen
        feature_array = np.concatenate([[input_year_scaled], department_dummy.values.flatten()])

        return feature_array.reshape(1, -1)
    
    def predict(self, input_department, input_year):
        transformed_input = self.transform_input(input_department, input_year)
        return self.model.predict(transformed_input)
