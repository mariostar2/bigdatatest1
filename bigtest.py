#1.임포트하기(라이브러리 설치완료)
import numpy as np
import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt

#3.경로 지정 (로드)
bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
bream_weight = pd.read_csv("bream_weight.csv").to_numpy().flatten()
smelt_length = pd.read_csv("smelt_length.csv").to_numpy().flatten()
smelt_weight = pd.read_csv("smelt_weight.csv").to_numpy().flatten()
#print(bream_length)

#4.시각화하기(csv)
plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length,smelt_weight)
#plt.show()


#5.합치기 도미 빙어데이터 (길이와 무게)
fish_length = np.concatenate((bream_length, smelt_length))
fish_weight = np.concatenate((bream_weight, smelt_weight))

fish_data =  np.column_stack((fish_length,fish_weight))
#print(fish_data)

#6. 타겟 데이터 만들기 
#print(bream_length.shape)
#print(smelt_length.shape)

fish_target = np.concatenate((np.ones(35),np.zeros(14)))
print(fish_target)

 