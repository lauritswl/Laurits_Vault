By: Laurits Lyngbæk
Slides:
![[M3_2022_W2_Bayes.pptx]]
___

# General intro to Baysean inference
The probability of a theory (parameter values) given the data is
**Prior *x* Likelihood = Posterior** 
* **Prior**: What we already knew
* **Likelihood**: what the data tells us 
* **Posterior**: What we know now

**Why Bayes??***
* **Principled** way of building your model:
	* Thinking through what you know
	* Thinking trough (with plots!) the implications of what you think you know
* **Easy to break**: It fails often, it **fails catastrophically**, with nice diagnostics


# Building the simplest model: 
## Describing the data as Gaussian

``` {Dataset for IDS}
d <- read.csv('vowel_space_area_data.csv')
glimpse(d)


## Rows: 48
## Columns: 7
## $ X             <int> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1…
## $ Subject       <chr> "AF", "AN", "CL", "DM", "IA", "JA", "JE", "KA", "KV", "L…
## $ Register      <chr> "ADS", "ADS", "ADS", "ADS", "ADS", "ADS", "ADS", "ADS", …
## $ ArticulationS <dbl> 0.76015464, -1.28956792, -0.85914839, -0.81478879, 0.797…
## $ ChildSex      <chr> "m", "m", "f", "m", "f", "m", "f", "m", "m", "m", "m", "…
## $ ChildAge      <int> 20, 22, 16, 12, 23, 24, 21, 14, 16, 16, 12, 16, 23, 12, …
## $ First_child   <chr> "No", "Yes", "No", "No", "No", "Yes", "Yes", "No", "Yes"…
```
```{r} #🖥️Code 
get_prior(Articulation_f1, data = d, family = gaussian)
```
**Intercept** (or mean expected value of articulation, here = mu $\mu$)
**Sigma** $\sigma$ (or average expected error when predicting datapoints from mu)

### Setting priors: What do we know?
The data is standardizes, and therefore scaled to be centred at 0, and gaussian.
**Intercept** (mu $\mu$) =The data has been scaled: centered at 0, divided by sd (so its sd is 1)
```
prior(normal(0, 1), class=Intercept)
```
**SD** (sigma $\sigma$) = Scaled: 1 SD = 1
* What about sd of the sigma?
	* Let’s be optimistic and say that we could in principle (but unlikely!) go all the way down to 0:
		* 1 to 0 is 1, which corresponds to 2 sd, so 0.5 (2 sd deviations is likely)
```
Prior(normal(1, 0.5), class=sigma)
```

![[Standardized priors.png]]

### Lets check:
```{r}
# {**defining priors**}

Articulation_p1 <- c(prior(normal(0,1), class= Intercept),  
				     prior(normal(1, 0.5), class= sigma))
```

```
# **The mean expected value**
rnorm(1e4, mean=0, sd = 1)

# Add the sigma
rnorm(1e4, mean=rnorm(1e4, 0, 1), sd = rnorm(1e4, 1, 0.5))
```


# Difference of means as a Gaussian distribution

