[Project 3](https://git.generalassemb.ly/MichaelKnight4714/Submissions/commit/c88a13cb8c58572dfa1ad9dc7231c340901cbf6e)

# Subreddit APIs & Classification

Distinguishing between posts in the cheese subreddit and the weed subreddit using different models

### Problem Statement

The goal is to create a model that will be able to take a reddit post and determine whether it came from two possible subreddits: r/Cheese or r/weed. These are two subreddits discussing two fairly different focal points.  However, the subjects of both subreddits share a strange and unusual feature in common: they are both things that are ingested where the quality can be measured in how pungent it smells. The question is, how well can I get two different computer programmed predictive models to distinguish between the two?


#### Data Collection

A little under 2000 posts were gathered from each of the two subreddits. This was done using reddit's API. By scraping each subreddit's tops posts, newest posts, and hottest posts, I was able to pull three times as much as the allowed 1000 posts per day (as specified by the reddit API).  Before I wrote the function to do this, I was scraping the cheese subreddit using instances of for loops, and sloppily saved a lot of that data into a .csv file in an unformatted manner.  Because of this I have provided a separate jupyter notebook detailing that process so as to keep my main notebook on the web scraping clean, without discarding this data.  I put the data munging and modelling in a third separate jupyter notebook.

---

### Data Munging

Any duplicates that existed among the posts were deleted. The titles of each post were merged with the text of the post in order to have enough data to work with. Using regex, any hyperlinks or html text were replaced with empty strings, as were any references to the namesakes of each subreddit.  All the predetermined english stopwords were filtered through the Tfidf Vectorizer.  Finally, I removed all the duplicate posts that had been grabbed during each scrape (which turned out to be a lot of the posts scraped).


---

### Preprocessing & Modeling

Setting my X-value to be the text (comprised of both title and selftext of each post) scraped from each post, and seting my y-value to be a dummy variable for whether or not the post came from the cheese subreddit or not (1 for yes, 0 for no), I then did a train-test-split.  After that I fit and transformed a Tfidf Vectorizer on the X_train, transformed it on the X_test, and converted the vectorized data onto two SparseDataFrames (one for train and one for test), and dropped the resulting null values.  Once I had done that, I instantiated a GridSearchCV for RandomForestClassifier, then fit and scored it on the train data.  I then instantiated a Multinomial Naive Bayes model, and fit and scored that on the train data.


---

### Conclusion and Recommendations

Using the Random Forrest model over 100 n_estimators, through a gridsearch testing over parameters of 8, 10 and 12 for 'min_samples_split' and 50, 75, and 100 for 'max_depth', the training score was about 89% and the testing score was about 82%.  Using the Multinomial Naive Bayes model with the built in parameters, the training score was 89% and the testing score was 84%.  Both models worked fairly well, and almost equally accurately, with the Random Forrest Model being just a hair overfit and weaker than the Multinomial Naive Bayes model.  I think that, had I munged the data a little more thoroughly, and perhaps gotten more scraping done, I could have improved the models.


#####Framework for this readme was taken from the spectacular Josh Robin
