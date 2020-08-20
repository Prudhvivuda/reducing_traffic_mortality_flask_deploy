import pandas as pd
import matplotlib.pyplot as plt
#import warnings
import pickle
#warnings.filterwarnings("ignore")

road_acc = pd.read_csv("road-accidents.csv", comment="#", sep="|")

from sklearn import linear_model
features = road_acc[["perc_fatl_speed","perc_fatl_alcohol","perc_fatl_1st_time"]]
target = road_acc["drvr_fatl_col_bmiles"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features,target, test_size=0.2, random_state=0)
reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)

pickle.dump(reg, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
