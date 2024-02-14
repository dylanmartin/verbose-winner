import pandas as pd
import os
from nvflare.apis.shareable import Shareable
from cache import save_cache
from local_ancillary import local_stats_to_dict_fsl


def load_data(file_path, base_directory, headers):
    """Loads specified columns from a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        base_directory (str): Base directory where the CSV file is located.
        headers (list): List of column headers to load.

    Returns:
        DataFrame: DataFrame with specified columns.
    """
    full_path = os.path.join(base_directory, file_path)
    return pd.read_csv(full_path)[headers]


def local_1(incoming_shareable, fl_ctx, abort_signal):

    # load the data
    data_directory = "data/"
    features_file_path = "covariates.csv"
    outcomes_file_path = "outcomes.csv"
    feature_headers = incoming_shareable['feature_headers']
    outcome_headers = incoming_shareable['outcome_headers']
    lamb = incoming_shareable["lambda"]

    features = load_data(features_file_path, data_directory, feature_headers)
    outcomes = load_data(outcomes_file_path, data_directory, outcome_headers)
    # end load the data

    # local computation
    beta_vector, local_stats_list, mean_outcomes, len_outcomes = local_stats_to_dict_fsl(
        features, outcomes)
    # end local computation

    # save cache
    cache_dict = {
        "features": features.to_json(orient='split'),
        "outcomes": outcomes.to_json(orient='split'),
        "lambda": lamb
    }

    save_cache(cache_dict)
    # end save cache

    return Shareable({"result": {
        "beta_vector_local": beta_vector,
        "mean_y_local": mean_outcomes,
        "count_local": len_outcomes,
        "X_labels": feature_headers,
        "y_labels": outcome_headers,
        "local_stats_dict": local_stats_list,
        "computation_phase": 'local_1',
    }})
