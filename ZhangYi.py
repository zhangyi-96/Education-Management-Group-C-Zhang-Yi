#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 数据字典
data = {
    "Copenhagen": [14.1, 14.1, 13.7, 12.9, 12.3, 11.7, 10.8, 10.6, 9.8, 5.3],
    "Dnipro": [11.0, 12.6, 12.1, 11.2, 11.3, 10.5, 9.5, 10.3, 9.0, 8.7],
    "Minsk": [12.8, 12.3, 12.6, 12.3, 11.8, 9.9, 9.9, 8.4, 8.3, 6.9],
    "St. Gallen":[13.7,12.8,12.4,10.6,11.0,10.7,10.1,9.5,7.4,3.0],
    "Muscat":[9.5,11.0,11.5,10.3,9.8,10.3,10.2,10.1,9.6,7.5],
    "Samara":[10.8,11.5,11.7,11.3,10.3,10.2,8.7,8.2,8.2,5.6],
    "Zurich":[11.1,12.2,10.8,10.6,8.5,7.1,7.4,7.3,6.2,3.7],
    "Boston":[13.0,12.7,12.7,11.4,11.0,10.1,9.1,6.2,4.2,2.9],
    "Bonn":[10.9,10.8,11.5,10.7,10.7,9.4,7.7,8.6,7.4,4.0],
    "Chengdu":[10.0,10.0,10.2,10.0,9.1,7.7,6.6,6.0,4.5,2.4],
    "Seoul":[8.2,9.1,9.9,9.7,9.0,8.6,7.9,7.1,5.9,3.8],
    "Riyadh":[8.0,7.7,7.2,7.9,7.9,7.8,8.1,8.3,7.5,5.9],
    "Nottingham":[10.9,10.5,9.1,9.0,8.1,5.4,5.3,4.7,4.1,2.4],
    "Athens":[8.1,6.3,6.4,6.3,6.7,6.3,5.9,6.3,5.9,5.4],
    "Istanbul":[8.9,9.0,8.4,6.9,5.8,4.5,3.9,3.2,2.2,1.4],
    "Melbourne":[8.2,7.3,6.3,6.0,5.4,5.1,4.3,3.2,2.3,1.3],
}

# 创建 DataFrame
df = pd.DataFrame.from_dict(data)

# 计算每个城市的平均值和标准差
means = df.mean()
std_devs = df.std()

# 打印平均值和标准差
print("平均值:")
print(means)
print("\n标准差:")
print(std_devs)

# 绘制折线图
plt.figure(figsize=(10, 6))
for city in df.columns:
    plt.plot(df.index, df[city], label=city, marker='o')  # 添加 marker 提升可读性

# 添加平均值和标准差到图中
for i, city in enumerate(df.columns):
    plt.text(len(df) - 1, df[city].iloc[-1], 
             f"Avg: {means[i]:.2f}\nStd: {std_devs[i]:.2f}", 
             fontsize=10, verticalalignment='center', 
             horizontalalignment='left')

# 图形设置
plt.title("多变量折线图及统计量")
plt.xlabel("时间点")
plt.ylabel("值")
plt.xticks(df.index)  # 确保 X 轴显示每一个时间点
plt.legend()
plt.grid(True)
plt.tight_layout()

# 显示图形
plt.show()


# In[ ]:




