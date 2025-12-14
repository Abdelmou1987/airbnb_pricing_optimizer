import numpy as np
from scipy.optimize import minimize

def demand_function(price, a, b):
    occ = max(a - b * price, 0)
    return occ

def revenue_function(price, a, b):
    occ = demand_function(price, a, b)
    return -(price * occ * 30)  # negative -> minimize

def optimize_price(min_price, max_price, a, b):
    initial_price = (min_price + max_price) / 2

    bounds = [(min_price, max_price)]

    result = minimize(
        revenue_function,
        x0=[initial_price],
        args=(a, b),
        bounds=bounds,
        method="L-BFGS-B"
    )

    optimal_price = float(result.x[0])
    optimal_occ = demand_function(optimal_price, a, b)
    optimal_rev = optimal_price * optimal_occ * 30

    return {
        "optimal_price": round(optimal_price, 2),
        "optimal_occupancy": round(optimal_occ * 100, 2),
        "optimal_revenue": round(optimal_rev, 2)
    }
