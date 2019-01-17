# -*- coding: utf-8 -*-
'''
Time: 2018-06-19 11:06
 Author: Lucifer yue
 To update your source code.
'''

#import numpy as np
import pandas as pd
from pytdx.reader import TdxDailyBarReader     
from pytdx.reader import TdxLCMinBarReader


#D:\new_tpyzq_v6\vipdoc\sh\lday
def marketcode(code):
    code = str(code)

    if  '60' == code[0]+code[1]:
        market = 'sh'
    #而elif后面的命令是根据上一个if是否运行，如果运行了，elif则略过，否则才运行
    elif  '51' == code[0]+code[1]:
        market = 'sh'
    elif  '88' == code[0]+code[1]:
        market = 'sh'
    elif  '99' == code[0]+code[1]:
        market = 'sh'

    elif '30' ==code[0]+code[1]:
        market = 'sz'
    elif '15' ==code[0]+code[1]:
        market = 'sz'
    elif '20' ==code[0]+code[1]:
        market = 'sz'
    elif '39' ==code[0]+code[1]:
        market = 'sz'
    else:
        market = 'sh'
    return market

#panfu = 'E:/BaiduNetdiskDownload/vipdoc/'
panfu = 'D:\\new_tpyzq_v6\\vipdoc\\'
def tdxread(code):  #day data
    market = marketcode(code)
    #market = str(market)
    reader = TdxDailyBarReader()
    data = reader.get_df(panfu+market+'\\lday\\'+market+code+'.day')
    return data


def tdxread5m (market,code):  # .5 minutes  
    market = str(market)
    code = str(code)
    reader = TdxLCMinBarReader()
    #reader = TdxDailyBarReader()
    df = reader.get_df(panfu+market+'/fzline/'+market+code+'.lc5')
    return df 
#df = tdxreadm('sh','600718')
#df.to_csv('E:/BaiduNetdiskDownload/template/data/input_data/stock_data/tdx5minutes.csv')
#print(df.head())
#print(df.tail())  
#dfr = pd.DataFrame()
def tdxreadm (code):  # 1 minutes
    market = marketcode(code)
    code = str(code)
    reader = TdxLCMinBarReader()
    #reader = TdxDailyBarReader()
    df = reader.get_df(panfu+'\\'+market+'\\minline\\'+market+code+'.lc1')
    return df 
#df = tdxreadm('sh','600479')
#dfr = pd.DataFrame(columns=['datetimer','openr','highr','lowr','closer','volumer','amountr'])
def toTime (df,minutes):  #30min 
    minutes = str(minutes)
    ohlc_dict = {'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum'}
    df = df.resample(minutes+'T', how=ohlc_dict, closed='left', label='left')
    dfr = pd.DataFrame(columns=['datetimer','openr','highr','lowr','closer','volumer','amountr'])
    dfr['openr'] = df[('Open','open')]
    dfr['highr'] = df[('High','high')]
    dfr['lowr'] = df[('Low','low')]
    dfr['closer'] = df[('Close','close')]
    dfr['volumer'] = df[('Volume','volume')]
    dfr['amountr'] = df[('Volume','amount')]
    df['datetime'] = df.index
    
    dfr['datetimer'] = df['datetime']
    dfr['datetimer'] = pd.to_datetime(dfr['datetimer'])
    #print(df.info())
    dfr = dfr[['datetimer','openr','highr','lowr','closer','volumer','amountr']]
    dfr = dfr[dfr['openr']>0]
    dfr.reset_index(level=0, inplace=True)
    return dfr




#minutes = int(30)
#dfr = toTime(df,minutes)
#minutes = str(minutes)
#print(dfr.info())
#print(dfr.tail()) 
#df.to_csv('E:/BaiduNetdiskDownload/template/data/input_data/stock_data/tdx'+minutes+'min.csv')
