import pandas as pd
import os

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

def local_1(args):
    """
    Computes the local beta vector for given covariate (feature) and outcome (dependent) data,
    along with other statistics including the local mean of outcomes and their count. This
    function is designed to work as part of a distributed or federated learning process, where
    local computations are performed before aggregating results globally.

    The workflow within this function includes loading data from CSV files, performing local
    computations to generate statistics, and preparing these statistics for subsequent phases
    of analysis. The results of these computations are structured for easy access and use in
    further processing.

    Args:
        args (dict): A dictionary containing all necessary inputs for the computation, with the following structure:
            - "state": Dictionary containing global state information, such as:
                - "baseDirectory" (str): Path to the base directory where data files are stored.
            - "input": Dictionary with input data and configuration details, including:
                - "covariates" (list): List containing the path to the covariates CSV file.
                - "data" (list): List containing the path to the outcomes CSV file.
                - "X_headers" (list): Headers of the covariate columns to be used in the computation.
                - "y_headers" (list): Headers of the outcome columns to be used in the computation.
                - "lambda" (float): The regularization parameter to be used in calculations.

    Returns:
        dict: A dictionary containing the results of the local computation, structured as follows:
            - "beta_vector_local" (list): Calculated local beta vector.
            - "mean_y_local" (list): Local mean of the outcome variables.
            - "count_local" (int): Count of outcome observations used in the computation.
            - "X_labels" (list): Covariate column headers used in the computation.
            - "y_labels" (list): Outcome column headers used in the computation.
            - "local_stats_dict" (dict): Additional local statistics generated during the computation.
            - "computation_phase" (str): Indicates the current phase of computation ('local_1').

    Note: This function assumes the existence of a `save_cache` function to handle caching of intermediate results.
          It is responsible for saving the computed data for future use, but the specifics of this functionality
          are not covered within this docstring.
    """
    
    ## load the data
    
    base_directory = args["state"]["baseDirectory"]
    input_list = args["input"]
    lamb = input_list["lambda"]

    features_file_path = input_list['covariates'][0]
    outcomes_file_path = input_list['data'][0]
    feature_headers = input_list['X_headers']
    outcome_headers = input_list['y_headers']

    features = load_data(features_file_path, base_directory, feature_headers)
    outcomes = load_data(outcomes_file_path, base_directory, outcome_headers)
    ## end load the data
    
    ## local computation
    beta_vector, local_stats_list, mean_outcomes, len_outcomes = local_stats_to_dict_fsl(features, outcomes)
    ## end local computation
    
    
    ## save cache
    cache_dict = {
        "covariates": features.to_json(orient='split'),
        "dependents": outcomes.to_json(orient='split'),
        "lambda": lamb
    }
    
    save_cache(cache_dict)
    ## end save cache
    
    ## format output
    output_dict = {
        "beta_vector_local": beta_vector,
        "mean_y_local": mean_outcomes,
        "count_local": len_outcomes,
        "X_labels": feature_headers,
        "y_labels": outcome_headers,
        "local_stats_dict": local_stats_list,
        "computation_phase": 'local_1',
    }
    ## end format output

    return output_dict
