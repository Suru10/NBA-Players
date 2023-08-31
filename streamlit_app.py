#import libraries
import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

# Team 1: Seth F., Kavya -> bottom
# Team 2:emilia, Jemiah -> top
#Introductions:
st.subheader('Tranquil Tiramisus')

st.write(
  'Hi, my name is Seth Fung and I reside in BC Canada. I just started to learn coding this year and look forward to continuing to code.'
)
st.write(
  'Hi! I am Kavya and I am a sophomore. I live in Washington. I have coding experience in mostly HTML, Java, and Python. I have created a few projects and I am so excited to continue expanding my knowledge on coding.'
)
st.write(
  'Hi, Im emilia and Im 16 years old going on my senior year. I live in San Diego, CA. I have got experience in HTML, JavaScript, and python.'
)
st.write(
  'Hi, my name is Jemiah! I am 16 and I live in Alberta, Canada. I am new to coding and I look forward to broadening my experiences with coding and technology.'
)
#Title:
st.title("GPA and IQ EDA")
st.write(
  "This dataset looks at 78 students and 5 variables: obs, gpa, iq, gender, and concept. We will look at how each of the variables affect each other."
)
df = pd.read_csv(
  "https://raw.githubusercontent.com/Suru10/GPA-and-IQ/main/gpa_iq.csv")
st.subheader('Inspection')
# st.divider()
st.write('Lets take a quick look at the data')
st.write(df.head())
st.write("Description of the data")
st.write(df.describe())
st.write("Shape of the data -rows and columns")
st.write(df.shape)
st.write(
  'There are only three relevent points: gpa, gender, and iq - all of which are represented as numerical values. We dropped the columns labeled obs and concept due to their irrelevance'
)

# Inspection
# head
#df.head()
#df.describe()
#df.shape

# Cleaning
# There is no missing info
st.divider()
st.title("Cleaning the Data")
st.write(
  "To clean the dataset we removed columns that were not relevant to our analysis as well as checked if the data had null values and there were none."
)
st.write("Post-processing head")
columns_dropped = ["obs", "concept"]
df.drop(columns_dropped, axis=1, inplace=True)
st.write(df.head())
st.write("Post-processing null vaues")
st.write(df.isna().sum())

# Visualizations:
# Team 1: Kavya, Seth
# Team 2:Jemiah, emilia

st.divider()

st.header("Hypothesis 1: What is the correlation between IQ and GPA?")
# code the visual
st.write("Plot 1a")
fig1 = plt.figure(figsize=(10, 4))
sns.lineplot(x="iq", y="gpa", data=df)
st.pyplot(fig1)

st.write("Plot 1b")
fig2 = plt.figure(figsize=(10, 4))
sns.lineplot(x="iq", y="gpa", hue="gender", data=df)
st.pyplot(fig2)

st.write("Plot 1c")
fig3 = px.scatter(df, x="iq", y="gpa", color="gender")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Analysis")
st.write(
  "My initial hypothesis for the question What is the correlation between IQ and GPA? was that a higher IQ would lead to a higher GPA. So to test this hypothesis, I created graphs with x = IQ and y = GPA:"
)
st.write(
  "Two line graphs, one showing the average IQ to GPA relation between both genders and another showing the IQ to GPA relation for each gender, with pink = gender 1 and black = gender 2."
)
st.write(
  "Both of these graphs displayed a strong-positive correlation of IQ to GPA for gender 1 and a weak-positive correlation of IQ to GPA for gender 2; which roughly proved my initial hypothesis that as IQ increases, so does GPA."
)

st.write(
  "To further solidify the initial conclusion, I created a third graph/ a scatter plot where x = IQ and y = GPA and gender 1 = Blue and gender 2 = Yellow. Much like the previous graphs, the scatter plot showed that there was a strong-positive correlation of IQ to GPA for gender 1 and a weak-positive correlation of IQ to GPA for gender 2."
)
st.write(
  "It is very important to note that the data was inconsistent; there were many outliers in the data, for example, the person with the highest IQ in both genders had a lower GPA than some people who had lower IQ, not to mention that there were many other spikes in the graphs that displayed someone with a lower IQ having a far higher GPA than that of someone with higher IQ. And at some points in the graphs, it seemed as if as IQ increases, GPA decreases."
)
st.write(
  "Despite all that, the trends of the graphs do show weak and strong positive correlations between IQ and GPA for both genders which tells us that generally speaking, IQ does somewhat correlate to GPA."
)
st.write(
  "In conclusion, IQ somewhat affects GPA and in general, when you have a higher IQ, you will also have a higher GPA. This may not be the case for everyone though as this data set excluded the students environments, as well as numerous other factors that also affect GPA."
)
st.divider()

st.header("Hypothesis 2: Is there a correlation between IQ and Gender?")

st.write("Plot 2a")
fig4 = plt.figure(figsize=(10, 4))
sns.lineplot(x='gpa', y='gender', hue='iq', data=df)
st.pyplot(fig4)

