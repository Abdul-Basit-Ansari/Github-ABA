from github import Github
import requests
import json
import os


class Github_Crud:

    def create_repo(repo_name:str , github_access_token:str ):
        '''Create Repository On Github Account'''
        ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , github_access_token)
        user_github = Github(ACCESS_TOKEN)
        user = user_github.get_user()

        new_repo = user.create_repo(f"{repo_name}")
        return new_repo

    def clone_repo_on_another_account(orignal_repo_name:str , orignal_repo_github_access_token:str  , clone_repo_github_access_token:str ,clone_repo_name:str = ""):
        '''Clone Repository From Your Github Account To Another Github Account'''
        ORIGNAL_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , orignal_repo_github_access_token)
        CLONE_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , clone_repo_github_access_token)
        orignal_github = Github(ORIGNAL_ACCESS_TOKEN)
        clone_github = Github(CLONE_ACCESS_TOKEN)
        orignal_user = orignal_github.get_user()
        orignal_username = orignal_github.get_user().name
        clone_user = clone_github.get_user()
        orignal_repo = orignal_user.get_repo(orignal_repo_name)
        if clone_repo_name == "":
            clone_repo_name = orignal_repo_name
        clone_repo = clone_user.create_repo(clone_repo_name , description=orignal_repo.description)
        url = f"https://api.github.com/repos/{orignal_username}/{orignal_repo_name}/contents"
        orignal_repo_content = requests.get(url)
        try:
            files = json.loads(orignal_repo_content.text)
            #  Get & Upload each file
            for file in files:
                file_url = file["download_url"]
                file_response = requests.get(file_url)
                data  = file_response.content
                clone_repo.create_file(file["name"], 'Initial Commit', data, branch='main')
            return clone_repo.url    
        except:
            clone_repo.delete()

    def clone_repo_on_myaccount(orignal_repo_name:str  ,orignal_repo_account_username:str , your_github_access_token:str):
        '''Clone Repository From Another Github Account To Your Github Account'''
        ORIGNAL_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , your_github_access_token)
        orignal_github = Github(ORIGNAL_ACCESS_TOKEN)
        orignal_user = orignal_github.get_user()
        clone_repo = orignal_user.create_repo(orignal_repo_name )
        url = f"https://api.github.com/repos/{orignal_repo_account_username}/{orignal_repo_name}/contents"
        orignal_repo_content = requests.get(url)
        try:
            files = json.loads(orignal_repo_content.text)
            #  Get & Upload each file
            for file in files:
                file_url = file["download_url"]
                file_response = requests.get(file_url)
                data  = file_response.content
                clone_repo.create_file(file["name"], 'Initial Commit', data, branch='main')
            return clone_repo.url    
        except:
            clone_repo.delete()

    def validate_github_token(github_access_token):
        '''Validate Github Token'''
        ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , github_access_token)
        headers = {
            "Authorization": f"Token {ACCESS_TOKEN}"
        }

        response = requests.get("https://api.github.com/user", headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    def delete_repo(repo_name:str , github_access_token:str):
        '''Delete Github Repository'''
        ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , github_access_token)
        user_github = Github(ACCESS_TOKEN)
        user = user_github.get_user()
        
        repo = user.get_repo(f"{repo_name}")
        repo.delete()

    def get_repo(repo_name:str , github_access_token:str):
        '''Get Github Repository'''
        ACCESS_TOKEN = os.getenv("ACCESS_TOKEN" , github_access_token)
        user_github = Github(ACCESS_TOKEN)
        user = user_github.get_user()
        
        repo = user.get_repo(f"{repo_name}")
        return repo
  
