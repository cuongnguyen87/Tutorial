import requests
import datetime

apiUrl = "https://api.github.com/users/SeleniumHQ/repos"
data =requests.get(apiUrl).json()

print("Find total open issues all repositories")
Total = 0
for i in range(0, len(data)):
    Open_Issue = data[i]['open_issues_count']
    Total = Total + Open_Issue

print("Total open issues :{}".format(Total),"\n\n")



print("The Repository has most watcher")
List_Watcher = {}
for j in range(0, len(data)):
    repository = data[j]['name']
    Watcher = data[j]['watchers_count']
    List_Watcher.update({repository:Watcher})
Max_watcher = max(List_Watcher,key=List_Watcher.get)

print("The Repository has most watcher:{}".format(Max_watcher),"\n\n")



print("Sort the repositories by date updated in descending order")
List_repo = {}
dateformat = '%Y-%m-%dT%H:%M:%SZ'
for j in range(0, len(data)):
    repository = data[j]['name']
    time = datetime.datetime.strptime(data[j]['updated_at'], dateformat)
    List_repo.update({repository:time})
List_repo = sorted(List_repo, key=List_repo.get)

print("List repositories after sorting:{}".format(List_repo))



