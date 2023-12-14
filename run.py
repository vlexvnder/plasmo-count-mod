import os
import subprocess 

os.chdir(r"C:\Users\la-filipaferreira\Documents\plasmo-count-mod\api")


out = subprocess.check_output(["python", "run_job.py"])

print(
    "\033[91m {}\033[00m".format("Finished job. You can find the results in plasmo-count-mod/data/" + str(out[-(len("output/PlasmoCount-2023-12-14-12_33_25")+2):-2].decode()))
)