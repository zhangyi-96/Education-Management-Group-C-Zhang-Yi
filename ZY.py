#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 数据字典
data = {
    "Copenhagen": [15.4,17.0,17.7,18.2,18.4,18.7,18.7,18.3,18.1,17.0],
    "Dnipro": [9.5,9.9,11.8,11.5,12.7,11.8,11.2,10.7,9.7,10.1,],
    "Minsk": [11.8,13.2,12.9,13.4,14.0,13.0,13.2,13.7,12.4,11.7],
    "St. Gallen":[15.0,16.7,17.6,17.4,17.6,17.3,16.8,16.8,16.9,15.2],
    "Muscat":[9.2,10.3,10.1,10.0,9.6,9.9,10.3,10.8,9.7,9.1],
    "Samara":[10.8,11.3,11.7,11.8,11.2,12.2,12.2,12.2,12.4,11.6],
    "Zurich":[13.2,15.0,15.8,16.3,16.4,16.6,17.2,17.0,17.6,16.5],
    "Boston":[16.0,17.8,18.6,18.9,18.2,18.6,18.7,18.1,18.2,16.8],
    "Bonn":[12.1,13.5,14.1,14.0,15.4,14.4,15.2,15.5,16.0,14.7],
    "Chengdu":[9.9,11.1,12.3,13.4,14.4,15.4,15.7,16.0,15.9,14.8],
    "Seoul":[9.7,12.1,13.3,14.1,14.4,15.3,16.0,16.8,17.3,17.5,],
    "Riyadh":[6.1,6.8,6.7,7.9,7.6,7.6,6.3,6.4,7.1,6.6],
    "Nottingham":[11.3,13.9,14.7,14.4,15.3,16.4,16.4,16.7,16.3,14.7],
    "Athens":[5.8,5.6,5.9,6.3,6.2,5.9,5.6,4.8,4.7,6.2],
    "Istanbul":[6.5,6.6,6.7,6.5,7.0,7.2,7.5,7.8,7.8,7.6],
    "Melbourne":[7.8,10.5,12.8,13.6,15.1,15.8,16.2,16.5,17.1,15.9],
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




