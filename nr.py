a="hey bro"
print(a)

"""
cd your-folder
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo-url>
git branch -M main
git push -u origin main
"""


"""
# Git Commands – Simple Copyable Cheat Sheet

## A) Setup (Do Once)

```
git --version                 # Check Git installed
git config --global user.name "Your Name"   # Set username
git config --global user.email you@example.com  # Set email
```

## B) Create / Clone Repository

```
git init                      # Create new repo
git clone <url>              # Clone existing repo
```

## C) Check Status

```
git status                   # See changes
```

## D) Add Files (Staging)

```
git add file.txt             # Add one file
git add .                    # Add all files
```

## E) Commit Changes

```
git commit -m "message"      # Save changes
git commit --amend           # Edit last commit
```

## F) View History

```
git log                      # Full history
git log --oneline            # Short history
git log --oneline --graph --all  # Visual graph
```

## G) Branching

```
git branch                   # List branches
git branch new-branch        # Create branch
git checkout new-branch      # Switch branch
git checkout -b new-branch   # Create + switch
```

## H) Merge

```
git merge branch-name        # Merge branch
```

## I) Remote Repository

```
git remote add origin <url>  # Connect to remote
git remote -v                # Show remotes
git push origin main         # Push code
git push -u origin main      # First push
git pull origin main         # Pull + merge
git fetch                    # Fetch only
```

## J) Undo / Reset / Restore

```
git restore file.txt                 # Undo file changes
git restore --staged file.txt       # Unstage file
git reset --soft HEAD~1             # Undo commit (keep staged)
git reset --mixed HEAD~1            # Undo commit (keep files)
git reset --hard HEAD~1             # Delete everything (danger)
git revert <commit-id>              # Safe undo
```

## K) Stash

```
git stash                    # Save temporarily
git stash list               # Show stashes
git stash apply              # Apply stash
git stash pop                # Apply + remove
```

## L) Tagging

```
git tag v1.0                 # Create tag
git push origin v1.0         # Push tag
```

## MOST IMPORTANT FLOW

```
git init
git add .
git commit -m "message"
git remote add origin <url>
git push -u origin main
```

## QUICK MEMORY TIP

```
git add    -> select files
git commit -> save changes
git push   -> upload to GitHub
```
"""
