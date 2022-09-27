Written by: Laurits Lyngbæk
Source of information:
Association links:
Tags: #📑ChildNode 
___
##  Repeated-measures linear regression
### (Within-participant design)
The variance in our data change depending on wither its within or between subject design, and we should account for that.  
For this we use multi-level regression (mixed-effects model) is a special class of regression models.

“**Mixed-effects**”:

| Fixed effects                                                               | Random effects            |
| --------------------------------------------------------------------------- | ------------------------- |
| Systematic variance                                                         | Unsystematic variance     |
| Experimental manipulation (interesting bu design)                           | Not interesting by design |
| Repeatable                                                                  | Not repeatable            |
| Exhaust the population of interest (as operationalized in our study design) | Sample of the population  |
| continuous / categorical                                                    | categorical (often ID of person)                          |


Outcome ~ fixed effects + random effects + $\epsilon$



#🖥️Code **for R:**
```r
pacman::pload(lme4)
lme4::lmer()
summary(lme4:lmer(outcome~predictor+(1+trial|varriable_ID), data = df_name)) - for plot etc
summary(lmerTest:lmer(outcome~predictor+(1+trial|varriable_ID), data = df_name)) --> for p values
```
![[Explanation of lmer.png]]
![[Corrigated for random slope.png]]

**Input example:** 
```r
pacman::pload(lme4)
data("sleepstudy")

intercept_model <- lmerTest::lmer(Reaction ~ Days + (1|Subject), data = sleepstudy, REML = F)

summary(intercept_model)

```

**Output example:**
```r
Linear mixed model fit by maximum likelihood . t-tests use Satterthwaite's method ['lmerModLmerTest']
Formula: Reaction ~ Days + (1 | Subject)
   Data: sleepstudy

     AIC      BIC   logLik deviance df.resid 
  1802.1   1814.9   -897.0   1794.1      176 

Scaled residuals: 
    Min      1Q  Median      3Q     Max 
-3.2347 -0.5544  0.0155  0.5257  4.2648 

Random effects:
 Groups   Name        Variance Std.Dev.
 Subject  (Intercept) 1296.9   36.01   
 Residual              954.5   30.90   
Number of obs: 180, groups:  Subject, 18

Fixed effects:
            Estimate Std. Error       df t value Pr(>|t|)    
(Intercept) 251.4051     9.5062  24.4905   26.45   <2e-16 ***
Days         10.4673     0.8017 162.0000   13.06   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Correlation of Fixed Effects:
     (Intr)
Days -0.380
```

**Marginal R^2 (R2m)**
Fixed effects only - what we really care about

**Conditional R^2 (R2c)**
Total variance explained (incl. Random effects)

**for reporting you have to specify:**
what software you have used 
what packages 
what kinds of models you used (incl. R syntax) 
transformations of data

```ad-cite
title: Exampel write-up (for referance)
“We used R (R Core Team, 2019) and lmerTest (Kuznetsova, Brockhoff and Christensen, 2017) to perform a linear mixed effects analysis of the relationship between sleep deprivation and reaction time. As fixed effects, we entered the number of days subjects have been lacking sleep into the model. As random effects, we had intercepts for subjects, as well as by-subject random slopes for the effect of the number of days. The model had the following syntax: 

Reaction ~ Days + (1 + Days | Subject) 

The whole model accounted for roughly 80% of variance in the reaction time (R2 conditional = 0.79), while the fixed effect for roughly 29% (R2 marginal = 0.29). Visual inspection of residual plots did not reveal any obvious deviations from homoscedasticity or normality. Reaction time has been found to significantly be modulated by number of days of sleep deprivation, β = 10.467, SE = 1.502, t = 6.968, p < .001”


```


**Plot of lmer (multi-level regression):**

![[Plot of lmer.png]]
Orange = average model
other colors = participants regressions

We expect both different intercepts and *slopes*, because of independent variability, we call these "random slopes". 



**Conclusion: **
To test XYZ, we fitted a linear mixed-effects model with Reading Time as the outcome variable and Condition as fixed effect. Our model had random intercepts for participant and random slopes for trial number







## Class 9
![[Gelman and Hill, 2006.png]] 
### How to deal with repeated measure:
**Complete pooling:**
Disregarding any grouping level that has repeated measure. So far this is what we’ve done.

**No-pooling:**
Adding subject as a fixed effect. (reproducible results)

**Partial pooling:**
Add subject as random effect. (not reproducible result)


#### Fixed effects 
- Systematic variation in your sample 
- What you can use to predict 
- E.g. Condition, Age or Gender
#### Random effects 
- Unsystematic variation -> individual differences 
- E.g. participant(id) or stimuli(id)