st.write("Plot 2b")
sns.set_theme()
fig5 = plt.figure(figsize=(10, 4))
sns.scatterplot(x="gpa", y="iq", hue="gender", data=df)
st.pyplot(fig5)

#st.write("Plot 2c")
#fig6 = plt.figure(figsize=(10, 4))
#df.plot.scatter(x='iq', y='gpa')
#st.pyplot(fig6)

st.write("Plot 2c")
sns.set_theme()
fig6 = plt.figure(figsize=(10, 4))
sns.scatterplot(x="iq", y="gender", hue="gpa", data=df)
st.pyplot(fig6)

st.write("Plot 2d")
fig7 = plt.figure(figsize=(10, 4))
sns.barplot(x='gender', y='iq', estimator='std', data=df)
st.pyplot(fig7)

st.subheader("Analysis")

st.write(
  "Initially, I assumed there would be no correlation whatsoever between gender and iq, but upon furthur analysis of the data it seems that according to this study one gender is slightly superior in this measure."
)

st.write(
  "The difference is so slight it was difficult to notice within scatterplots and line graphs, but a barplot gave a much clearer picture. Gender 1 was shown to have on average a higher iq than gender 2, but alas, no one knows which gender is which."
)

st.write(
  "In conclusion, gender seems to have a correlation to an individual's iq, albeit extraodinarily slight and dependent on a rather dodgy dataset."
)

st.divider()

st.header("#Hypothesis 3: Does gender affect gpa?")
st.write(
  'Before I examined the data, my hypothesis for the question "Does gender affect GPA?" was no. I did not believe there was any correlation. To determine if this was true I made a scatter plot to see if there was any correlation.'
)
st.write("Plot 3a")
fig1 = px.scatter(
  df,
  x="gpa",
  y="gender",
  color="gpa",
)
st.plotly_chart(fig1, use_container_width=True)
st.write(
  'For both gender 1 and gender 2, the gpa values seem to be in a straight line, which means that each gender had a variety of GPA values. This shows that there is no correlation.'
)
st.write(
  'However, gender 2 did have a few people who had lower GPAs than gender 1. This might just be a coincidence or it might show that gender 2 typically has a smaller minimum GPA than gender 1. Also, it did seem like gender 2 had more GPA values below four than gender 1. To examine this further, I took the average gpa for both genders and made a bar plot. '
)
st.write("Plot 3b")
new_df = df.groupby('gender')['gpa'].mean()
figbar = px.bar(new_df, y="gpa")
st.plotly_chart(figbar, use_container_width=True)

st.write(
  "The bar plot showed that gender 1 had a slightly higher average GPA. So, According to the data, there is mostly no correlation between gender and GPA. However, gender 1 tends to have somewhat higher GPAS."
)

st.divider()
st.header("#Hypothesis 4: Correlation Heatmap")
st.write(
  "To show how GPA, IQ, and gender correspond to each other I made a correlation heatmap that compares all the possible relations through color. "
)
st.write("Plot 4a")
df_heatmap = plt.figure()  # imp! create a fig.
sns.heatmap(
  df.corr(),
  vmin=-1,
  vmax=1,
  annot=True,
  cmap='BrBG',
)
#df_heatmap.set_title('Correlation Heatmap', fontdict={'fontsize': 12}, pad=12)
st.pyplot(df_heatmap)

st.write(
  'The colorbar on the right displays a gradient going from a dark teal to light gray to dark orange. The darkest teal represents a perfect positive correlation at 1,the light gray in the very middle represents no correlation at 0, and the darkest orange represents a perfect negative correlation at -1. Disregarding the correlation each of the variables to itself, all of which had the darkest teal(1), the highest correlation was between IQ and GPA with a moderate teal color and a value of 0.63. Gender and IQ had a much lower correlation with the color being a light teal and the value 0.19. The relationship with the least correlation was between gender and gpa with a light orange color and a value of -0.097.'
)
st.write(
  'To reinforce this I created a scatter matrix showcasing and comparing all the relationships.'
)

st.write("Plot 4b")
df_list = df[['gpa', 'iq', 'gender']]
df_scatter = px.scatter_matrix(df_list)
st.plotly_chart(df_scatter, use_container_width=True)
st.write(
  ' Here it shows GPA and IQ as a weak positive correlation. While gender can be observed as having no correlation to either IQ or GPA, it can be seen very slightly on the correlation heatmap and scatter matrix that gender has a weak correlation to both GPA and IQ due to only a small amount of values.'
)

st.title("Conclusion")
st.write(
  "To summarize our 4 analyses on the correlations between GPA, IQ, and Gender, we reached the conclusion that generally speaking, those with a higher IQ would tend to have a higher GPA. We also came to the conclusion that gender has little to no effect on IQ and GPA."
)
st.write(
  "In conclusion, there is a slight positive correlation between IQ and GPA, and there is a very slight correlation between gender and IQ and gender and GPA."
)
