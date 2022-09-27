
What is a good model?

*Criteria for model comparison*:
- **Predictive performance** 
	- Test model on holdout data (requires extra data)
	- loo (leave one out) as an alternative to BIC and AIC.
		- Gives you a score: elpd (expeceted log predictive density)
		- Function for comparing to functions: {loo::compare(loo1,loo2)}
* **Theoretical background** - validity (does the model answer my scientific question?)
* **Sensible prior predictive checks**
* **Posterior predictive checks** (not a direct test of predictive power, but a qualitative test) 
	* {rstanarm pp_check (fit)}
* 
* 
