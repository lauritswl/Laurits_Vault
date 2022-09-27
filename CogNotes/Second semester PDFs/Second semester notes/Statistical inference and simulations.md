Written by: Laurits Lyngbæk
Source of information: [[Methods ROS.pdf|Regression and other stories]]
Association links: [[103 Methods 2]]
Tags: #🌿Sprout 
___
# Statistical Inference
**Statistical inference** can be formulated as a ***set of operations*** on data that yield estimates and uncertainty statements about predictions and ==parameters== of some underlying process or **population**.
==Parameters==: Unknown quantitates (often greek letters $\alpha \space or \space beta$)


**Statistical inference is used to learn from incomplete or imperfect data.**
### Sampling model
In the *sampling model* we are interested in learning some characteristics about about a population: this could be the mean and standard deviation of the heights of Danish women. 

To get this information we must estimate it from a sample of the population.

### Measurement error model
In the *measurement error model* we are interested in learning something about the underlying pattern/law. As an example this could be understanding $\alpha$ and $\beta$ in the model $y_i=\alpha+\beta x_i$, but we always encounter errors in our measurements, and therefore end up with  $y_i=\alpha+\beta x_i+\epsilon_i$. Errors need not be additive.

### Model error
*Model error* refers to the inevitable imperfections of the models that we apply to real data.


## Sampling distribution:
The *sampling distribution* refers to the *set of possible possible datasets* that can be observed when sampling from a population: along with the probability of the possible values.  A more accurate term might be “probabilistic data model”, as variation doesn't need to be modeled by any sampling process.

**A simple example:**
For a simple random sample of size *n* from a population of size *N*, then the sampling distribution is the set of all samples of size *n*, all with equal probabilities.

**A bit more complex example:**
for $y_i=\alpha+\beta x_i+\epsilon_i$, the sampling distribution is the set of possible datasets obtained from these values of $x_i$ , drawing new errors $\epsilon_i$ from their assigned distribution.

## Jargon
==*Parameters*== = Unknown quantitates (often greek letters $\alpha \space or \space beta$)
For $y_i=\alpha+\beta x_i+\epsilon_i$ the parameters $\alpha$ and $\beta$ are called *coefficients*, the standard deviation $\sigma$ is called *a scale or variance parameter*.




## Exponentional relation
The data has exponential relations if a log-transformation of results and data-points puts the relation on a straight line 
$$y=ae^{bt}<=>log(y)=log(ae^{bt})<=>log(y)=log(ae^{bt})<=>log(y)=log(a)+log(e^{bt})<=>log(y)=log(a)+bt$$

### Power laws
![[Pasted image 20220215135801.png]]

![[Log-normal distribution.png]]

## Hidden factors for a gaussian distribution 

![[Probability distrubution.png]]
![[Normal Distribution properties.png]]

# Simulation




