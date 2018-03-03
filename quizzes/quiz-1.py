
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import wget
import csv


if __name__ == '__main__':
    # get files from website using wget
    # https://finance.media.yahoo.com/quote/NVDA/history/
    # https://finance.media.yahoo.com/quote/AMD/history/
    
    #nvda_data = os.system('wget 'https://finance.media.yahoo.com/quote/NVDA/history/')
    #nvda_data = wget.downlaod('https://finance.media.yahoo.com/quote/NVDA/history/')
    #amd_data = wget.downlaod('https://finance.media.yahoo.com/quote/NVDA/history/')
    
    # Date,Open,High,Low,Close,Adj Close,Volume
    #  2017-12-22,10.750000,10.770000,10.200000,10.540000,10.540000,50744500
    #  2017-12-26,10.380000,10.580000,10.340000,10.460000,10.460000,20437900
    
    with open('C:/ubuntu-sf/byte/quizzes/AMD.csv', 'r') as f:    
        # initialize input lists
        rows = csv.reader(f)
        dates = []
        opens = []
        highs = []
        lows = []
        closes = []
        adj_closes = []
        volumes = []
        
        #skip header row
        firstRow = True
        for row in rows:
            if firstRow:
                firstRow = False
                continue
            else:
                dates.append(row[0][0:4] + row[0][5:7] + row[0][-2:])
                opens.append(float(row[1]))
                highs.append(float(row[2]))
                lows.append(float(row[3]))
                closes.append(float(row[4]))
                adj_closes.append(float(row[5]))
                volumes.append(float(row[6]))
            
    df = pd.DataFrame({'Dates': dates,
                   'Opens':opens,
                   'Highs': highs,
                   'Lows':lows,
                   'Closes': closes,
                   'Adj_closes':adj_closes,
                   'Volumes': volumes
                   })
                   
    df2 = pd.DataFrame({'P': df['Closes'],
                   'V': df['Volumes'],
                   'PV': df['Closes']*df['Volumes'] })
                   
    vwap = df2['PV'].sum() / d2['V'].sum()
    
    print('vwap: ', vwap)
    