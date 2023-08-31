#import libraries
import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
from datetime import datetime

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('players.csv')
# top (inspection + cleaning)  Riley
# graph 1-5 Warik
# graph 6-7 + conclusion Natalie
st.subheader('Fancy Fondue')
st.write(
  'Hi my name is Riley, I am a sophomore, and I have experience with python,pandas, plotly, and torch, and have been programming with multiple languages in the past 2.5 years.'
)
st.write('--------WARIK—--------')
st.write('--------------NATALIE—------------')

#TITLE
st.title('NBA Player Statistics EDA')
st.write(
  "This dataset was formulated for the statistics of NBA players. This includes Data about all NBA players active during 2022-2023 season including: First and last name, Position, Height and weight, Date of birth, Country of origin, Last attended school and Draft info. We utilized this raw data and got a better understanding of the statistics of NBA players. The Dataset was sourced from kaggle and last updated on August 14th 2023."
)

#Inspection:
st.header('Inspection')
st.markdown("""---""")
# 1) Showing some Data
st.subheader('LET\'S LOOK AT THE DATA')
st.write(df.head())
st.write('Here we are displaying a small portion of what our data looks like')
st.write("\n")
col1, col2 = st.columns(2)
# 3) Null values
col1.markdown('NULL VALUES')
col1.write(df.isna().sum())
col1.write('Here we are displaying the number of null values for each feature')
# 4) Stat Values
col2.markdown('THE STATS')
col2.write(df.describe())
col2.write('These are the statistical values of the current quantitative data')
st.write("\n")
st.subheader("Inspection Summary")
st.markdown(
  "In inspection we learned, the min and max values of the quantatitive values, we learned about which possible features we should drop in our dataset, and we learned where our null values are. "
)
st.markdown("""---""")

#Cleaning:
st.header('Cleaning the Data')
#Removing all rows that contain null values
col1, col2 = st.columns(2)
col1.markdown('NULL VALUES BY COLUMN')
col1.write(df.isna().sum())
df[['Feet', 'Inches']] = df['height'].str.split('-', expand=True)
df['HeightInches'] = df['Feet'].astype(int) * 12 + df['Inches'].astype(int)
df = df.drop(['Feet', 'Inches'], axis=1)
columns_to_drop = df[['draft_round', 'draft_number']]
df.drop(columns_to_drop, axis=1, inplace=True)
df.head(1)
#filtered_df = df[df[['fname', 'lname', 'school']].isna().any(axis=1)]
df.loc[28, 'school'] = "Saint Joseph's Preparatory School"
df.loc[50, 'school'] = "Argentina"
df.loc[81, 'school'] = "Cordoba High School"
df.loc[120, 'school'] = "Saint Mary's"
df.loc[192, 'school'] = "Little Elm"
df.loc[210, 'school'] = "Spain"
df.loc[231, 'school'] = "Brazzaville High School"
df.loc[313, 'school'] = "EuroLeague"
df.loc[368, 'school'] = "Trinity International School"
df.loc[453, 'school'] = "EuroLeague"
df["Date coverted"] = pd.to_datetime(df["birthday"])
col2.markdown('AFTER CLEANING')
col2.write(df.isna().sum())
st.subheader("Reasoning:")
st.write(
  "Dropped all rows with null values contained in them, and rows that served no purpose for further data analysis. This was necessary in order to keep a consistent dataset with the least amount of gaps. We also manually researched the data to completely fill up the ‘school’ column."
)
st.markdown("""---""")
#Removing the 'playerid' Column
col1, col2 = st.columns(2)
column_to_drop = ['playerid']
df.drop(column_to_drop, axis=1, inplace=True)
col1.markdown("DATA AFTER REMOVING THE ‘'playerid’ COLUMN")
col1.write(df.head(5))
col2.subheader("Reasoning:")
col2.write(
  "Dropped the ‘playerid’ column as it was not needed for the analysis and would serve no value to answering any of the hypotheses."
)
st.markdown("")

