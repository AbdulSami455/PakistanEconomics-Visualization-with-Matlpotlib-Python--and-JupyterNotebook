import matplotlib.pyplot as plt
#first Graph
x=["2012-13","2013-14","2014-15","2015-16","2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23"]
y=["2.7","2.8","2.9","3.0","3.1","3.3","3.4","3.5","3.6","3.8","3.8"]
plt.xlabel("Years",fontsize=15)
plt.ylabel("In Trillion Rupees",fontsize=15)
plt.title("Gdp Growth Simple Chart")
plt.bar(x,y,width=0.4,color='y',edgecolor='r',linewidth=.1,label="Nominal Gdp")
plt.show()
