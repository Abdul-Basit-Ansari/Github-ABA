# Github-ABA

[![PyPI version](https://badge.fury.io/py/Github-ABA.svg)](https://badge.fury.io/py/Github-ABA)

## Installation

You can install your package using pip:

pip install Github-ABA


## Usage

This Package Will Help You To Github Crud Opration.

# Example usage code here

For Get Repository

```
from Github-ABA import Github_Crud

github = Github_Crud
repo = github.get_repo("repo_name" , "github_access_token")

```

For Create Repository
```
from Github-ABA import Github_Crud

github = Github_Crud
repo = github.create_repo("repo_name" , "github_access_token")

```

For Delete Repository
```
from Github-ABA import Github_Crud

github = Github_Crud
repo = github.delete_repo("repo_name" , "github_access_token")

```

For Clone Repository On Another Account
```
from Github-ABA import Github_Crud

github = Github_Crud
repo = github.clone_repo_on_another_account("orignal_repo_name" , "orignal_repo_github_access_token" ," clone_repo_github_access_token" ,"clone_repo_name(optional)")

```

For Clone Repository On Another Account
```
from Github-ABA import Github_Crud

github = Github_Crud
repo = github.clone_repo_on_myaccount("orignal_repo_name" ,"orignal_repo_account_username", "your_github_access_token")

```


