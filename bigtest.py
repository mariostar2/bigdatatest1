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
plt.show()
