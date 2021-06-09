game_points <- c(35,56,43,59,63,79,35,41,64,43,93,60,77,24,82)

# Varianza
dt_var = var(game_points)
print(round(dt_var,2))

# Desviación Standard
dt_std = sd(game_points); print(round(dt_std,2))

#Rango
range_val<-function(x) return(diff(range(x)))
dt_range = range_val(game_points)
print(dt_range)

dt_quantile = quantile(game_points,probs = c(0.2,0.8,1.0))
print(dt_quantile)
dt_iqr = IQR(game_points); print(dt_iqr)
