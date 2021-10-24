import csv 

dataset1File = open('Dataset1.csv')
dataset1Reader = csv.reader(dataset1File)
dataset1Data = list(dataset1Reader)
dataset1Data

femalewage = [ float(row[0]) for row in dataset1Data if row[2] == '1' ]
xvar = sum(femalewage)/len(femalewage)
malewage = [ float(row[0]) for row in dataset1Data if row[2] == '0' ]
xvar2 = sum(malewage)/len(malewage)

xaxis = {
    'Female' : xvar,
    'Male' : xvar2
}

terms = xaxis.keys()
counts = xaxis.values()

import matplotlib.pyplot as plt
''' 
fig, ax = plt.subplots()
ax.bar(terms, counts, color =('purple'))
plt.ylabel('Mean of Hourly Wages')
plt.title('Figure 1. Gender Differences in Hourly Wages')
plt.show()
'''

dataset2File = open('Dataset2.csv')
dataset2Reader = csv.reader(dataset2File)
dataset2Data = list(dataset2Reader)
dataset2Data

Earnings = [ float(row[0]) for row in dataset2Data if row[0] !=  'Earnings Decile' ]
Full = [ float(row[1]) for row in dataset2Data if row[1] !=  'Full' ]
Capped50 = [ float(row[2]) for row in dataset2Data if row[2] !=  '50K' ]
Capped10 = [ float(row[3]) for row in dataset2Data if row[3] !=  '10K' ]
IDR = [ float(row[5]) for row in dataset2Data if row[5] !=  '(a)' ]


plt.plot(Earnings,Full, color=('red'))
plt.plot(Earnings,Capped50, color=('purple'))
plt.plot(Earnings,Capped10, color=('teal'))
plt.plot(Earnings,IDR, color=('black'))
plt.title('Figure 2. Student Loan Plan Forgiveness Based on Income')
plt.xlabel('Earnings Decile')
plt.ylabel('Student Loan Forgiveness per Person')
leg = plt.legend(['Full Forgiveness','$50K of Forgiveness', '$10K of Forgiveness', 'Income Driven Repayment'])
plt.show()
