
# Running testApp in Flare simulator
* Launch the docker container using `./dockerRun.sh`
* Run the following command inside the container: `nvflare simulator ./testApp/ -w /tmp/nvflare/workspace_folder/ -t 2`

# Running a job in POC mode

* Launch the docker container using `./dockerRun.sh`
* Run the following commands inside the container:
    * `export NVFLARE_POC_WORKSPACE="/my-workspace/poc-workspace"`
    * `nvflare poc --prepare`
    * `nvflare poc --start`
* This will put the terminal in the `Flare Console`
* Put custom apps in `my-workspace/poc-workspace/admin/transfer`
* `submit_job <job_folder>` will run the job at `admin/transfer/<job_folder>`

# Run the production-mode-test

* cd into `production-mode-test/`
* follow instructions in the `production-mode-test/README.md`