# Overview of Normal Distribution
#🌲Evergreen 
## When do normal distributions occur? 
"It turns out that if we add together many random variables, all having the same probability distribution, the sum (a new random variable) has a distribution that is approximately normal"
[Denny & Gaines, 2000, pp. 82– 83)]

## What is needed for a normal distribution
Symmetrical gravitation toward the mean with decreasing N of data points as we approach the tails.

Defined by two parameters: mean (μ) and standard deviation (σ):
![[Normal Distribution properties.png]]
### Sample Distribution
If you sample from a population, the means of each sample, will be a [normal distribution](https://onlinestatbook.com/stat_sim/sampling_dist/index.html).


## Describing a normal distribution
from [[Data Collection]]
[[Population]] = The exhaustive collection of units which we want to generalize our findings (all of the population) 
N = The size of the exhaustive population 
$\mu$ = The mean of the populations data $\approx \space \frac{2\sigma}{\sqrt{n}}$
$\sigma$ = Standard deviation


[[Sample]] = A smaller collection of units extracted from the population on which we can practically test our hypotheses 
n = The size of the sample (sample size)
x̄ = The mean of the sample data
s = Standard deviation of sample



## Is the data normal?
Use the Shaprio-Wilk test of normality:
if p < 0.05 --> significantly different from normal.

or, for visual:
Levene's test: is the H_1 of difference  between variances statistically significant?


See page 30 of Statistical assumptions, for a guide to R.studio on Shaprio-Wilk:
See page  30 of Statistical assumptions, for a guide to R.studio on the Levene's test.
[[Lecture_4_Statistical_assumptions.pdf]]


If the data is based on time, it can never be normal distributed.


## [[Checking for normality code]]
