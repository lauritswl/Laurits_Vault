Written by: Laurits Lyngbæk
Source of information: [[Lecture_7_Linear_regression.pdf]]
Association links: [[003 Methods]] 
Tags: #🌲Evergreen 
___

# Linear regression
Is a inferential test predicting a continuous outcome from one or more continuous or categorical predictors.

We are trying to explain/predict an outcome
$Outcome_i = model + error_i$
$X_i = participant$

The most simple model for data is the mean, but it's not good for predicting outcome.
The regression line is often a better model (if there is a relationship between the variables), as it minimizes the $\sum{error}$.

**Mean					vs 							Linear regression**
![[Mean vs Linear regression.png]]


**The regression line** = The line that minimizes the sum of the squares of the error (residuals)
or
**The regression line** = The line that minimizes the vertical distances between the model and the data points

Interpolation vs extrapolation (the magic of regressions:)
![[Interpolation vs extrapolation.png]]

### Correlation vs Regression
*Linear regression differs from the [[Correlation]] line in a statistical setting of 2 independent variables*, but **regression offers more freedom** as it can take **as many predictors** as you want and the **predictors can be categorical.**

You can theoretically only use correlation, when it's a quasi-experiment, and you use regression when the outcome variable is explained by the predictor(s).

| Regression                        | Correlation                              |
| --------------------------------- | ---------------------------------------- |
| Form of relation                  | Strength of relationships (no direction) |
| Attempts to show cause and effect | No causation                             |
| Multiple variables                | Only pair of variables                   |
| "Predictive"                      | Descriptive                              |

## Regression formula
**Formula:** (*Alternative model*)
```ad-tip
title: 
$$Y_i=\beta_0+\beta_1 X_1+\epsilon_i$$
```

**Variables:**
$Y_i=$ The i-th value of the outcome Y that I am trying to predict

$\beta_0=$  Regression coefficient for **"the intercept"** of the regression line
= "what is the value of Y when X is zero"

$\beta_1=$ Regression coefficient for **"the slope"** of the regression line 
= "how much does Y change for each one increment on X"

$X_i=$ The i-th value of the predictor variable X

$\epsilon_i=$ The residual error for the i-th observation



**The mean  model:**  (*Null model*)


```ad-tip
title: 
$$Y_i=\bar{x}+\epsilon_i$$  
```
==If the Null model is a better model than the alternative model, you reject the alternative model.==

### Regression in r
#🖥️Code **template:** 
```R
#Code for lm
model<-lm(outcome~predictor,data = df_name)

#Has be used in a function:
summary(model)
```
**Output example:**
```
summary(lm(formula = y ~ x1 + x2))

Residuals:
     Min       1Q   Median       3Q      Max 
-1.69194 -0.61053 -0.08073  0.60553  1.61689 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)   
(Intercept)   0.8278     1.7063   0.485  0.64058   
x1            0.5299     0.1104   4.802  0.00135 **
x2            0.6443     0.4017   1.604  0.14744   
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.141 on 8 degrees of freedom
Multiple R-squared:  0.7477,	Adjusted R-squared:  0.6846 
F-statistic: 11.85 on 2 and 8 DF,  p-value: 0.004054

```


#### Explanation of regression results in r 
**SE of the betas:**
A measure of how good our estimates of the betas ($\hat{\beta_0}$ and $\hat{\beta_1}$) are in relation to the “true” population value of the betas ($\beta_0$ and ($\beta_1$) 

**The t-value of beta:**
How far from zero is beta on a t distribution, measured as the ratio between systematic and unsystematic variance 

**A p-value for the t-value of beta:**
The probability of the t-value given the degrees of freedom if $H_0$ is correct

**$R^2/r^2$**:
A measure of the variance in the data explained by the model

**F-Statistic** (and associated p-value)**:**
A measure of whether the model is statistically significant from the null model
A good model has a value above 1.



## Linear regressions for categorical categories explanation (example):
![[Regression with categorical predictors.png]]
In this example you would have a score of 64.1 if you haven't completed the predicting test preparation course, and a score of 64.1+5.6=**69.7** if you have completed the course.
The [[Correlation#r 2|r^2]] of this test indicates that only 3% of this value is explained by the predictor.
So its not very useful.

## Multiple regression
Is when you have more than one predictor in a regression analysis.

```ad-tip
title: 
$$Y_i=\beta_0+\beta_1 X_1+\beta_2 X_2+...+\beta_n X_n+\epsilon_i$$
```


## Assumptions of regression:
1. **Absence of multicollinearity:** : no perfect linear relationship between two or more predictors (NB: multiple regression only)
	```ad-tip
	title: R code: (largest value should be < 10)
	vif(model)
	```
2. **Linearity of residuals** : 
	```ad-tip
	title: R code: (largest value should be < 10)
	vif(model)
	```
	
	![[Assumptions of regression.png]]

## [[Repeated-measures linear regression]]
See hyper link for guide to Ln reg for repeated-measures


## [[Logistic Regression]]