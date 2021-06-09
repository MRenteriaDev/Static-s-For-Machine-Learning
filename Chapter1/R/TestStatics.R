xbar = 990; mu0 = 1000; s = 12.5 ; n = 30
t_smple = (xbar - mu0)/(s/sqrt(n));print (round(t_smple,2))

# Critical value from t-tabl
alpha = 0.05
t_alpha = qt(alpha,df= n-1);print (round(t_alpha,3))

#Lower tail p-value from t-table
p_val = pt(t_smple,df = n-1);print (p_val)
