# -*- coding: utf-8 -*-
"""Copy of task01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tCd6KunFLPqfGl5MTxFl3Ge6phdF_kwB
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import scipy
import seaborn as sns

data=pd.read_csv("/content/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_84031.csv")

data.head()

# @title Region vs IncomeGroup

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['IncomeGroup'].value_counts()
    for x_label, grp in data.groupby('Region')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('Region')
_ = plt.ylabel('IncomeGroup')

data.shape

data.info()

data.tail()

gender_counts = data['Region'].value_counts()
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='muted')
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Distribution of Region')
plt.xticks(rotation=90)
for x, y in enumerate(gender_counts.values):
  plt.text(x, y, str(y), ha='center', va='bottom')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show

country_metadata = pd.DataFrame({
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France', 'Japan', 'China'],
    'Region': ['North America', 'North America', 'Europe', 'Europe', 'Europe', 'Asia', 'Asia']
})
plt.figure(figsize=(8, 6))
country_metadata['Region'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.title('Histogram of Regions in Country Metadata')
plt.grid(axis='y', alpha=0.75)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()