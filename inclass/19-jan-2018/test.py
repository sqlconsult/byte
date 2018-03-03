#! usr/bin/env python3

import functools

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.DataFrame({'AAA': [4,5,6,7], \
                  'BBB': [10,20,30,40], \
                  'CCC': [100,50,-30,-50]})

#df.loc[df.AAA >= 5, 'BBB'] = -1

#df.loc[df.AAA % 2 == 0, 'BBB'] = -1

#df.loc[df.AAA>=5,['BBB','CCC']]=2000

#df_mask = pd.DataFrame({'AAA':[True]*4, 'BBB':[False]*4, 'CCC':[True,False]*2})
#x=df.where(df_mask, -1000)

print (df)


#set the criteria where it'll be applied to all the columns in the matrix
Crit1=df.AAA <= 5.5 
Crit2=df.BBB == 10.0
Crit3=df.CCC> -40.0

Critters = [Crit1, Crit2, Crit3]

#annoymous function
AllCritters = functoolsredue(lamda x:y: x & y, Critters)

print (AllCritters)

print(df[AllCritters])

  


#if __name__=='__main__':
    #print(df)
