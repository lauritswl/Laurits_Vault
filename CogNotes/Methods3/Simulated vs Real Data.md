# Simulated vs Real data
## How to move from simulated data to real data:
**Formula**:
types_CHI ~ 0 + Diagnosis + Diagnosis:Visit + (1 + Visit| Child.ID)
0 = intercept
class = $\beta$, coef = DiagASD
class = $\beta$, coef = DiagTD
class = $\beta$, coef 


