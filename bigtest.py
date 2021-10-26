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
#print(fish_target)

#7. 데이터 셔플(샘플 편향 막아내기) 

indexs = np.arange(49)
np.random.shuffle(indexs)
#print(indexs)
fish_data = fish_data[indexs]
fish_target = fish_target[indexs]
#print(fish_data)
print(fish_target)

#8. 훈련데이터와 테스트 데이터로 나누기 (8:2)
train_data = fish_data[:39]
train_target =fish_target[:39]
test_data = fish_data[39:]
test_target= fish_target[39:]

#9.훈련데이터 시각화하세요
plt.scatter(train_data[:,0],train_data[:,1])
#plt.show()

#10.데이터를 판다스로 변경하기(train,test)

#(1)트레인데이터
print(train_target.shape)
train_target = train_target.reshape(39,1)

train = np.hstack((train_data,train_target))

train_dataFrame =pd.DataFrame(train,columns=["train_length","train_weight","train_target"])
print(train_dataFrame)

#(2) 테스트데이터
train_target = train_target.reshape(10,1)
test = np.hstack((test_data,test_target))
test_dataFrame =pd.DataFrame(test,columns=["test_length","test_weight","test_target"])
print(train_dataFrame)

#train_dataFrame = pd.DataFrame()
#print(train_data.shape)
#print(train_data)
#print(train_target)

#11. 데이터 넣기 (insert) 
engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")
train_dataFrame.to_sql("train",engine, index=False,if_exists="replace")
test_dataFrame.to_sql("test",engine, index=False,if_exists="replace")

