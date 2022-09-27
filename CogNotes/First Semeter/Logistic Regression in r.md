# Logistic Regression in r
#🖥️Code 

**Input**

```{r}
model <- glm(formula= vs ~ wt + disp, data=mtcars, family=binomial)

summary(model)
```
**Output**
```r
Call:
glm(formula = vs ~ wt + disp, family = binomial, data = mtcars)

Deviance Residuals:
     Min        1Q    Median        3Q       Max
-1.67506  -0.28444  -0.08401   0.57281   2.08234

Coefficients:
            Estimate  Std. Error z value  Pr(>|z|)
(Intercept)  1.60859    2.43903   0.660    0.510
wt           1.62635    1.49068   1.091    0.275
disp        -0.03443    0.01536  -2.241    0.025 *
---
Signif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

Null deviance: 43.86 on 31 degrees of freedom
Residual deviance: 21.40 on 29 degrees of freedom
AIC: 27.4

Number of Fisher Scoring iterations: 6
```
https://www.theanalysisfactor.com/r-glm-model-fit/




Use a function to find the odds ratio:
```{r}
boot::inv.logit(intercept+(x+slope))

```


## R syntax for repeated-measures logistic regression
Input
```{r}
lme4::glmer(..formula.., family = binomial(link = logit), data) 
```

Output
```{r}
MISSING
```