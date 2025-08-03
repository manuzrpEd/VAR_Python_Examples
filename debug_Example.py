import pandas as pd
import numpy as np
import statsmodels.api as sm

np.random.seed(0)
df = pd.DataFrame({
    'y1': np.random.randn(100),
    'y2': np.random.randn(100)
})

B = np.array([[1.0, 0.0],
              ["E", 1.0]], dtype=object)

svar_mod = sm.tsa.SVAR(df, svar_type='B', B=B)
svar_res = svar_mod.fit()#B_guess=np.array([0.1])

svar_res.k_exog_user = 0
print(svar_res.summary())