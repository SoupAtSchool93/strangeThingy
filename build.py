"""
build scripts and assets folder into one pyz
"""
import os
import shutil
scripts = [] # scripts to include in build other than main
folders = [] # folders to include in build
v = "proto0.1" #version
build_cmd = f"python -m zipapp build -o build-{v}.pyz"
if not os.path.exists("build"):
    os.makedirs("build")
else:
    print("build folder already exists, overwrite? (y/n)")
    choice = input(">").lower().strip()
    if choice == "y":
        for i in os.listdir("build"):
            os.remove(os.path.join("build", i))
    elif choice == "n":
        print("aborting build")
        exit()
#snag some extra files and rename main to __main__
shutil.copy("README.md", "build")
shutil.copy("LICENSE", "build")
shutil.copy("main.py", "build/__main__.py")
for i in scripts:
    shutil.copy(i, "build")
for i in folders:
    shutil.copytree(i, os.path.join("build", i), dirs_exist_ok=True)
os.system(build_cmd)
input("Press [Enter] to exit.")