import numpy as np

def compute_global_mean(mean_y_local, count_local):
    """Computes the global mean of dependent variables."""
    weighted_means = np.multiply(mean_y_local, count_local)
    global_mean = np.sum(weighted_means) / np.sum(count_local)
    return global_mean

def compute_degrees_of_freedom(count_local, num_features):
    """Computes the global degrees of freedom."""
    return np.sum(count_local) - num_features

def remote_1(args):
    """
    Computes the global beta vector, global mean of dependent variables (mean_y_global), 
    and degrees of freedom (dof_global) based on local statistics.

    Args:
        args (dict): A dictionary with the following structure:
            - "input": A nested dictionary containing data from multiple sites, 
              where each key represents a site ID and its value is another dictionary with:
                - "beta_vector_local": A list or array of local beta vectors from each site.
                - "mean_y_local": A list or array of local means of dependent variables from each site.
                - "count_local": An integer representing the count of observations at each site.
                - "computation_phase": A string indicating the current phase of computation.
                - "X_labels": List of strings specifying column headers for covariates used in the model.
                - "y_labels": List of strings specifying column headers for dependent variables used in the model.
                - "local_stats_dict": A dictionary with local statistics for further computations.
            - "cache": An initially empty or previously used cache dictionary for storing intermediate results.

    Returns:
        dict: A dictionary with two main keys:
            - "output": Contains the results of the global computation:
                - "avg_beta_vector": A list representing the average beta vector computed from all sites.
                - "mean_y_global": A list representing the global mean of dependent variables.
                - "computation_phase": The current computation phase ('remote_1').
            - "cache": A dictionary for caching results, which includes:
                - "avg_beta_vector": Cached average beta vector.
                - "mean_y_global": Cached global mean of dependent variables.
                - "dof_global": Cached degrees of freedom, calculated globally.
                - "X_labels": Column headers for covariates used in the model.
                - "y_labels": Column headers for dependent variables used in the model.
                - "local_stats_dict": Cached dictionary of all local statistics.

    The function aggregates local statistics to compute global metrics essential for distributed or federated analyses.
    """
    sites_data = args["input"]
    site_ids = list(sites_data.keys())

    # Assuming all sites have the same number of features for simplicity
    num_features = len(sites_data[site_ids[0]]["beta_vector_local"])

    beta_vectors = np.array([sites_data[site]["beta_vector_local"] for site in site_ids])
    mean_y_local = np.array([sites_data[site]["mean_y_local"] for site in site_ids])
    count_local = np.array([sites_data[site]["count_local"] for site in site_ids])

    avg_beta_vector = np.mean(beta_vectors, axis=0)
    mean_y_global = compute_global_mean(mean_y_local, count_local)
    dof_global = compute_degrees_of_freedom(count_local, num_features)

    output_dict = {
        "avg_beta_vector": avg_beta_vector.tolist(),
        "mean_y_global": mean_y_global.tolist(),
        "computation_phase": 'remote_1'
    }

    cache_dict = {
        "avg_beta_vector": avg_beta_vector.tolist(),
        "mean_y_global": mean_y_global.tolist(),
        "dof_global": dof_global,
        # Assuming X_labels and y_labels are consistent across sites; taking from the first site
        "X_labels": sites_data[site_ids[0]]["X_labels"],
        "y_labels": sites_data[site_ids[0]]["y_labels"],
        "local_stats_dict": [sites_data[site]["local_stats_dict"] for site in site_ids]
    }

    return {"output": output_dict, "cache": cache_dict}
