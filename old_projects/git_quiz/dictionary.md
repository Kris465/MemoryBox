# Git Glossary for Quest

## Level 1 - Navigation and Status

git clone <url>
Create a local copy of a remote repository on your computer.
Создать локальную копию удалённого репозитория на вашем компьютере.

git status
Show the current state of the working directory and staging area.
Показать текущее состояние рабочей директории и области подготовленных файлов (staging area).

git log
Display the commit history.
Показать историю коммитов.

git log --oneline
Show commit history with each commit on a single line (hash and message).
Показать историю коммитов, каждый коммит на одной строке (хэш и сообщение).

git log --oneline --graph --all
Show commit history with branch visualization and all references.
Показать историю коммитов с визуализацией веток и всеми ссылками.

git diff
Show changes between working directory and last commit (unstaged changes).
Показать изменения между рабочей директорией и последним коммитом (неподготовленные изменения).

## Level 2 - Files and Commits

git add <file>
Stage a file for the next commit.
Подготовить файл для следующего коммита (добавить в staging area).

git add .
Stage all changes (new, modified, deleted) in the current directory.
Подготовить все изменения (новые, изменённые, удалённые) в текущей директории.

git commit -m "message"
Create a commit with the staged changes and the given message.
Создать коммит с подготовленными изменениями и указанным сообщением.

git push <remote> <branch>
Upload local commits to a remote repository.
Отправить локальные коммиты в удалённый репозиторий.

git push origin main
Upload commits to the main branch of the origin remote.
Отправить коммиты в ветку main удалённого репозитория origin.

git pull <remote> <branch>
Download changes from a remote repository and merge with local branch.
Загрузить изменения из удалённого репозитория и объединить с локальной веткой.

git show <commit-hash>
Display the changes and metadata of a specific commit.
Показать изменения и метаданные конкретного коммита.

git show <commit-hash>:<file-path>
Display the content of a specific file as it existed in a given commit.
Показать содержимое конкретного файла в том виде, в котором оно было в указанном коммите.

## Level 3 - History Search

git log --grep="pattern"
Find commits whose message contains the pattern.
Найти коммиты, сообщение которых содержит указанный образец.

git log -S"string"
Find commits that added or removed the exact string (pickaxe search).
Найти коммиты, которые добавили или удалили точную строку (поиск "киркой").

git log --follow <file>
Show the history of a file including renames.
Показать историю файла, включая переименования.

git blame <file>
Show who last modified each line of a file and in which commit.
Показать, кто последним изменял каждую строку файла и в каком коммите.

git diff <hash1>..<hash2>
Show changes between two commits.
Показать изменения между двумя коммитами.

git diff <hash>^!
Show changes introduced by a single commit (compare with its parent).
Показать изменения, внесённые одним коммитом (сравнение с родительским коммитом).

git checkout <commit-hash>
Switch the working directory to a specific commit (detached HEAD state).
Переключить рабочую директорию на конкретный коммит (состояние отсоединённого HEAD).

## Level 4 - Branches and Remote

git branch
List all local branches.
Показать список всех локальных веток.

git branch -a
List all branches (local and remote-tracking).
Показать список всех веток (локальных и отслеживающих удалённые).

git branch <branch-name>
Create a new branch.
Создать новую ветку.

git checkout <branch-name>
Switch to an existing branch.
Переключиться на существующую ветку.

git checkout -b <branch-name>
Create and switch to a new branch.
Создать новую ветку и сразу переключиться на неё.

git merge <branch-name>
Merge the specified branch into the current branch.
Влить указанную ветку в текущую ветку.

git branch -d <branch-name>
Delete a local branch.
Удалить локальную ветку.

git remote -v
Show remote repository URLs (fetch and push).
Показать URL-адреса удалённого репозитория (для fetch и push).

## Level 5 - Recovery and Advanced

git reflog
Show the history of HEAD movements (useful for finding lost commits).
Показать историю перемещений HEAD (полезно для поиска потерянных коммитов).

git reset HEAD~1
Undo the last commit, keeping changes in the working directory.
Отменить последний коммит, оставив изменения в рабочей директории.

git reset --hard <commit-hash>
Revert to a specific commit and discard all changes after it.
Вернуться к конкретному коммиту и отбросить все изменения после него.

git stash
Temporarily save uncommitted changes.
Временно сохранить незакоммиченные изменения.

git stash list
List all stashed changes.
Показать список всех временных сохранений (stash).

git stash show -p <stash>
Display the content of a specific stash.
Показать содержимое конкретного временного сохранения.

git stash pop
Apply the most recent stash and remove it from the stash list.
Применить последнее временное сохранение и удалить его из списка.

git commit --amend -m "new message"
Replace the last commit with a new one (change message or add forgotten files).
Заменить последний коммит новым (изменить сообщение или добавить забытые файлы).

git restore <file>
Discard unstaged changes in a file (revert to last commit).
Отменить неподготовленные изменения в файле (вернуться к последнему коммиту).

git restore --staged <file>
Unstage a file (undo git add).
Убрать файл из области подготовленных (отменить git add).