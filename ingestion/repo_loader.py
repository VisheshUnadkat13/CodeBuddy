from git import Repo
import os

def clone_repo(repo_url,path="repo"):
    if os.path.exists(path):
        return path
    
    Repo.clone_from(repo_url,path)

    return path
