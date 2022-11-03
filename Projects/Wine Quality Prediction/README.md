[Project 1](./Final_Project_Wine_Quality_KNIGHT.Rmd)

#  Wine Quality Prediction


#### Overview

An R script that, given specific wine features, will predict the wine quality.

### Problem Statement

For this project I decided to use data from [the Wine Quality Data Set](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) for both a regression and a classification model set. The study sample data consists of 1,599 red wines and 4,898 white wines from the northwest region of Portugal (one of the top ten wine producing countries in the world), a type of wine known as Vinho Verde. This data was collected between May of 2004 to February of 2007. The overall goal of my analysis was to try to predict the quality of wine based on a set of 11 objective quantitative variables; one binary and one base-10.

### Executive Summary

For the sake of this project I focused solely on the white wine data (using a full data set sample size of n = 4,898 observations). I excluded the red wine data because combining the data sets would have added a categorical predictor variable to my otherwise fully quantitative set of predictor variables, for the fact that red wine is different enough from white wine that they should be done separately, and for the principle of parsimony.

The overall goal of my analysis was to try to predict the quality of white wine based on a set of objective quantitative variables using 2 different regression methods (Multiple Linear Regression and Shrinkage Methods, predicting quality as a quantitative variable) and 2 different classification methods (Support Vector Machine and Bayes Classifiers, predicting quality as a qualitative variable), and to determine which models performed better.



### Contents:
- [Data Dictionary](#Data-Dictionary)
- [Conclusion and Recommendations](#Conclusion-and-Recommendations)
- [Source Documentation](#Source-Documentation)


---

### Data Dictionary

|Feature|Type|Description|
|---|---|---|
|fixed.acidity|float|The fixed acidity of the wine measured in grams of tartaric acid per liter|
|volatile.acidity|float|Volatile acidity of the wine measured in grams of acetic acid per liter|
|citric.acid|float|The amount of citric acid in a wine measured in grams per liter|
|residual.sugar|float|The amount of residual sugar in a wine measured in grams per liter|
|chlorides|float|The amount of chlorides in a wine measured in grams per liter|
|free.sulfur.dioxide|int|The amount of free sulfur dioxide in a wine measured in grams per liter|
|total.sulfur.dioxide|int|the amount of total sulfur dioxide in a wine measured in grams per liter|
|density|float|The density of a wine measured as grams of wine per cubic centimeter|
|pH|float|The pH balance of each wine|
|sulphates|float|The amount of sulfates in the wine measured in grams of potassium sulfate per cubic decimeter or liter|
|alcohol|float|alcohol content as a percentage|
|quality|int|A rating from 0-10, with 0 denoting ‘very bad’ and 10 denoting ‘excellent’|
|quality.good|int|A binary rating from 0-1, with 0 denoting ‘no’ and 1 denoting yes|




---


### Conclusion and Recommendations

Regression conclusion: For the optimal MLR model using Best Subsets and optimizing by Cp, the train MSE was 0.542259 and the test MSE was 0.4487168; For the optimal Shrinkage method using a LASSO model with a lambda tuned by 10-fold Cross Validation, the train MSE was 0.5442927 and the test MSE was 1.097064, making the Multiple Linear Regression superior to the Shrinkage in the predicting the quality of white wine based of the features included in the White Wine dataset. Since both models are essentially running on the same MLR model, it may be more accurate to say that variable selection via Shrinkage outperformed variable selection via Best Subsets. It was interesting that the train scores for both models were so close, which suggests that the models fit the training data almost equally well. Having a lower test error score than a train error score, which happened with the MLR regressions, suggests overfitting.

Classification conclusion: For the optimal SVM model tuning on kernel and cost, the Train Error Rate was 0.1678782 and the Test Error Rate was 0.1938776; For the optimal Bayes Classifier method using a QDA model with the choice of variables tuned by 10-fold Cross Validation, the Train Error Rate was 0.2565909 and the Test Error Rate was 0.2367347, making the Support Vector Machine superior to the Bayes Classifier method in the predicting the binary quality of white wine based of the features included in the White Wine dataset. I was impressed with how well the SVM performed, especially given that the Test Error Rate was larger than the Train Error Rate, suggesting no overfitting. And while the QDA also performed quite well, having a lower test error score than a train error score, which happened with the MLR regressions as well, does suggest overfitting.

Overall conclusion: although it is hard to compare the classification error rate to the regression mean squared error, it does look like the classification models both performed better than the regression models. I potentially attribute this to the classification metric ‘quality.good’ breaking down the 10 ratings of ‘quality’ into two ratings of either ‘good’ or ‘bad’.


---

### Source Documentation
My entire dataset was obtained from:
- [Wine Quality Data Set](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)

Other research came from:
- ["Modeling wine preferences by data mining from physicochemical properties" by Paulo Cortez et al.](https://www.sciencedirect.com/science/article/abs/pii/S0167923609001377?via%3Dihub)
