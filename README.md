# Running testApp in Flare simulator

- Launch the docker container using `./dockerRun.sh`
- Run the following command inside the container: `nvflare simulator ./testApp/ -w /tmp/nvflare/workspace_folder/ -t 2`

# Running a job in POC mode

- Launch the docker container using `./dockerRun.sh`
- Run the following commands inside the container:
  - `export NVFLARE_POC_WORKSPACE="/my-workspace/poc-workspace"`
  - `nvflare poc --prepare`
  - `nvflare poc --start`
- This will put the terminal in the `Flare Console`
- Put custom apps in `my-workspace/poc-workspace/admin/transfer`
- `submit_job <job_folder>` will run the job at `admin/transfer/<job_folder>`

# Run the production-mode-test

- cd into `production-mode-test/`
- follow instructions in the `production-mode-test/README.md`

# Run an app that uses local code

- In the container, set the python path to your local code directory. EX `export PYTHONPATH=$PYTHONPATH:/my-workspace/poc-workspace/localcode`
- In the config files for the app, change the component paths to point to the directory containing your modules.
- Example:
  - The `localcode/` directory contains a folder called `np` which is a python module with `__init__.py` and `np_trainer.py`
  - config_fed_client.json for the app looks like this:

```
{
    "format_version": 2,
    "executors": [
      {
        "tasks": [
          "train"
        ],
        "executor": {
          "path": "np.np_trainer.NPTrainer",
          "args": {}
        }
      }
    ],
    "task_result_filters": [],
    "task_data_filters": [],
    "components": []
}
```
