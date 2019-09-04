
# Standardized Testing, Statistical Summaries and Inference



### Problem Statement

I looked over aggregate SAT and ACT scores and participation rates from each state in the United States for 2017 and 2018. I sought to identify trends in the data and combine my data analysis with outside research to identify likely factors influencing participation rates and scores in various states.

### Executive Summary

My approach was to import all of the data for the 2017 and 2018 SAT and ACT scores and participation rates, then thoroughly clean the data, and compare and analyze all of the stats pulled from the data, using various graphs and EDAs.


### Contents:
- [Provided Data](#Provided-Data)
- [Data Dictionary](#Data-Dictionary)
- [Conclusion and Recommendations](#Conclusion-and-Recommendations)
- [Source Documentation](#Source-Documentation)


---

### Datasets

#### Provided Data

I utilized the following datasets:

- [2017 SAT Scores](./data/sat_2017.csv)
- [2017 ACT Scores](./data/act_2017.csv)
- [2018 SAT Scores](./data/SAT2018.csv)
- [2018 ACT Scores](./data/ACT_2018.csv)

These data give average SAT and ACT scores by state, as well as participation rates, for the graduating classes of 2017 and 2018.

You can see the source for the 2017 SAT data [here](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/), the source for the 2017 ACT data [here](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows), the source for the 2018 SAT data [here](https://reports.collegeboard.org/sat-suite-program-results/state-results), and the source for the 2018 ACT data [here](http://www.act.org/content/dam/act/unsecured/documents/cccr2018/Average-Scores-by-State.pdf).

---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|SAT|Name of each U.S. state listed alphabetically|
|participation_sat_2017|float|SAT|Percentage of 2017 SAT scores reported per state|
|reading_writing_sat_2017|int|SAT|Evidence-Based Reading and Writing SAT score for 2017|
|math_sat_2017|int|SAT|Math SAT score for 2017|
|total_sat_2017|int|SAT|Combined Evidence-Based Reading and Writing/Math SAT score for 2017|
|state|object|ACT|Name of each U.S. state listed alphabetically|
|participation_act_2017|float|ACT|Percentage of 2017 ACT scores reported per state|
|english_act_2017|float|ACT|English ACT scores for 2017|
|math_act_2017|float|ACT|Math ACT scores for 2017|
|reading_act_2017|float|ACT|Reading ACT scores for 2017|
|science_act_2017|float|ACT|Science ACT scores for 2017|
|composite_act_2017|float|ACT|Composite of all ACT scores for 2017|
|state|object|SAT|Name of each U.S. state listed alphabetically|
|participation_sat_2018|float|SAT|Percentage of 2018 SAT scores reported per state|
|reading_writing_sat_2018|int|SAT|Evidence-Based Reading and Writing SAT score for 2018|
|math_sat_2018|int|SAT|Math SAT score for 2018|
|total_sat_2018|int|SAT|Combined Evidence-Based Reading and Writing/Math SAT score for 2018|
|state|object|ACT|Name of each U.S. state listed alphabetically|
|participation_act_2018|float|ACT|Percentage of 2018 ACT scores reported per state|
|composite_act_2018|float|ACT|Composite of all ACT scores for 2018|



---


### Conclusion and Recommendations
Probably the biggest takeaway from my exploration of the data is that there is a *negative* correlation between participation rates and scores for both the SATs and the ACTs:  in 2017, DC had the highest participation rate, yet in the same year it also had the lowest average SAT total score.  Similarly, in 2017, New Hampshire had one of the lowest ACT participation rates, and yet in the same year it also had the highest average ACT combined score.  This leads me to suspect that when a state requires its students to take a standardized test, a lot of those student are taking the test against their will and therefore not studying, whereas when the test is *not* required, the students that *are* taking the test are only doing so because they actually *want* to, and thus would be more inclined to study for the test and take it more seriously.

One state with a lower participation rate was North Dakota.  Of all the states, North Dakota had the lowest SAT participation rate in both 2017 and in 2018.  Rather than trying to get the North Dakota to mandate the taking of the test (which statistically brings up participation rates but NOT test scores), I would reccommend various other courses of action.  Based on [Hanover Research's 2014 report](https://www.hanoverresearch.com/media/Best-Practices-to-Increase-SAT-Participation-1.pdf), the best means to getting The College Board to increase participation amongst graduating seniors in North Dakota would be
- Covering all or part of exam fees
- Offering the SAT testing during school hours
- Providing a paid tutoring service to target high-scoring, low-income students


---

### Source Documentation

- [Hanover Research's 2014 report](https://www.hanoverresearch.com/media/Best-Practices-to-Increase-SAT-Participation-1.pdf)
- [magoosh](https://magoosh.com/hs/act/2017/states-that-require-the-act-or-sat/)
- [Vox](https://www.vox.com/the-goods/2019/3/28/18282453/sat-act-college-admission-testing-cost-price)
- [CNBC](https://www.cnbc.com/2018/12/07/median-household-income-in-every-us-state-from-the-census-bureau.html)
