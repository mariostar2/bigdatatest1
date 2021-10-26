#1.임포트하기
import numpy as np
import pandas as pd
import sqlalchemy as db

#2.경로 지정 (로드)
bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
bream_weight = pd.read_csv("bream_weight.csv").to_numpy().flatten()
smelt_length = pd.read_csv("smelt_length.csv").to_numpy().flatten()
smelt_weight = pd.read_csv("smlet_weight.csv").to_numpy().flatten()
#print(bream_length)

