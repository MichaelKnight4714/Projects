[Project 1](./Team 2 Final Project.Rmd)

#  Analysis of Trust in Media


#### Overview

An R script that details _.

### Problem Statement


With the advent of the internet, there has been a shift on how and where people obtain news. Additionally, there is a growing trend of people getting news from social media platforms, which comes at the expense of credibility and correctness of the news reports on social media (Aldwairi & Alwahedi, 2018). Despite apparent evidence of inconsistencies in social media news reports, a huge number of internet users have made social media their primary source of daily global/local economic, political, or social news updates (Gottfried & Elisa, 2016).



### Executive Summary

This goal of this project is to address the reason why people continue to frequently get their news from social networking sites despite the fact that they do not trust it. We have identified a few hypotheses that form the basis of our research question. Firstly, we will use the survey findings to show the lack of trust that people who obtain news from social media have towards family, friends, and news media in general. Additionally, we will show that the respondents who read the news for political reasons tend to only focus on either republican or democratic debates to enhance their political views. We also identify that respondents who approach social media news with a skeptical eye are more likely to fact check whatever they read on social platforms to verify its authenticity. Survey data also indicates that readers who diversify their sources of information on the subject of government and politics are more likely to engage and share their opinions with their family and friends.

Based on our lit review (see [paper](./Team-2-Final-Project.docx)), we hypothesize the following:

- H1) People who get their news from social media feel that most people in society cannot be trusted (i.e., family, friends, & community).
- H2) People who get their news from social media feel that most national news orgs cannot be trusted.
- H3) People who do not trust the news they see online are more likely to fact check.


### Contents:
- [Data Dictionary](#Data-Dictionary)
- [Conclusion and Recommendations](#Conclusion-and-Recommendations)
- [Source Documentation](#Source-Documentation)


---

### Data Dictionary

|Feature|Type|Survey Question|Available Answers
|---|---|---|---|
|News_Preference|object|Which of the following would you say you prefer for getting news?|TV, Radio, Newspaper, Social Media, News Site/App|
|Trust_in_Others|int|Generally speaking, would you say that most people can be trusted or that you can't be too careful in dealing with people?|Can't be too careful (0), Most people can be trusted (1)|
|Trust_in_social_media_news|object|How much, if at all, do you trust the information you get from Social networking sites, such as Facebook and Twitter?|Not at all (0), Not too much (1), Some (2), A lot (3)|
|Fact_Check|int|When you are online and come across information in a news story that you think is inaccurate, how often do you take it upon yourself to figure out whether it is accurate?|Never (0), Hardly ever (1), Sometimes (2), Often (3)|
|How_often_social_media_for_news|int|How often do you get news from a social networking site?|Never (0), Hardly ever (1), Sometimes (2), Often (3)|
|Trust_in_natl_news_orgs|int|How much, if at all, do you trust the information you get from National news organizations?|Not at all (0), Not too much (1), Some (2), A lot (3)|



---


### Conclusion and Recommendations

#### Data Driven Hypotheses/Conclusion

The results from our analysis confirm our first two hypotheses. First, we hypothesized that people who get their news from social media feel that most people in society cannot be trusted (i.e., family, friends, & community). The results from our study support this claim, showing that individuals who get their news from social media have a greater overall trust for people in society. Second, we hypothesized that people who get their news from social media feel that most national news organizations cannot be trusted. The results from our analysis supports this claim, showing that individuals who get their news from social media have a decreased trust in national news organizations compared to individuals who get their news through other means (i.e., print, radio, television, news websites, etc).

The results from our analysis reject our third hypotheses. Based on the review of the literature and findings from our first two hypotheses, we suspected that individuals who were mistrusting of social networking websites would be more likely to fact check the news they consumed on social media. However, we found that an increase in trust in social media news is associated with an increase in fact checking. Therefore, our new data driven hypothesis would be thhat individuals who trust social media news are more likely to fact check. This was an interesting finding and future research ought to look further into the relationship between trust and fact checking.


#### Discussion/Recommendations

The spread of misinformation can mislead the public to believing information which is not factually credible or supported by evidence. This includes information about national elections, climate change, global pandemics, and so much more. Therefore, the current study is important in understanding how social media news consumption can impact overall trust in news media and members of society as a whole. Our main findings show that people who prefer to get their news on social media have the least amount of trust in others compared to those who prefer to get their news through other means. This finding is consistent with previous literature which have identified a significant relationship between social media consumption and general mistrust in the news across all platforms (i.e., print, radio, television, news websites, etc) (Fletcher & Park, 2017; Kalogeropoulos, Udris, & Eisenegger, 2019; Park, Fisher, Flew, & Dulleck, 2020; Tsfati & Ariely, 2014). Additionally, fact checking is an indication of general mistrust in the news (Allcot & Gentzkow, 2017). Therefore, it is not surprising that 79% of individuals that do not trust news obtained from social media platforms fact check whatever they read. However, existing research suggests that most people are bias in their fact checking process (Shin & Thorson, 2017).Therefore, future research is needed on the relationship between fact checking and general mistrust in news platforms.



---

### Source Documentation
Our entire dataset was obtained from:
- [The Pew Research Center](https://www.pewresearch.org/journalism/2016/05/26/news-use-across-social-media-platforms-2016/)

Other research came from:
- ["Social Media and Fake News in the 2016 Election" by Hunt Allcott, & Matthew Gentzkow](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.211)
- ["Internet, News, and Political Trust: The Difference between Social Media and Online Media Outlets" by Andrea Ceron](https://academic.oup.com/jcmc/article/20/5/487/4067572)
- ["The Impact of Trust in the News Media on Online News Consumption and Participation" by Richard Fletcher & Sora Park](https://www.tandfonline.com/doi/abs/10.1080/21670811.2017.1279979)
- ["News Media Trust and News Consumption: Factors Related to Trust in News in 35 Countries" by Antonis Kalogeropoulos, et al](https://ijoc.org/index.php/ijoc/article/view/10141)
- ["Global Mistrust in News: The Impact of Social Media on Trust" by Sora Park](https://www.tandfonline.com/doi/abs/10.1080/14241277.2020.1799794)
- ["Partisan Selective Sharing: The Biased Diffusion of Fact-Checking Messages on Social Media" by Jieun Shin & Kjerstin Thorson](https://onlinelibrary.wiley.com/doi/abs/10.1111/jcom.12284)
