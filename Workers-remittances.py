#USA-12.5
#SaudiArabia-24%
#UK-15
#UAE-18
#Oman-3%
#QAtar-3%
#Italy-3.3%
#Canada-2%

import matplotlib.pyplot as plt
x=[24,12,15,18,3,3,3,2]
y=["Saudi Arabia","USA","UK","UAE","Oman","Qatar","Italy","Canada"]
ex=[0,0.1,0,0,0,0,0,0]
plt.pie(x,labels=y,explode=ex,autopct="%.f%%",shadow=True,radius=1.2,labeldistance=1.04,startangle=180,textprops={"fontsize":10},wedgeprops={"linewidth":2})
plt.title("Workers Remittances")
plt.legend(loc=1)
plt.show()
