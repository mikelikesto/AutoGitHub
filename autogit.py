
import configparser
import os
import subprocess 
config = configparser.ConfigParser()
config.read("config.ini")
Repo = config["Repo"]
RepoName = config["Location"]
print(list(Repo))
IN=input("which repo would you like to update")
subprocess.run(["Rm -Rf ", RepoName, "&& Gitclone ", Repo])
