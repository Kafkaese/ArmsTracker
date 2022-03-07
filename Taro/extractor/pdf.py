from tabula.io import read_pdf
#import pandas as pd

def german_report(pdf_path, pages = 'all'):
    '''
    Extract table of exports from bi-annual report of BMWK
    '''
    
    report = read_pdf(pdf_path, pages=pages)[0]
    report.rename(columns = {'Land':' country', 'Wert in Tausend €': 'amount'}, inplace=True)
    report.amount = report.amount.apply(lambda x: x * 1000)
    
    return report
        