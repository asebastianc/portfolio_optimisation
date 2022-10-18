import numpy as np
import pandas as pd
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.rnsga2 import RNSGA2
from pymoo.optimize import minimize
from pymoo.termination import get_termination
from pymoo.problems import get_problem
from scipy import stats

# load data
df = pd.read_csv("../../data/stocks_info.csv")
daily_returns = pd.read_csv("../../data/daily_returns.csv")
daily_returns = daily_returns.set_index("Date")

# formating data
returns = df.set_index("Ticker")
returns = returns["Annualized Return"].squeeze()

# covariance matrix for computing portfiolio sd
cov_matrix = (daily_returns.cov())

class MyProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var = 20,
                         n_obj = 2,
                         n_constr = 1,
                         xl = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
                         xu = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

    def _evaluate(self, x, out, *args, **kwargs):
    	# mazimize returns
        f1 = (returns[0] * x[0] + returns[1] * x[1] + returns[2] * x[2] + returns[3] * x[3] + returns[4] * x[4] + returns[5] * x[5] + returns[6] * x[6] + returns[7] * x[7] + returns[8] * x[8] + returns[9] * x[9] + returns[10] * x[10] + returns[11] * x[11] + returns[12] * x[12] + returns[13] * x[13] + returns[14] * x[14] + returns[15] * x[15] + returns[16] * x[16] + returns[17] * x[17] + returns[18] * x[18] + returns[19] * x[19]) * - 1 + stats.uniform.rvs(loc = 0.0005203581055095, scale = 0.38301454817263453)
        
        # minimize risk
        weights = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19]]
        weights = np.array(weights, dtype = object)
        f2 = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) + stats.uniform.rvs(loc = 4.248634762318073e-05, scale = 0.01950831956677842)

        # all weights must sum 1
        g1 = x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] + x[10] + x[11] + x[12] + x[13] + x[14] + x[15] + x[16] + x[17] + x[18] + x[19] - 1

        out["F"] = [f1,f2]
        out["G"] = [g1]

problem = MyProblem()
pf = problem.pareto_front()
ref_points = np.array([[0.2, 0.02], [0.4, 0.07]])

# Get Algorithm
algorithm = RNSGA2(
    ref_points = ref_points,
    pop_size = 100,
    epsilon = 0.01,
    normalization = 'front',
    extreme_points_as_reference_points = False)

tickers = ["BRK-B", "GOOG", "AAPL", "YAHOF", "HL.L", "O", "META", "AMZN", "LGEN.L", "ISRG", "SQ", "TSCO.L", "BP", "LLOY.L", "BARC.L", "ULVR.L", "NG.L", "WETF", "GLEN.L", "PHNX.L"]
results_labels = ["Return", "Risk"]

pop_size = 100

dfs_ = []
for g in range(400):

    res = minimize(problem,
               algorithm,
               save_history = True,
               termination = ('n_gen', 200),
               seed = g,
               pf = pf,
               disp = False)

    X = res.X
    F = res.F

    for i in range(len(X)):
        individual = list(X[i])
        if i == 0:
            weights_df = pd.DataFrame([individual], columns = tickers)
        else:
            weights_df.loc[len(weights_df)] = individual
    for n in range(len(F)):
        results = list(np.rint(F[n] * 1000000000).astype(int))
        if n == 0:
            results_df = pd.DataFrame([results], columns = results_labels)
        else:
            results_df.loc[len(results_df)] = results

    nsga2_results = pd.concat([weights_df, results_df], axis = 1)
    nsga2_results.loc[len(nsga2_results)] = "-"
    dfs_.append(nsga2_results)

final_df = pd.concat(dfs_)
final_df.to_csv("../../results/alg2/alg2_results.csv", index = False)