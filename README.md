# oh-shgit

This package is designed to help users who are beginner to Git. 

Even though basic Git commands are easy to memorize, most of the time I find myself googling things such as;
- How to reset current branch to remote head?
- How to apply specific stash?
- How to add specific commit from another branch to current branch without messing things up?
- How to revert last commit?
- How to remove a commit from remote? etc. etc.

To solve this problem, gathering up all the google searches that I've done before into a single package could save me some time over years and also helps me to remember those commands easily.

First thing to do is to list all the problems that we have encountered before.

## TODOS

- List all the questions that we've searched for and find the right commands for them.
- Search for the right command when user searches (text-based search, maybe AI in future)
- Display commands to the user with explanations.

## Questions (any help is welcomed)

- How to commit current changes?
- How to push commit to remote?
- How to stash current changes?
- How to discard current changes?
- How to remove commit from local?
- How to remove local branch?
- How to remove remote branch?
- How to ignore files/folders?
- How to revert a commit?
- How to see differences of currenct changes?
- How to see differences in specific commit?
- How to merge branches?
- How to rebase a branch? What is rebase? :)
- Below commands are taken from [StackOverflow](https://stackoverflow.com/questions/tagged/git?sort=MostVotes&edited=true)
- How do I undo the most recent local commits in Git?
- How do I delete a Git branch locally and remotely?
- What is the difference between 'git pull' and 'git fetch'?
- How do I undo 'git add' before commit?
- How do I rename a local Git branch?
- How to modify existing, unpushed commit messages?
- How do I revert a Git repository to a previous commit?
- How do I force “git pull” to overwrite local files?
- How to remove local (untracked) files from the current Git working tree?
- How do I check out a remote Git branch?
- How to make Git “forget” about a file that was tracked but is now in .gitignore?
- Move the most recent commit(s) to a new branch with Git
- How to resolve merge conflicts in Git
- How do I discard unstaged changes in Git?
- How can I reset or revert a file to a specific revision?
- How do I push a new local branch to a remote Git repository and track it too?
- How can I add an empty directory to a Git repository?
- How to clone all remote branches in Git?
- How can I determine the URL that a local Git repository was originally cloned from?
- Undo a Git merge that hasn't been pushed yet
- How to change the URI (URL) for a remote Git repository?
- Reset local repository branch to be just like remote repository HEAD
- Make an existing Git branch track a remote branch?
- How do I update a GitHub forked repository?
- How do I remove a submodule?
- Squash my last X commits together using Git
- How to delete a remote tag?
- Delete commits from a branch in Git
- How do you create a remote Git branch?
- Undoing a git rebase
- Move existing, uncommitted work to a new branch in Git
- View the change history of a file using Git versioning
- Stash only one file out of multiple files that have changed with Git?
- Remove a file from a Git repository without deleting it from the local filesystem
- How do I clone a specific Git branch?
- Difference between “git add -A” and “git add .”
- Find and restore a deleted file in a Git repository
- How to list all the files in a commit?
- Commit only part of a file in Git
- How to get the current branch name in Git?
- How to change the author and committer name and e-mail of multiple commits in Git?
- Comparing two branches in Git?
- How do I make Git ignore file mode (chmod) changes?
- What does cherry-picking a commit with Git mean?
- Git fetch remote branch
- How do you push a tag to a remote repository using Git?
- How to modify a specified commit?
- How do I show the changes which have been staged?
- Showing which files have changed between two revisions
- What is the best (and safest) way to merge a Git branch into master?
- How to change the commit author for one specific commit?
- Download a specific tag with Git
- How to “git clone” including submodules?
- How to list only the file names that changed between two commits?
- How do I revert all local changes in Git managed project to previous state?
- How to retrieve the hash for the current commit in Git?
- How can I delete a file from a Git repository?
- How can I delete all Git branches which have been merged?
- What are the differences between .gitignore and .gitkeep?
- Is there a way to cache GitHub credentials for pushing commits?
- Branch from a previous commit using Git
- See what's in a stash without applying it 
- Viewing unpushed Git commits
- How to recover a dropped stash in Git?
- When do you use Git rebase instead of Git merge?
- How to compare files from two different branches?
- Why do I need to do `--set-upstream` all the time?
- How to selectively merge or pick changes from another branch in Git?


### For Developers
- Requirements: 
  - Python 3.x
  - virtualenv

- ```
  virtualenv venv -p python3
  source venv/bin/activate
  pip install -r requirements.txt
  pip install --editable .
  ggt [keyword] 
  ```
