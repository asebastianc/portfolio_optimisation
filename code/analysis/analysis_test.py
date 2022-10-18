import pandas as pd
from pingouin import mwu
import sys

df_1 = pd.read_csv("../../results/alg1/alg1_results.csv")
df_1 = df_1.iloc[:, -2:]
df_1 = df_1.replace("-", 0)
df_1 = df_1[df_1["Return"] != 0]
df_1.to_csv("../../results/alg1/alg1_data_test.csv", index = False)

df_2 = pd.read_csv("../../results/alg2/alg2_results.csv")
df_2 = df_2.iloc[:, -2:]
df_2 = df_2.replace("-", 0)
df_2 = df_2[df_2["Return"] != 0]
df_2.to_csv("../../results/alg2/alg2_data_test.csv", index = False)

test_return = mwu(df_1["Return"].astype(int),  df_2["Return"].astype(int))
test_risk = mwu(df_1["Risk"].astype(int),  df_2["Risk"].astype(int))

sys.stdout = open("../../results/mann_whitney_tests.txt", "w")
print("Mann-Whitney U Test Return:")
print(test_return)
print("*" * 58)
print("Mann-Whitney U Test Risk:")
print(test_risk)