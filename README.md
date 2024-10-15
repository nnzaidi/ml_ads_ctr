ML-Python Practice 1: Ads Click Trough Rate Prediction (Classification)

The project is referred from below link for study purpose. Credit to the owner:
https://thecleverprogrammer.com/2023/01/16/ads-click-through-rate-prediction-using-python/

Prior to building the prediction model, we have to analyze and understand the relationship between 'Clicked on Ad' column with other columns.

1. CTR based on Time Spent on Site

    Based on the box plot, we can see that more users clicked on the ads when they spent more time on the site.

2. CTR based on Daily Internet Usage

    Although users use the internet more on daily basis, that doesn't guarantee that they will click on the ads as shown on the figure.

3. CTR based on Age of Users

    Users who are 40 and above tend to click on the ads more as compared to younger generation.

4. CTR based on Income

    Based on the box plot, it shows that users with lower income clicked on the ads more.

Based on these analyses, we get better understanding on how each columns affect the Ads Click Through Rate  (CTR). Next, we dropped unnecessary columns from the dataset and divided them into training and test sets.

We built the model using Random Forest Classification and obtained an accuracy score of ~96%
