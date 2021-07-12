# packages for data analysis & mapping
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt
import seaborn as sns
from datetime import date 

# modeling methods
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, f_regression, RFE 
import sklearn.preprocessing

# address warnings
import warnings
warnings.filterwarnings("ignore")

def clean_college_data(df):
    '''
    This function takes in a Pandas DataFrame made up of college/university data.
    The output is a clean dataframe.
    '''
    # Rename college name column
    df = df.rename(columns={"Unnamed: 0": "Name", 
                            "F.Undergrad": "Full-time", 
                            "P.Undergrad": "Part-time",
                            "Room.Board": "RoomBoard",
                            "S.F.Ratio": "SFRatio",
                            "perc.alumni": "perc-alumni",
                            "Grad.Rate": "GradRate"})
    
    # Changing Cazenovia College GradRate to mean GradRate
    df.loc[95, 'GradRate'] = 65
    
    # Encoding Private column to numeric dtype
    df.Private.replace({'Yes': 1, 'No': 0}, inplace=True)
    
    # Create AcceptanceRate column
    df['AcceptanceRate'] = df.Accept / df.Apps
    
    column_names = ['Name', 
                    'Private',
                    'Apps',
                    'Accept',
                    'AcceptanceRate',
                    'Enroll',
                    'Top10perc',
                    'Top25perc',
                    'Full-time',
                    'Part-time',
                    'Outstate',
                    'RoomBoard',
                    'Books',
                    'Personal',
                    'PhD',
                    'Terminal',
                    'SFRatio',
                    'perc-alumni',
                    'Expend',
                    'GradRate']
    
    # Re-order columns
    df = df.reindex(columns=column_names)
    
    return df

def train_validate_test(df, target):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
        
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, X_train, y_train, X_validate, y_validate, X_test, y_test