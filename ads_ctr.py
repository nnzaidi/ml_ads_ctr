import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import numpy as np
pio.templates.default = "plotly_white"

data = pd.read_csv("ad_10000records.csv")
# print(data.head())

'''
   Daily Time Spent on Site   Age  ...            Timestamp  Clicked on Ad
0                     62.26  32.0  ...  2016-06-09 21:43:05              0
1                     41.73  31.0  ...  2016-01-16 17:56:05              0
2                     44.40  30.0  ...  2016-06-29 10:50:45              0
3                     59.88  28.0  ...  2016-06-21 14:32:32              0
4                     49.21  30.0  ...  2016-07-21 10:54:35              1

[5 rows x 10 columns]

Clicked on Ad: [0] not clicked, [1] clicked
'''

# Converting values in column 'Clicked on Ad'
data['Clicked on Ad'] = data['Clicked on Ad'].map({0: 'No',
                                                   1: 'Yes'})
# print(data.head())

# Click Trough Rate Analysis

# 1. Analysis based on time spent by the users on the website
# fig = px.box(data,
#              x = 'Daily Time Spent on Site',
#              color = 'Clicked on Ad',
#              title = 'Click Through Rate based on Time Spent on Site',
#              color_discrete_map = {'Yes':'blue',
#                                    'No':'red'})
# fig.update_traces(quartilemethod = 'exclusive')
# fig.show()
# fig.write_image('Click Through Rate based on Time Spent on Site.png')

# 2. Analysis based on the daily internet usage of the user
# fig = px.box(data,
#              x = 'Daily Internet Usage',
#              color = 'Clicked on Ad',
#              title = 'Click Through Rate based on Daily Internet Usage',
#              color_discrete_map = {'Yes':'blue',
#                                    'No':'red'})
# fig.update_traces(quartilemethod = 'exclusive')
# fig.show()
# fig.write_image('Click Through Rate based on Daily Internet Usage.png')

# 3. Analysis based on the age of users
# fig = px.box(data,
#              x = 'Age',
#              color = 'Clicked on Ad',
#              title = 'Click Through Rate based on Age of Users',
#              color_discrete_map = {'Yes':'blue',
#                                    'No':'red'})
# fig.update_traces(quartilemethod = 'exclusive')
# fig.show()
# fig.write_image('Click Through Rate based on Age of Users.png')

# 4. Analysis based on the income of the users
# fig = px.box(data,
#              x = 'Area Income',
#              color = 'Clicked on Ad',
#              title = 'Click Through Rate based on Income',
#              color_discrete_map = {'Yes':'blue',
#                                    'No':'red'})
# fig.update_traces(quartilemethod = 'exclusive')
# fig.show()
# fig.write_image('Click Through Rate based on Income.png')

# 5. Calculate overall ads CTR
# First, calculate the ratio of users who clicked on the ad
# ratio = data['Clicked on Ad'].value_counts()
# print(ratio)
'''
No     5083
Yes    4917
Name: Clicked on Ad, dtype: int64

4,917/10,000 users clicked on the ads
'''
# Find the Click Through Rate percentage
# click_through_rate = 4917/10000*100     #49.17
# print(click_through_rate)

# CTR Prediction Model
# First, divide the data into training and testing sets
# data['Gender'] = data['Gender'].map({'Female':0,
#                                      'Male':1})

# x = data.iloc[:,0:7]
# x = x.drop(['Ad Topic Line','City'], axis = 1)
# y = data.iloc[:,9]

# from sklearn.model_selection import train_test_split
# xtrain, xtest, ytrain, ytest = train_test_split(x,
#                                                 y,
#                                                 test_size = 0.2,
#                                                 random_state = 4)

# Train the model using randow forecast classification algorithm
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier()
# model.fit(x.values,y.values)    # .values to avoid warning:'does not have valid feature names'

# Check the model's accuracy
# from sklearn.metrics import accuracy_score
# y_pred = model.predict(xtest)
# print(accuracy_score(ytest,y_pred))     # Accuracy score = 0.9585

# Test the model by making predictions
# print('Ads CTR Prediction: ')
# a = float(input('Daily Time Spent on Site: '))
# b = float(input('Age: '))
# c = float(input('Area Income: '))
# d = float(input('Daily Internet Usage: '))
# e = input('Gender (Male = 1, Female = 0): ')

# features = np.array([[a,b,c,d,e]])
# print('Will the user click on ad: ', model.predict(features))