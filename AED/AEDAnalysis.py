import pandas as pd

df = pd.read_excel('AED/CleanedFiles/Master Data Set - Option A.xlsx')
df.rename(columns={
    'adults living in the richest 60% of households' : 'adults_rich_60', 'adults  living in the poorest 40% of households' : 'adults_poor_40', 'Inflation ' : 'inflation', 'Risk Diversification' : 'risk_div',
    'Interest' : 'interest', 'Interest Compounding' : 'interest_comp', 'Account (% age 15+)': 'account_ownership', 'Debit card ownership (% age 15+) ': 'debit_ownership', 'Saved at a financial institution (% age 15+) ': 'saved_at_fin_inst',
    'Debit card used to make a purchase in the past year (% age 15+)': 'debit_card_used_12m', 'age 15-34' : 'age_15_34', 'age 35-54' : 'age_35_54', 'age 55+' : 'age_55_plus'
    }, inplace=True)

sumstat = df.agg( 
     {
        "all_adults": ["mean", "std", "min", "max"],
        "adults_rich_60": ["mean", "std", "min", "max"],
        "adults_poor_40": ["mean", "std", "min", "max"],
        "men": ["mean", "std", "min", "max"],
        "women": ["mean", "std", "min", "max"],
        "risk_div": ["mean", "std", "min", "max"],
        "inflation": ["mean", "std", "min", "max"],
        "interest": ["mean", "std", "min", "max"],
        "interest_comp": ["mean", "std", "min", "max"],
        "account_ownership": ["mean", "std", "min", "max"],
        "debit_ownership": ["mean", "std", "min", "max"],
        "saved_at_fin_inst": ["mean", "std", "min", "max"],
        "debit_card_used_12m": ["mean", "std", "min", "max"],
    }
 )

df.to_stata('AED/CLeanedFiles/masterdata.dta')

#sumstat.T.to_excel('AED/CleanedFiles/sumstats.xlsx')
