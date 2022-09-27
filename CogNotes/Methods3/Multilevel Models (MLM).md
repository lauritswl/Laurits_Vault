# MLM
* Building models one step at a time
* Use the information you have (and you always have information)
* Obsessively check what you are telling the model
* Don't be afraid to change and adjust your models
* Build a good workflow to structure your modelling activity

## Heretical structure mixed-effect models
![[Nested Varriables.png]]
When a nested structure is nested, the r-syntax is:

```
Test score ~ Time + (1|Student/Class) + $\epsilon$
```

In this example the students use of time is also dependent on what class they are in.

## Too many levels!
Many hierachial models with levels > 2 or inclusion of random a slope often leads to error message ==(isSingular!)==.

## Multilevel models
Are models that explicitly acknowledge that parameters might vary 
* By participant
* By stimulus
Are models that partially pool information
- The values in the data are not taken at face value
- Estimates for individuals are adjusted by what we know about other individuals (shrinkage)
### Shrinkage
Shrinkage feels like cheating, as we change our data post-collecting.
**Therefore**,
We need to think whether it is acceptable for us to shrink our data, from both
**Data perspectives** (How much we trust our data):
- How robust is the measurement?
- Is one data point per condition persuasive? 
**Theoretical perspectives**:
- Do individual variations of this size make sense?
- What could be the source of such variation?
- How would we investigate it?
**Collect more data,** think about systematic sources of variation, but also asses implications (how would a neural network learn form these data?)

### Using informed priors:
Bayesian doesn't forget what happened in previous studies:
