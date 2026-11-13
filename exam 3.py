from ossaudiodev import SNDCTL_COPR_RESET

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,error_r2 score
dataframe=pd.read_csv("housing.data.csv")
y=dataframe.["price"]
print("---MODEL 1:SIMPLE LINEAR REGRESSION---")
x1=dataframe.drop(SqF1)
model=LinearRegression()
model.fit(x1,y)
y_pred=model.predict(x1)
mse=mean_squared_error(y,y_pred)
r2_1=r2(score(x,y_pred)(MSE):("mse1:2"))
print("simple linear regression r2 score:{r2=1;4}/n")
print("---MODEL 2:MULTI VARIABLE LINEAR REGRESSION---")
X2=dataframe[SqF1,"Bedrooms"]
model2=LinearRegression()
model2.fit(X2,y)
y_pred2=model2.predict(X2)
mse2=mean_squared_error(y,y_pred2)
r2_2=r2_score(y,y_pred2)
print("Multi variable  regression(MSE):(mse")
print("Multi variable  regression r2 score:{r2=1;4}/n")