#!/usr/bin/env python
# coding: utf-8

# - project 2 : 하노이 탑 응용
# - author : 문범수(2018114657)
# - date : 2023-04-06

# In[43]:
import sys

x = int(sys.argv[1])
def moving(x, start, last, sub): # 1 <= x <= 20
    
    if x == 1: #만약 기둥에 원반이 1개만 있을 경우
        print(start, '번 기둥에서 ', last, '번 기둥으로 ', x, '번 원반 이동')
        return
    
    elif x > 20:
        print("원반은 1개 이상 20개 이하여야 합니다.")
    
    moving(x-1, start, sub, last) #먼저 sub(보조) 기둥에 맨 마지막 원반을 제외한 원반 이동
    print(start, '번 기둥에서 ', last, '번 기둥으로 ', x, '번 원반 이동')
    moving(x-1, sub, last, start) #도착지점에 남겨둔 원반 이동
    
    return

def count(x):  # 옮긴 횟수 구하는 함수
    if 20 >= x > 1:
        return 2*count(x-1) + 1
    else:
        return 1

print('총 움직인 횟수 : ',count(x), '번')
moving(x,1,3,2)

