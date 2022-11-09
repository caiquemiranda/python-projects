# importing required libraries
import pandas as pd
import string
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier

import pickle
import warnings
import re

warnings.filterwarnings("ignore")

msg = pd.read_csv("./Message_Spam_Detection/Cleaned_Dataset.csv", encoding='latin-1')
msg.drop(['Unnamed: 0'], axis=1, inplace=True)