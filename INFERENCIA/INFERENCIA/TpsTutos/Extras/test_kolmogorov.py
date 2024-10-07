import scipy.stats as stats
import numpy as np

# Definir el número de muestras
N = 100

# Generar 100 muestras de una distribución uniforme (0, 1) y una normal (0, 1)
uniform_samples = stats.uniform.rvs(0, 1, N)
n_samples = stats.norm.rvs(0, 1, N)

# Estandarizar las muestras de la distribución uniforme
mean_uniform = np.mean(uniform_samples)
std_uniform = np.std(uniform_samples)
standardized_uniform_samples = (uniform_samples - mean_uniform) / std_uniform


# Definir la función de distribución acumulativa empírica
def acumulada_empirica(data):
    sorted_data = np.sort(data)
    n = len(sorted_data)
    
    def cdf(x):
        count = np.searchsorted(sorted_data, x, side='right')
        return count / n
    
    return cdf

# Calcular la CDF empírica de las muestras estandarizadas
ecdf = acumulada_empirica(n_samples)

# Calcular el estadístico KS manualmente
d_star = 0
for x in n_samples:
    d = abs(ecdf(x) - stats.norm.cdf(x))
    if d > d_star:
        d_star = d

# Comparar el estadístico KS con el valor crítico para un nivel de significancia del 5%
p_value = 1 - stats.ksone.cdf(d_star, N)

if p_value <= 0.05:
    print('Rechazo H0')
else:
    print('No rechazo H0')


