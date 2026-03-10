# Imports
from github import Github
from config import config as cfg

# Authenticating key from config.py
apikey = cfg["githubkey"]
g = Github(apikey)

# Acessing repository
repo = g.get_repo("vanelyraa/WSAA-coursework")
