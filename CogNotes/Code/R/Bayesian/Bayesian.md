


## Setting up the analysis
- Define the **formula**
- Define the *priors* + plots plots plots
- *Prior* **predictive checks**
- Model *fitting* and quality check
- *Posterior* **predictive checks**
- Parameter recovery
- No pooling, full pooling partial pooling

- Making sure the model can do what we think it should
- Identifying desired sample sizes (or alternatively acceptable effect sizes)

## Setting up the model
- UniqueWords_f0 <- bf(UniqueWords ~ 1)
- UniqueWords_f1 <- bf(UniqueWords ~ 0 + Diagnosis)
- UniqueWords_f2 <- bf(UniqueWords ~ 0 + Diagnosis + Diagnosis:Visit)
- UniqueWords_f3 <- bf(UniqueWords ~ 0 + Diagnosis + Diagnosis:Visit - (1 + Visit|ID))
	- Add effect (all intercept are different for each child)
- UniqueWords_f4 <- bf(UniqueWords ~ 0 + Diagnosis + Diagnosis:Visit - (1 + Visit|gr(ID, by = Diagnosis)))
	- We group ID by diagnosis, so the model doesn't shrink the autistic children further towards the mean, as their difference is a *marker* of the *autistic learning curves variety*
