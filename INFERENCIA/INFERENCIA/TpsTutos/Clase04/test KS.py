import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt 
import statsmodels.api as sm

def test_ks(muestra, distribucion, alpha):
    # Calcular la media y el desvío de la muestra
    media = np.mean(muestra)
    desvio = np.std(muestra, ddof=1)
    
    # Estandarizar la muestra
    muestra_estandarizada = [(x - media) / desvio for x in muestra]
    
    # Generar la muestra de la distribución a testear
    muestra_distribucion = distribucion.rvs(size=1000)
    
    # Calcular la función de distribución acumulada empírica
    acumulada_muestra = sm.distributions.ECDF(muestra_estandarizada)
    acumulada_distribucion = sm.distributions.ECDF(muestra_distribucion)
    
    # Calcular el estadístico D
    d_estrella = np.max([np.abs(acumulada_muestra(x)-distribucion.cdf(x)) for x in muestra_estandarizada])
    
    # Calcular la probabilidad de que el estadístico D sea mayor al valor crítico
    proba = 1 - st.kstwobign.cdf(d_estrella/np.sqrt(len(muestra_estandarizada)))
    
    # Realizar el test
    if proba < alpha:
        print('Se rechaza la hipótesis nula')
    else:
        print('No se rechaza la hipótesis nula')

def dn(n): return st.ksone(n)

muestra_uniforme = st.uniform.rvs(size=1000)
media = np.mean(muestra_uniforme)
desvio = np.std(muestra_uniforme, ddof=1)

muestra_uniforme_estandarizada = [(x - media) / desvio for x in muestra_uniforme]

muestra_normal = st.norm.rvs(size=1000)
e = 0.05

# Test de Kolmogorov-Smirnov
acumulada_uniforme = sm.distributions.ECDF(muestra_uniforme_estandarizada)
acumulada_normal = sm.distributions.ECDF(muestra_normal)

d_estrella_uniform = np.max([np.abs(acumulada_uniforme(x)-st.norm.cdf(x)) for x in muestra_uniforme_estandarizada])
d_estrella_normal = np.max([np.abs(acumulada_normal(x)-st.norm.cdf(x)) for x in muestra_normal])
proba_normal = 1 -  dn(1000).cdf(d_estrella_normal)
proba_uniform = 1 - dn(1000).cdf(d_estrella_uniform)

# Generar valores de x para evaluar las ECDF
x_vals_uniforme = np.sort(muestra_uniforme_estandarizada)
x_vals_normal = np.sort(muestra_normal)

# Evaluar las ECDF en los valores de x
y_vals_uniforme = acumulada_uniforme(x_vals_uniforme)
y_vals_normal = acumulada_normal(x_vals_normal)

if proba_uniform < e:
    print('Se rechaza la hipótesis nula para la distribución uniforme')
else:
    print('Se acepta la hipótesis nula para la distribución uniforme')

if proba_normal < e:
    print('Se rechaza la hipótesis nula para la distribución normal')
else:
    print('Se acepta la hipótesis nula para la distribución normal')



# # Graficar los resultados
# plt.plot(x_vals_uniforme, y_vals_uniforme, label='Uniforme')
# plt.plot(x_vals_normal, y_vals_normal, label='Normal')
# plt.legend()
# plt.show()
