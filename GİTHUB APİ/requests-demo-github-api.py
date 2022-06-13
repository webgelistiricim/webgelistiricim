import requests
import json

class Github:
    pass
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token_url = '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'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+ username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username)
        return response.json()
    def createRepository(self,name):
        response = requests.get(self.api_url+'/user/repo?/acces_token='+ self.token_url, json={
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://batuhandavarci.com.tr",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
  }
        })
        return response.json()
github = Github()
while True:
    secim = input("1) Find User\n2) Get Repositories\n3) Create Repositories\n4) Exit\nSeçiminiz: ")
    if secim == '4':
        break
    else:
        if secim == '1':
             username = input("username: ")
             result = github.getUser(username)
             print(f"name: {result['name']}, public repos: {result['public_repos']}, followers: {result['followers']}")
        elif secim == '2':
            username = input("username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo)
        elif secim == '3':
            name = input("Repository Name: ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Geçersiz İşlem Yaptınız.")
