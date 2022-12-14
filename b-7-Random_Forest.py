#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 04:18:20 2018

@author: regkr
"""

#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# veri yukleme
veriler = pd.read_csv('maaslar.csv')

x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values


#linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

plt.scatter(X,Y,color='red')
plt.plot(x,lin_reg.predict(X), color = 'blue')
plt.show()

#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

#tahminler

print(lin_reg.predict(11))
print(lin_reg.predict(6.6))

print(lin_reg2.predict(poly_reg.fit_transform(11)))
print(lin_reg2.predict(poly_reg.fit_transform(6.6)))

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)

from sklearn.svm import SVR

svr_reg = SVR(kernel = 'rbf')
svr_reg.fit(x_olcekli,y_olcekli)

plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color='blue')
plt.show()
print(svr_reg.predict(11))
print(svr_reg.predict(6.6))


from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
Z = X + 0.5
K = X - 0.5
plt.scatter(X,Y, color='red')
plt.plot(x,r_dt.predict(X), color='blue')
plt.plot(x,r_dt.predict(Z),color='green')
plt.plot(x,r_dt.predict(K), color = 'black')
plt.show()
print(r_dt.predict(11))
print(r_dt.predict(6.6))

from sklearn.ensemble import RandomForestRegressor #rf ,mport i??lemi
rf_reg = RandomForestRegressor(n_estimators = 10, random_state=0)
"""
RandomForestRegressor(n_estimators = 10, random_state=0) anlam??:
i??ine verdi??imiz de??erlerden n_estimator ka?? tahmin yap??laca???? veya ka??
tane decision tree ??izilece??i, random state ise verileri random olarak 
b??lece??ini anlat??yor.
"""
rf_reg.fit(X,Y) #modeli x ve y den e??it

print(rf_reg.predict(6.6)) #rf ile 6.6 ya gelen tahmin de??erini yazd??r

#grafikleri ??izdirme
plt.scatter(X,Y, color='red') #scatter data pointleri yani veri noktalar??n?? ??izer.
#plot ise grafik ??izer noktalar yerine
plt.plot(x,rf_reg.predict(X), color = 'blue')
plt.plot(x,rf_reg.predict(Z), color = 'green')
plt.plot(x,rf_reg.predict(K), color = 'black')
#g??r??lece??i gibi farkl?? a??a??lardan farkl?? sonu??lar ????kt??
#random forest farkl?? a??a??lardan gelen de??erlerin ortalamas??n?? verir.
"""
Bildi??imiz verilerde dt algoritmas?? daha iyi gibi g??r??nebilir
hatta kar????la??t??rma yapt??????m??zda randomforest daha ba??ar??s??z g??r??nebilir
ama bu sadece buras?? i??in ge??erlidir. ????nk?? e??er bilmedi??imiz verilerden
tahmin yaparsak decision tree bildi??i verilerle ayn?? sonu??lar?? d??nd??rme
e??ilimine sahiptir. Ama randomforest bir??ok decision tree nin ortalamas??n??
d??nd??rd?????? i??in daha iyi sonu??lar verecektir.
"""






    

