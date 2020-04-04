import os
import sys
from github import Github

git_username = <USERNAME>
git_password = <PASSWORD>

path = <Path>

def create_folder_and_repo():
    folder_name = str(sys,argv[1])
    public_private = str(sys.argv[2])
    os.makedirs(path+folder_name)

    user = Github(git_username, git_password).get_user()
     
     if (public_private == "private")
         print('PRIVATE')
         user.create_repo(folder_name, private=True)
    else:
        print('PUBLIC')
        user.create_repo(folder_name)

    print("You Have Created A Repository {}".format(folder_name))

if __name__ == "__main__"
    create_folder_and_repo()