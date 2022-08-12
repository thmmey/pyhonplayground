import os
import glob

vmdir = "C:/Users/thmme/ssd/Virtual Machines"
keyword = "MemAllowAutoScaleDown"
substitute = "MemAllowAutoScaleDown = \"FALSE\""

def patchvmx(rootdir, keyword, substitute):
    os.chdir(rootdir)
    for file in glob.glob("*/*.vmx"):
        found = False
        with open(file) as f:
            for line in f.readlines():
                if keyword in line:
                    found = True
                    print("keyword in " + file + " gefunden.")
            if not found:
                with open(file, "a") as f:
                    f.write(substitute + " \n")
                print("keyword in " + file + " ergänzt.")

patchvmx(vmdir, keyword, substitute)



 

