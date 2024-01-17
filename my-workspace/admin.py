from nvflare.fuel.flare_api.flare_api import new_secure_session
import os

print("Starting new secure session")
sess = new_secure_session(
    "admin@nvidia.com",
    "workspace/example_project/prod_00/admin@nvidia.com/"
)

print("Current working directory:", os.getcwd())
job_path = os.path.abspath("workspace/job")
print("Job path:", job_path)

try:

    print(sess.get_system_info())
    job_id = sess.submit_job(job_path)
    print(job_id + " was submitted")
    # sess.monitor_job(job_id)
    # print("job done!")

except Exception as e:
    print(e)
finally:
    sess.close()