# Visualizations:
st.header('The Organized Data')
st.subheader("HYPOTHESIS 1: What is the average height of an NBA player?")
average_height_inches = df['HeightInches'].mean()
fig1 = px.box(df, y='HeightInches', labels={'HeightInches': 'Height (inches)'})
fig1.update_layout(title='Height Distribution')
st.plotly_chart(fig1)

# Summary
st.write(
  "I found average player height tallest player height and shortest player height tallest height was 80 inch average was 78 inch and the shortest height was 68 inch"
)

st.title("Hypothesis 2: Most common name of NBA players")
#code
fc = df['fname'].value_counts()
# fc = fc.rename(columns={
#   'index': 'fnames',
#   'fname': 'counts'
# })  # Renaming columns

print(fc.head())

# fig = px.bar(fc, x='fnames', y='counts')
fig = px.bar(fc)
st.plotly_chart(fig, use_container_width=True)

st.write(
  " I found out from the bar graph and data chart that the most common first name is Jalen."
)

st.title("Hypothesis 3: What school have highest yield for draft picks")
#code
fc = df['school'].value_counts()
# fc = fc.rename(columns={
#   'index': 'school',
#   'school': 'count'
# })  # Renaming columns

fig = px.bar(fc)  # Use 'school' as the x-axis
st.plotly_chart(fig, use_container_width=True)
st.write(
  "The graph and chart showed me that the school with the highest yield for draft picks is Kentucky."
)

st.title("Hypothesis 4: What's the average weight?")
fig1 = px.box(df['weight'])
st.plotly_chart(fig1, use_container_width=True)
st.write(
  "From this graph we can see that the median weight for an NBA player is 215 pounds. The minimum weight was 160 pounds, while the maximum was 290. From this graph we can see how much the average NBA player weighes as a median value, and other values."
)

st.title("Hypothesis 5:Most common birth year aka average age ")

df['birthday'] = pd.to_datetime(df['birthday'])

now = datetime.now()
df['age'] = (now - df['birthday']).astype('<m8[s]')

fig2 = px.scatter(df, x='birthday', y='age')

fig2.update_layout(title='Average Age', xaxis_title='', yaxis_title='Age')
st.plotly_chart(fig2, use_container_width=True)

st.write(
  "Another Hypothesis of mine would be that the players with the higher ages have better average stats than those under 30. As the players above 30 have prved themselves through long careers and the under 20 players are mostly rookies and players who will have shorter careers. Here we examine the average age of an NBA player. as we can see, the age is generally under 30 with consistant players. After age 30 the amount of players starts to drop off."
)

st.title("Hypothesis 6: Height Weight Correlation")
fig = px.scatter(df, x='HeightInches', y='weight')
fig.update_layout(title='Height and Weight Correlation',
                  xaxis_title='Height (Inches)',
                  yaxis_title='Weight (Pounds)')
st.plotly_chart(fig, use_container_width=True)

st.write(
  "In this graph we set out to examine the corralation between player's height and weight. We can tell from the graph below that weight and height are heavily correlated,the graph shows that the height/weight correlation works in acending values of weight based on increasing height. We observe a range of weight for evry height, but the incline of height-weight is consistant"
)

st.header("Hypothesis 7: Height Weight Correlation to Position")
avg_hw_data = df.groupby('position')[['HeightInches',
                                      'weight']].mean().reset_index()

fig3 = px.bar(avg_hw_data,
              x='position',
              y=['HeightInches', 'weight'],
              title='Average Height and Weight by Position',
              labels={
                'position': 'Position',
                'value': 'Value'
              },
              color_discrete_map={
                'HeightInches': 'blue',
                'weight': 'red'
              })

fig3.update_layout(barmode='group', xaxis_title='Position')
fig3.update_yaxes(
  title_text='Average Value, Blue is in Inches, Red is in Pounds')

st.plotly_chart(fig3, use_container_width=True)
st.write(
  "In this Graph we looked at the correlation between players weight/height and position. Based on the presuppostion that NBA players are selected for there respective postion based on physical factors. The chart confirms our hypothesis, with centers having the highest average height and weight."
)

st.title("Conclusion")
st.write("write small paragraph about dataset, and what you found out")
