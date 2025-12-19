#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)
 
def mean_std_distribution(distribution):
    mean = distribution.mean()
    std = distribution.std()
    return mean, std

def get_distributions():
    return {
        # Lois discrètes
        "Loi de Dirac": scipy.stats.rv_discrete(values=([3], [1])),
        "Loi Uniforme discrète": scipy.stats.randint(low=1, high=7),
        "Loi Binomiale": scipy.stats.binom(n=10, p=0.5),
        "Loi de Poisson (discrète)": scipy.stats.poisson(mu=3),
        "Loi Zipf-Mandelbrot": scipy.stats.zipf(a=2),

        # Lois continues
        "Loi Normale": scipy.stats.norm(loc=0, scale=1),
        "Loi Log-normale": scipy.stats.lognorm(s=0.5, scale=np.exp(0)),
        "Loi Uniforme continue": scipy.stats.uniform(loc=0, scale=1),
        "Loi Chi-deux": scipy.stats.chi2(df=4),
        "Loi Pareto": scipy.stats.pareto(b=3)
    }

def compute_all_means_std():
    distributions = get_distributions()

    print("Moyenne et écart type des lois statistiques\n")

    for name, dist in distributions.items():
        mean, std = mean_std_distribution(dist)
        print(f"{name:20s} | moyenne = {mean:.4f} | écart type = {std:.4f}")

if __name__ == "__main__":
    compute_all_means_std()
