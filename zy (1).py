#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置图形主题
sns.set(style="whitegrid")
# 读取数据
imdb_df = pd.read_csv('imdb_top_250.csv')
douban_df = pd.read_csv('douban_top_250.csv')

# 显示数据概况
print(imdb_df.head())
print(douban_df.head())
# 计算平均评分
imdb_avg_rating = imdb_df['rating'].mean()
douban_avg_rating = douban_df['rating'].mean()

# 可视化平均评分比较
avg_ratings = {'IMDb': imdb_avg_rating, '豆瓣': douban_avg_rating}
plt.figure(figsize=(8, 5))
sns.barplot(x=list(avg_ratings.keys()), y=list(avg_ratings.values()))
plt.title('平均评分比较')
plt.ylabel('平均评分')
plt.show()
# 找到重叠电影
imdb_titles = set(imdb_df['title'])
douban_titles = set(douban_df['title'])
overlap_titles = imdb_titles.intersection(douban_titles)

# 打印重叠的电影
print("重叠的电影数量:", len(overlap_titles))
print("重叠的电影:", overlap_titles)
# 转换年份为整数
imdb_df['year'] = imdb_df['year'].apply(lambda x: int(x.split(' ')[-1]))
douban_df['year'] = douban_df['year'].apply(lambda x: int(x.split(' ')[-1]))

# 可视化年份分布
plt.figure(figsize=(12, 6))
sns.histplot(imdb_df['year'], bins=20, label='IMDb', color='blue', kde=True)
sns.histplot(douban_df['year'], bins=20, label='豆瓣', color='orange', kde=True)
plt.title('发布年份分布')
plt.xlabel('年份')
plt.ylabel('电影数量')
plt.legend()
plt.show()
# 将类型列拆分为多行
imdb_types = imdb_df['genres'].str.get_dummies(sep=',').sum().reset_index()
douban_types = douban_df['genres'].str.get_dummies(sep=',').sum().reset_index()

# 重命名列
imdb_types.columns = ['Genre', 'IMDb']
douban_types.columns = ['Genre', '豆瓣']

# 合并数据
merged_types = pd.merge(imdb_types, douban_types, on='Genre', how='outer').fillna(0)

# 可视化类型分布
plt.figure(figsize=(12, 6))
merged_types.set_index('Genre').plot(kind='bar', stacked=True)
plt.title('类型分布比较')
plt.ylabel('电影数量')
plt.xlabel('类型')
plt.xticks(rotation=45)
plt.show()
# 统计导演出现次数
imdb_directors = imdb_df['director'].value_counts().reset_index()
douban_directors = douban_df['director'].value_counts().reset_index()

# 重命名列
imdb_directors.columns = ['Director', 'IMDb Count']
douban_directors.columns = ['Director', '豆瓣 Count']

# 合并数据
merged_directors = pd.merge(imdb_directors, douban_directors, on='Director', how='outer').fillna(0)

# 可视化导演分布
plt.figure(figsize=(12, 6))
merged_directors.set_index('Director').head(10).plot(kind='bar')
plt.title('出场最多的导演')
plt.ylabel('电影数量')
plt.xlabel('导演')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




