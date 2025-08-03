This repo demonstrates four types of VAR models
* Reduced-Form VAR
* Structural VAR (SVAR)
* VAR with Exogenous Variables (VARX)
* Bayesian VAR (BVAR)—using real-world economic data from FRED.

We use data from FRED:
- Real GDP Growth (GDPC1, quarterly, percent change)
- Inflation Rate (CPIAUCSL, quarterly, percent change)
- Federal Funds Rate (FEDFUNDS, quarterly average) as an exogenous variable for VARX.

We estimate the models, compute impulse response functions (IRFs), and visualize results.
