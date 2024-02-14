from nvflare.apis.shareable import Shareable
import pandas as pd
import numpy as np
from cache import load_cache
import statsmodels.api as sm
from local_ancillary import ignore_nans
import regression as reg


def local_2(incoming_shareable, fl_ctx, abort_signal):

    cache = load_cache()

    X = pd.read_json(cache["features"], orient='split')
    y = pd.read_json(cache["outcomes"], orient='split')

    avg_beta_vector = incoming_shareable["avg_beta_vector"]
    mean_y_global = incoming_shareable["mean_y_global"]

    biased_X = sm.add_constant(X.values)

    SSE_local, SST_local, varX_matrix_local = [], [], []
    for index, column in enumerate(y.columns):
        curr_y = y[column]

        X_, y_ = ignore_nans(biased_X, curr_y)

        SSE_local.append(reg.sum_squared_error(X_, y_, avg_beta_vector[index]))
        SST_local.append(
            np.sum(np.square(np.subtract(y_, mean_y_global[index]))))

        varX_matrix_local.append(np.dot(X_.T, X_).tolist())

    return Shareable({"result": {
        "SSE_local": SSE_local,
        "SST_local": SST_local,
        "varX_matrix_local": varX_matrix_local,
        "computation_phase": 'local_2'
    }})
