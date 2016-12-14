import pandas as pd

'''
Bubble chart of BorrowerAPR on Y axis and DebtToIncomeRatio on X axis of 
different occupations (Occupation). Size of bubble is a total debt
'''

data = pd.read_csv("prosperLoanData.csv")
data = data.dropna(subset = ["Occupation"])
data = data.loc[:,["DebtToIncomeRatio", "Occupation", "BorrowerAPR", "LoanOriginalAmount"]]
final = data.groupby(["Occupation"]).agg({"BorrowerAPR": "mean", "DebtToIncomeRatio": "mean", "LoanOriginalAmount": "sum"}).reset_index()

final.to_csv('mydf.tsv', sep='\t')
