# Correlation
#🌿Sprout 
[[003 Methods]]


Correlation tests the relationship between two continuous variables.
## Covariance

[Variance] = mean deviance of each observed point from the mean.

[Covariance] = A measure of how two measurements on two different variables vary together

![[Covariance.png]]

**Calculation of covariance:**

$$cov(x,y) = \frac{\sum{(x_i-\bar{x})(y_i-\bar{y})}}{N-1}$$

Depending on the covariance of the data, you can say the following about the relation:
**Positive covariance** = positive relationship (higher x = higher y)  
**Negative covariance** = negative relationship (higher x = lower y)  
**Covariance around zero** = no relationship (higher x = same y)

## From covariance to correlation
The covariance coefficient is too dependent on scale/units of measurements, and therefore to hard to measure. We solve this problem by **standardizing (= z-score transform)** the covariance by dividing it by the product of the *s* (standard deviation) of the two variables:
$$r = \frac{cov(x,y)}{s_x s_y}$$
s = [[Error Bars#Standard Deviation|Standard Deviation]]


The standardized covariance is called **correlation coefficient**.

### Effect size
Correlation is a way to calculate "effect size".

| Effect size | r         | Meaning                                        |
| ----------- | --------- | ---------------------------------------------- |
| Small       | 0.1<x<0.3 | Relationship explains 1-9% of total variance   |
| Medium      | 0.3<x<0.5 | Relationship explains 9%-25% of total variance |
| Large       | 0.5<x     | Relationship explains > 25% of total variance  |


#### r^2
This isn't very easy to remember, so we use coefficient of determination r^2.
**This number explains** *how much of the variance in our **data is explained** by the relationship between X and Y.*
r^2 is a linear number.



## [[P-value]]
The p-value is something we use to determine whether our coefficient is statistically different from 0.
The lower the p-value the more confident is your result (threshold at 0.05, before statistically = 0)