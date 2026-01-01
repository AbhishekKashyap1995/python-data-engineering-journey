🧠 Git Cheat Sheet for Data Engineers

Minimal commands. Real usage. No overload.

🔑 Core Concept (MOST IMPORTANT)

A Git repository is any folder that contains a hidden .git directory.

All Git commands work only inside that folder.

📍 Check Where You Are
pwd # show current folder
ls # list files

Always confirm you’re at repo root.

🟢 Daily Workflow (90% of Your Work)
1️⃣ Check status
git status

Shows:

Modified files

New files

Deleted files

2️⃣ Stage changes
git add .

Stages all changes.

Or stage one file:

git add file.py

3️⃣ Commit changes
git commit -m "meaningful message"

Good commit messages:

docs: add Day 2 notes on variables
feat: add CSV reader script
chore: reorganize folder structure

4️⃣ Push to GitHub
git push

Uploads your commits.

🔄 Sync with GitHub
Pull latest changes
git pull

Use when:

Working on multiple machines

GitHub has changes you don’t have locally

🌿 Branch Basics (Later Use)

Check branch:

git branch

Create & switch:

git checkout -b feature-name

Switch branch:

git checkout main

(You won’t need this until team work.)

🔗 Remote Repositories

Check connected GitHub repo:

git remote -v

Add remote:

git remote add origin <repo-url>

🧹 Undo Mistakes (Safe Ones Only)
Unstage a file:
git reset file.py

Discard local changes (DANGER):
git checkout -- file.py

⚠️ This deletes local changes.

🚨 Important Warnings (READ THIS)
❌ Do NOT use casually:
git push --force

Use only when:

You understand why

You are the only contributor

Repo history is broken

🧠 Interview Questions (With Short Answers)
Q: What is Git?

A distributed version control system to track code changes.

Q: What is a repository?

A folder tracked by Git, defined by the presence of a .git directory.

Q: Difference between Git and GitHub?

Git is a tool; GitHub is a remote hosting service.

Q: What does git status do?

Shows the current state of the working directory and staging area.

📌 Best Practices (Follow These)

✔ Commit daily
✔ Write clear commit messages
✔ Keep repo structure clean
✔ Push frequently
✔ Learn Git only when needed

🎯 What You Don’t Need Right Now

❌ Rebase
❌ Cherry-pick
❌ Submodules
❌ Stash (for now)

These come much later.

⭐ One-Line Summary (Memorize)

Git tracks changes locally; GitHub stores them remotely.
