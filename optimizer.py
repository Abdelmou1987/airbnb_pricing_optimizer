import numpy as np

try:
    import gurobipy as gp
    from gurobipy import GRB
    USE_GUROBI = True
except:
    USE_GUROBI = False
    from scipy.optimize import minimize_scalar

def optimize_price(a, b, p_min, p_max):
    def revenue(p):
        return p * (a - b * p)

    if USE_GUROBI:
        m = gp.Model("airbnb_pricing")
        p = m.addVar(lb=p_min, ub=p_max, vtype=GRB.CONTINUOUS, name="price")
        m.setObjective(p * (a - b * p), GRB.MAXIMIZE)
        m.optimize()
        p_opt = p.X
        rev_opt = revenue(p_opt)
        occupancy_opt = a - b * p_opt

    else:
        result = minimize_scalar(
            lambda x: -revenue(x),
            bounds=(p_min, p_max),
            method="bounded"
        )
        p_opt = result.x
        rev_opt = revenue(p_opt)
        occupancy_opt = a - b * p_opt

    return {
        "optimal_price": round(float(p_opt), 2),
        "optimal_revenue": round(float(rev_opt), 2),
        "occupancy": max(round(float(occupancy_opt), 4), 0)
    }
