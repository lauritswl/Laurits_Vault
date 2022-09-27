Written by: Laurits Lyngbæk
Source of information:
Association links: [[003 Methods]]
Tags: #🌿Sprout 
___
# Interaction effects 
![[Interacting predictors.png]]
## Conceptual understanding
Interaction effects are repeatable.

**Main effect:** 
The effect of a predictor on an outcome variable

**Interaction effect:**
The effect of one predictor on an outcome variable as a function of another predictor variable


### How to interpret:
#### **Continuous - Continuous:**
Y ~ 1 + x1 * x2 is very counterintuitive
- X1 is the effect of x1, only when x2 is 0
- X2 is the effect of x2 only when x1 is 0
- X1:X2 is
	- how much the effect of x1 changes when x2 goes from 0 to 1
	- how much the effect of x2 changes when x1 goes from 0 to 1

**Let’s interpret our coefficients:**

Diet_contin = diet(slope|time = 0)
Time = Time(slope| diet = 0) 
Diet_contin:Time = How much Time & Diet coefficients changes.

![[weiht by diet and time.png]]

**Case:**
```
weight intercepts at 12.8
and the slope is calculated:

(1.81*(-0.25*X2))*X1+(10.8*(-0.25*X1))*X2

So:
weight = 12.8 +
		(1.81*(-0.25*X2))*X1+
		(10.8*(-0.25*X1))*X2

```



#### **Categorical - Categorical**
Only decides the intercept, as it is categorical.
two by two categorical design.

In this example its only if we interpret as interacting effects, there is any effect:
![[Categorical - Categorical.png]]


**Input for plot:**
```{r}
library(emmeans)
model<-lm(outcome~ predictor1*preictor2) 
emmip((model, predictor1 ~ preictor2, CIs = TRUE) )

```
**Output for code:**
![[Cont Cont plot.png]]

For harder plots see slide 29-31 in [[Lecture_11_Interaction_analysis]]
or use easy (ugly) way / 
```{r}
plot(effects::allEffects(model)
```

#### **Categorical - Continuous**
Reaction time ~ Gender + Height
```
main fixed effect (int - female)= 10
GenderM = -5
Height = 1
GenderM:Height =0,2
```
If your are female:
rt = 10 + 1 * X(height),

If you are a male:
rt =  (5-5)+(1+0.2) * X(height) <=>
rt = 5 +1.2 * X(height)




[[Interacction effects in r]]




