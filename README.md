# Install

`git clone git@github.com:Krayorn/git-log.git`

```
cd git-log

pipenv shell

pipenv install
```
then simply run

`py gitlog.py relative_path_to_git_repo`

Two files will then be generated :
- timeline.png (indicating which day and week of the year most commits were made on that repo)
- commit.png (indicating which day of the week and at which hour most commits are made on that repo)
