Written by: Laurits Lyngbæk
Source of information: [[Lecture_10_Logistic_regression.pdf|PP for lecture 10]]
Association links: [[003 Methods]]
Tags: #🌿Sprout 
___
# Logistic regression
Is trying to predict an binary outcome.
We need a **generalized** (=expanded) regression model that accommodates **binomial** (= binary) **outcomes**. We **predict** a binary outcome from continuous or categorical predictors
 by fitting a squiggly line (sigmoid function), that **predicts the probability** of y given different levels of x?

![[Logistic regrission sigmoid.png]]


$P(Y_i)=\frac{e^(\beta_0+\beta_1+X_i+\epsilon_i)}{1+e^(\beta_0+\beta_1+X_i+\epsilon_i)}$



> Gives the conditional probability that an outcome variable equals one at a particular value of a predictor variable.
## Bernoulli trials / Binomial distributions
![[Bernoulli trials.png]]


## Need to know about Log Reg





____

## [[Logistic Regression in r]]

____


## TL;DR
- Logistic regression is for categorical (binary) outcome variables 
- Predicts P(Y) given values of X’s 
- Expands upon linear regression (generalized linear model) 
- Same output as linear model, but estimates are in the log-odd scale 
- Very common classification algorithm in machine learning


____

- Independence of residuals 
- Linearity of residuals (in the logit-transformed data) 
- Absence of multicollinearity
- Lack of strongly influential outliers


