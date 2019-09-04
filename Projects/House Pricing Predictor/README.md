
# Ames Housing Data and Kaggle Challenge


#### Overview

Predicting house prices based on a long series of features describing various different aspects of a house



### Problem Statement

Using the well known Ames housing data, as well as a guide in the form of an [Ames Housing .txt file](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt), I created a regression model that predicts the price of houses in Ames, Iowa.  It required a lot of data cleaning (fixing null values appropriately and dropping unneeded information), and I did some evaluation of the correlations to determine which features had the most impact on price (both positively and negatively).



### Executive Summary

My aim was to predict the sales price for each house in the provided testing data. For each Id in the test set, I had to predict the value of the SalePrice variable.  I was doing this to submit to [Kaggle](https://www.kaggle.com/) as part of a [competition](https://www.kaggle.com/c/dsi-us-8-project-2-regression-challenge/) (so the final data had to be submitted very particularly), where [Kaggle](https://www.kaggle.com/c/dsi-us-8-project-2-regression-challenge/) leaderboard standings will be determined by root mean squared error (RMSE).



### Contents:
- [Provided Data](#Provided-Data)
- [Conclusion and Recommendations](#Conclusion-and-Recommendations)
- [Source Documentation](#Source-Documentation)


---

### Datasets

#### Provided Data

For this project, I utilized the following datasets:

- [Ames Housing Training Data](./datasets/train.csv)
- [Ames Housing Testing Data](./datasets/test.csv)

The Ames Housing Dataset is an exceptionally detailed and robust dataset with over 70 columns of different features relating to houses.  The testing dataset has a bunch of features for houses in Ames, but doesn't include the price.  The predicted prices that matched this testing dataset were saved into the following .csv file:

- [Submission](./datasets/submission.csv)


---


### Conclusion and Recommendations
The cleaning of this data was rigorous and occasionally not completely obvious. While the provided document [Ames Housing .txt file](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt) alluded to null values in regards to alley access, basement, fireplace, garage, pool, fence, and other miscellaneous features (which were switched to mark as 'none'), and thus to descriptive factors of those features (which were marked to integer values of 0), there were other null values that took more exploration to discover. Masonry Veneer Type was listed in the [Ames Housing .txt file](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt) as being marked "none" for an absence of the feature, but this was not the case as those values were left null, discovered only by the fact that the same amount of cells for Masonry Veneer area were also null in the provided training data document. The remaining total null values in that document happened to be equal to the amount of null values for Lot Frontage (marked to 0), and there was one null value for a single cell in the Electrical Sytem column in a single row of the testing data, also marked to 0.

Then, using dummy variables, I converted the qualitative features into something numeric that could be used by a computer to find the correlation between that data and the sales price. This produced a lot of new columns, many which were in the training data but not the testing data, and vice versa (this was due to values under the qualitative categories that existed in the column of one but not the other, such as a roof material value of metal (which was in at least one house in the testing data but not for any in the training data) or the roof material made of membrane (which was in the training data but not the testing data). I tried setting these values where they were missing to 0 (since they were dummy variables with a value of 1 or 0, where 0 signified not having said quality), but for some reason this gave me a worse fitting models and worse [Kaggle](https://www.kaggle.com/c/dsi-us-8-project-2-regression-challenge/) scores, so I just dropped those dummy columns.

Based on the final data, I analyzed factors that affected the price in the training data. The features that had the greatest positive correlation with price were (in order) Overall Quality, the Above Ground Living Area Square Footage, the Garage Area Square Footage, the Size of garage (in car capacity), and the Total Basement Square Footage. The features that had the greatest negative correlation with price were (in order) having an External Quality ranked Average or Typical, having a Kitchen with Quality ranked as Average or Typical, the absence of a Fireplace, the quality of the Basement being ranked as Average or Typical, and having a garage with an unfinished Interior. All of these results made logical sense and seemed quite obvious. Analyzing only the neighborhood dummy variables correlation with price, I found the the top 5 neighborhoods with a positive effect on the sales price were (in order) Northridge Heights, Northridge, Stone Brook, Somerset, and Timberland.

I fiddled around with filtering out some of the data by low correlation, and through much testing, found I acheived the best results filter out features that had less than 5% positive correlation and more than -5% negative correlation. I also dropped Id and PID, because even though they had a relatively ok correlation with price in the training data, they were random numbers that had no actual impact on the price, and dropping them improved my results. When fitting a model to a train-test-split of this enhanced training data, I tried a linear regression model, a LASSO model, and a ridge model. The linear regression model worked TERRIBLY (probably because I used a LOT of features - 173 features to be precise). The ridge and LASSO models worked much, much better (which was not unexpected as they are more refined and filter out noise that comes from having so many features. In the end, the LASSO model worked the best, and got a score of 0.897 on the training data's training data and a score of 0.899 on the training data's testing data (note to self: next time rename the variables containing the data). When formatted and submitted to the [Kaggle contest](https://www.kaggle.com/c/dsi-us-8-project-2-regression-challenge/) I only got a score of 27658.196; which makes sense because the model was obviously overfitted and the [Kaggle contest](https://www.kaggle.com/c/dsi-us-8-project-2-regression-challenge/) was judged by the Root Mean Squared Error.

​


---

### Source Documentation

- [Kaggle's DSI-US-8 Project 2 Regression Challenge](https://www.kaggle.com/c/dsi-us-8-project-2-regression-challenge/)
- [Ames Housing .txt file](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)
