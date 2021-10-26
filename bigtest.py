#1.임포트하기
import numpy as np
import pandas as pd
import sqlalchemy as db

bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
print(bream_length)

