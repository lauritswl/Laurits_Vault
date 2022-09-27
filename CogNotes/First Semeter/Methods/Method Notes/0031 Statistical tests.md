# Statistical tests
#🗂️Organization 
#🌲Evergreen 

---

# [[Correlation]]
descriptive assessment/inferential test of the relation between two continuous variables

# [[Inferential Statistics#T-test|T-test]]
inferential test of whether two means are significantly different from each other / whether one mean is significantly different from a hypothesized mean
# (Simple/multiple) [[Linear Regression]]
inferential test predicting a continuous outcome from one or more continuous or categorical predictors




## Assumptions of normality in statistics

### Parametric tests
The assumptions of parametric tests are:

1) **Normally distributed data**: 
If the data is not normally distributed, then you the logic behind hypothesis testing is flawed
2) **Homogeneity of variance**: 
One variable should be stable at all levels of another variable. To phrase it differently, if you have test multiple groups of participants, the samples of these groups, should have similar variance in their other variables.
3) **Interval data**:
Data should be measured at least at interval level.
(It must be numerical data) 
4) **Independence**:
This can have multiple meanings:
![[Methods#Between Subject vs Withing Subject]]
	1) In Between-subject studies its important that the behavior of one subject doesn't influence the behavior of other subjects
	2) In Withing-subject studies its important that behavior doesn't influence other subjects, but the subjects behavior on part 1 of the study, is of course allowed to influence the second part.
**Also**, one participant can't have 2 data points. 

#### Test of normality
To test the data's normality, check [[Normal Distrubution]] or [[QQ Plot]]

### Non-parametric tests
"Distrubution-free"

- Data can be transformed to become normally distributed - e.g by log(data)
- By transforming to z-score you become mor enormal.