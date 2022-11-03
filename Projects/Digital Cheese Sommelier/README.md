[Project 1](./Recommender_model.ipynb)

#  The Digital Cheese Sommelier


#### Overview

A pythonic script that will recommend cheeses.

### Problem Statement


There are over 3,000 cheeses that exist around the world (750 from France alone!), with around [500 different varieties recognized by the International Dairy Federation (and that's only as of 1981!)](https://books.google.com/books?id=-oRp5VCVTQQC&pg=PA388&hl=en#v=onepage&q&f=false). Because cheese varies so greatly and has changed so much in the [10,000 years](https://www.thespruceeats.com/the-history-of-cheese-1328765) that it has existed, there is no universally agreed upon means for classification. There are many, many factors that contribute significantly to how it tastes: milk source (or vegan!) and what the animals were fed, milk treatment (how it was heated), rennet type, rind type, age, fat content, moisture content (firmness), production type, and the country/region it was sourced are the most prominent flavor determinators.

The problem then is thus: how to teach a computer to recommend a cheese based on these factors?



### Executive Summary

My approach was to import all of the data on cheese from cheese.com (a list of 1,827 different entries) into a pandas dataframe, then thoroughly clean and munge the data. The next step was to dummy all of this information into a big binary matrix which could then be affixed to a recommender.

The next step was using widgets to instantiate raw input question via a series of dropdown menus for each feature. Once the user selects the cheese to recommend off of, and/or the list of features to filter through, The Digital Sommelier then passes the values put in by the user into a series of masks that narrow and refine the cheeses in the big binary dataframe.

Then, by calculating the cosine similarity for each cheese in this refined binary dataframe using the pairwise_distances function (which returns a square matrix comparing every cheese with every other cheese in the refined dataframe), a distances dataframe can be created. From this distance dataframe, the recommendations can be called by finding the cheeses with the smallest pairwise distances from the original cheese (within the limited dataframe created by the masks).

Additionally it should be noted that, should the user not choose a cheese to build a recommender model on, the model will recommend a list of cheese based on the features entered simply by narrowing the original dataframe through a series of masks created by user input and then displaying that dataframe.



### Contents:
- [Data Dictionary](#Data-Dictionary)
- [Conclusion and Recommendations](#Conclusion-and-Recommendations)
- [Source Documentation](#Source-Documentation)


---

### Data Dictionary

|Feature|Type|Description|
|---|---|---|
|Name|object|Name of each cheese listed alphabetically|
|Volatile Acidity|float|Volatile acidity of the wine measured in grams of acetic acid per liter|
|Milk|object|Animal source(s) and pasteurization type(s)|
|Country of origin|object|Location source, by country|
|Region|object|Location source, by region|
|Type|object|Type of cheese|
|Texture|int|Texture of cheese|
|Rind|object|Type of rind the cheese has|
|Flavour|object|cheese's flavor|
|Aroma|object|Cheese's aroma|
|Vegetarian|object|Is the cheese vegetarian (does it contain animal rennet)|
|Producers|object|who makes the cheese|
|Description|object|A paragraph or so describing each cheese|
|Fat content|float|Percentage of fat in the cheese|
|Family|object|family of cheese|



---


### Conclusion and Recommendations

The model recommends fairly well. I know there is no tangible way to test the accuracy of a recommender, but I worked in a cheese shop (CowGirl Creamery near Metro Center in Washington, DC in 2008) and have been studying artisnal and farmhouse cheeses since falling in love with the stuff following a trip to France with my family at age 15.

I spent waaaay too long trying to get data from 4 separate sources, and only used one of those sources in the final project, which didn't have all of the features I wanted (especially age, rennet type, and production source type). Given more time, I would find this missing data for all of these cheeses, plus twice the number of cheeses, and I would more explicitly distinguish the 7 main types of cheese, and add extra weight to certain specific features.

I hope to have this running on flask in time for the Spotlight presentation.


---

### Source Documentation
My entire dataset was obtained from:
- [cheese.com](https://cheese.com)

Other research came from:
- ["Cheese Primer" by Steven Jenkins](https://www.amazon.com/Cheese-Primer-Steven-Jenkins/dp/0894807625)
- ["The World Encylopedia of Cheese" by Juliet Harbutt](https://www.amazon.com/World-Encyclopedia-Cheese-Definitive-Illustrated/dp/1843099594)

Additional research from these websites:

- [wikipedia](https://en.wikipedia.org/wiki/Cheese#Types)
- [American Cheese Society](https://www.cheesesociety.org/)
- [Cheese Science Toolkit](https://www.cheesescience.org/)
