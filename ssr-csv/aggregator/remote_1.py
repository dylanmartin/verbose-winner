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
