import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

st.write("""
# Tipping charts and miscellaneous information for an unnamed eatery
         
Shows ways in which you can observe how much people like (not) to leave tips
         
""")


path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)



start_date = '2023-01-01'
end_date = '2023-01-31'
dates = pd.date_range(start=start_date, end=end_date, periods=len(tips))
tips['time_order'] = np.random.choice(dates, len(tips))
st.line_chart(tips, x = 'time_order', y = 'tip')

st.scatter_chart(tips, x = 'total_bill', y = 'tip')

st.line_chart(tips[['total_bill', 'tip', 'size']])

st.scatter_chart(tips, x = 'day', y = 'total_bill')


sns.catplot(x='day', y='total_bill', data=tips, kind='bar')
plt.xlabel('День недели')
plt.ylabel('Размер счета')
plt.title('Связь между днем недели и размером счета')
plt.show()
st.pyplot(plt)



tip_lunch = tips[tips['time'] == 'Lunch']['tip']
tip_dinner = tips[tips['time'] == 'Dinner']['tip']

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(tip_lunch, bins=10, color='lightpink')
plt.xlabel('Чаевые')
plt.ylabel('Частота')
plt.title('Гистограмма чаевых в обед')

plt.subplot(1, 2, 2)
plt.hist(tip_dinner, bins=10, color='salmon')
plt.xlabel('Чаевые')
plt.ylabel('Частота')
plt.title('Гистограмма чаевых во время ужина')
plt.tight_layout()
plt.show()
st.pyplot(plt)

plt.figure(figsize=(8, 6))  
sns.histplot(tips['total_bill'], bins=20, kde=True) 
plt.title('Гистограмма total_bill')
plt.xlabel('Сумма счета')
plt.ylabel('Частота') 
plt.grid(True)  
plt.tight_layout() 
plt.show()
st.pyplot(plt)



plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(data = tips[tips['sex']=='Female'], x = 'sex', y='tip', hue = 'smoker', s = 60, alpha = 0.5)
plt.title('Scatterplot для женщин')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

plt.subplot(1, 2, 2)
sns.scatterplot(data = tips[tips['sex']=='Male'], x = 'sex', y='tip', hue = 'smoker', s = 60, alpha = 0.5)
plt.title('Scatterplot для мужчин')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
st.pyplot(plt)


numeric_df = tips.select_dtypes(include=['number']) #оставим только численные переменные
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Тепловая карта зависимостей численных переменных')
plt.show()
st.pyplot(plt)

