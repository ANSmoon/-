#!/usr/bin/env python
# coding: utf-8

# - project 1 : 최대 부분 배열 문제의 응용
# - author : 문범수(2018114657)
# - date : 2023-04-06


# pip install -U finance-datareader

import matplotlib.pyplot as plt
import datetime
import pandas as pd
import FinanceDataReader as fdr
fdr.__version__
import FinanceDataReader as fdr
import sys

stock_name = sys.argv[1]
start_year = sys.argv[2]
last_year = sys.argv[3]

# 구글(GOOG), 2021년 ~ 2022년
df = fdr.DataReader(stock_name, start_year, last_year)
df['Close'].plot()




df
df['Close'].plot() # 종가기준 주가 변동 추이 그래프




price_cl = {}
price_co = {}




for i in range(len(df['Close'])):
    price_cl[i] = round(df['Close'][i],2) # 소숫점 뒤 2자리 내림
    price_co[i] = round(df['Close'][i],2) # 소숫점 뒤 2자리 내림




dif = {} 
for i in range(len(price_cl) - 1):
    dif[i] = round(price_cl[i + 1] - price_co[i],2) # 소숫점 2자리 까지 가격간 차이 변환




def MaxSubarray(x, low, high):
    if high < low: # 최댓값이 최솟값보다 작은 경우
        return 0, 0, 0

    if high == low: #최댓값과 최솟값이 동일할 경우
        return low, high, x[low]

    else: #나머지 case 3가지 설정
        mid = (low + high) // 2
        (ll, lh, ls) = MaxSubarray(x, low, mid - 1)
        (rl, rh, rs) = MaxSubarray(x, mid + 1, high)
        (cl, ch, cs) = Cross(x, low, mid, high)

        if ls >= rs and ls >= cs: # 모두 왼쪽 배열에 있는경우
            return ll, lh, ls
        elif rs >= ls and rs >= cs: # 모두 오른쪽 배열에 있는경우
            return rl, rh, rs
        else: # 가운데 배열을 포함해서 있는 경우
            return cl, ch, cs

def Cross(x, low, mid, high): #가운데 배열을 포함해서 위치하는 경우
    ls = 0
    rs = 0
    ml = 0
    mr = 0
    index_left = True
    index_right = True

    sum = 0
    for i in range(mid - 1, low - 1, -1):
        sum = sum + x[i]
        if sum > ls:
            ls = sum
            ml = i
            index_left = False

    sum = 0
    for j in range(mid + 1, high + 1, 1):
        sum = sum + x[j]
        if sum > rs:
            rs = sum
            mr = j
            index_right = False

    if index_left:
        ml = mid
    if index_right:
        mr = mid

    return ml, mr, round(ls + rs + x[mid],2)

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


low_index, max_index, max_profit = MaxSubarray(dif,0,len(dif)-1)
max_index = max_index + 1 # 각각의 index 파악



low_price = df['Close'][low_index]
max_price = df['Close'][max_index]



min = df['Close'][0]

for i in df['Close']:
    if i < min:
        max = i
min # 실제 최솟값




df[df['Close'] == min] # 최솟값 위치




max = df['Close'][0]

for i in df['Close']:
    if i > max:
        max = i
max # 실제 최댓값




df[df['Close'] == max] # 최댓값 위치



date = df.index




low_date = date[low_index].date()
max_date = date[max_index].date()




df['Close'].plot()
plt.title(stock_name)
plt.ylabel('price')
plt.xlabel('Date')
plt.vlines(low_date,min-30,df['Close'][low_index],color = 'blue',linestyle = '--',linewidth = 2)
plt.vlines(max_date,min-30,df['Close'][max_index],color = 'red',linestyle = '--',linewidth = 2)

print('종목 : GOOG','매입날짜 : ' , low_date, '매도날짜 : ' ,max_date,'총수익',max_profit,'$')
