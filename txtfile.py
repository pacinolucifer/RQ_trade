# -*- coding: utf-8 -*-
'''
Created on %(date)s
Author: Lucifer yue
To update your source code.
'''

import os
import sys
#import urllib3
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import talib
#import scipy.stats
#from scipy import stats
import tushare as ts
#import seaborn as sns
#import math
#import FuncationData as fd
#import FuncationTalib as ft
#import tosignal as tosig
import tdxpy4 as tdx
#%matplotlib qt5

mytoken = '376bf5201feaf8875d52aa16d8cc0799a2c28dbca9186dd1aaf11937'
print(ts.__version__)
ts.set_token(mytoken)
pro = ts.pro_api()
#df000878 = pro.daily(ts_code='000878.SZ', start_date='20190103') #, end_date='20180718')


def today ():
    today = datetime.date.today()
    today=today.strftime('%Y-%m-%d')
    return today
day = today()
#日期	证券代码	证券简称	股票数量(股)	现金替代标志	现金替代溢价比率	替代金额

res = 'E:\\BaiduNetdiskDownload\\ETF申赎\\ETF300申赎.xlsx'
filename = 'E:\\BaiduNetdiskDownload\\ETF申赎\\5103000111.txt'
res_df =pd.read_excel(res)

# def EtfSS():  #ETf510300 申赎
with open(filename, 'r') as file_to_read:
     lines_list = file_to_read.readlines() # 全部读取数据
     lines_list = lines_list[14:-2] #去掉非股票信息
     if not lines_list:
         print('It is empty.')
     else:
         lines_list_len = len(lines_list)
         res_df_rows = res_df.shape[0]
         for ix,info in enumerate(lines_list):
             #print(ix,info)
             info = info.split('|')
             res_df.loc[ix+res_df_rows,'日期']= day
             res_df.loc[ix+res_df_rows,'证券代码']= str(info[0])
             res_df.loc[ix+res_df_rows,'证券简称']= info[1]
             res_df.loc[ix+res_df_rows,'股票数量(股)']= info[2].strip()
             res_df.loc[ix+res_df_rows,'现金替代标志']= info[3]
             res_df.loc[ix+res_df_rows,'现金替代溢价比率']= info[4]
             res_df.loc[ix+res_df_rows,'替代金额']= info[5].strip()
         if ix+1 >298:
             print('Master,All stock are ok: ',ix)
             res_df['股票数量(股)']= pd.to_numeric(res_df['股票数量(股)'],errors='coerce')
             res_df['替代金额']= pd.to_numeric(res_df['替代金额'],errors='coerce')
             res_df['现金替代溢价比率']= pd.to_numeric(res_df['现金替代溢价比率'],errors='coerce')
             res_df.fillna(0,inplace=True)
             #res_df.to_excel('ETF300申赎.xlsx')
             print('res_df is good.')
         else:
              print('My master,Something is wrong.')
              #data['所属组'] = pd.to_numeric(data['所属组'], errors='coerce').

def marketcode(code):
    code = str(code)
    if '60' == code[0]+code[1]:
        code = code + '.SH'
    elif '00' == code[0]+code[1]:
        code = code + '.SZ'
    elif '30' == code[0]+code[1]:
        code = code + '.SZ'
    return code

def GetClose(df):
     # today = datetime.date.today()
     # today = today.strftime('%Y%m%d')
     counter = 0
     js = 0
     for ix,code_name in enumerate(df['证券代码']):
         code_name = marketcode(code_name)
         js = js +1
         try:
            code_df = pro.daily(ts_code=code_name, start_date='20190108')  # , end_date='20180718')
            #rows = code_df.shape[0]
            code_df_col_list = code_df.columns.tolist()
            #code_df_col_list = code_df_col_list [2:]
            for key in code_df_col_list:
                df.loc[ix,key]  = code_df.loc[0,key]
         except:
             print('A error data :',code_name)
             counter = counter + 1
             print('counter: ',counter)
             pass
         if js >100:
             time.sleep(10)
             js = 0
             print('js is 100 to wait.')
         # df.loc[ix,'open'] = code_df.loc[rows - 1, 'open']
         # close = code_df.loc[rows-1,'close']
         # high = code_df.loc[rows - 1, 'high']
         # low = code_df.loc[rows - 1, 'low']
         # change = code_df.loc[rows - 1, 'change']
         # pct_chg = code_df.loc[rows - 1, 'pct_chg']
         # vol = code_df.loc[rows - 1, 'vol']
         # amount = code_df.loc[rows - 1, 'amount']
     return  df
result_df = GetClose(res_df)






# def main():
    
    
#
# if '__name__' == 'main':
#     main()

