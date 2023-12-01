import os
import subprocess 
print(
    "Starting job. This may take several minutes!"
)

os.chdir(r"C:\Users\mukht\PlasmoCount\PlasmoCountScripts\api")



subprocess.run(["python", "run_job.py"], capture_output=True)

print(
    "Finished job. You can find the results in PlasmoCount/data/ouput"
)