# Overview

This repository demonstrates a way to use NVIDIA flare's production mode to provision a secure network and execute a federated analysis run.

# Provisioning

Provision packages need to be distributed to each entity in the network of a project.

Run the following command to generate packages:
```bash
cd Provisioner/ && ./launch.sh
```

The packages will be found in the following directory (or `prod_01` `prod_02` etc.)
```
Provisioner\to_mount\example_project\prod_00
```

Move the packages found there into the respective directories of their network entity and rename them. For example:

- The contents of `Provisioner\to_mount\example_project\prod_01\admin@nvidia.com` will go into `Admin\to_mount\provisioned`
- The contents of `Provisioner\to_mount\example_project\prod_01\host.docker.internal` will go into `Server\to_mount\provisioned`

Note: The `name` property of a server resource in `project.yml` needs to be a FQDN that the clients can connect to. Hence the provision package for the server being named `host.docker.internal`.

# Executing a Job

A `Job` in Flare is a definition of a workflow to be executed by the provisioned network. An example job is defined in `Admin\to_mount\job`. An Admin component submits a job to the Server. The server then distributes the tasks to the clients and initiates the run.

To execute the demo job:

1. Provision each network entity (Admin, Server, Site1, Site2) as described above.
2. Launch all of the network entities by going into each of the following directories and running `./launch.sh`:
   - `Server/`
   - `Site1/`
   - `Site2/`
   - `Admin/` (Make sure Admin is last since it will submit the job when launched)

# View Results (TODO)
Evidence that a run has taken place can be found in each site's respective directory.