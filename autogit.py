
import configparser
import os
import subprocess 
config = configparser.ConfigParser()
config.read("repoconfig.ini")
Repo = config["Repo"]
RepoName = config["RepoName"]
subprocess.run(["Rm -Rf ", RepoName, "&& Gitclone ", Repo])
