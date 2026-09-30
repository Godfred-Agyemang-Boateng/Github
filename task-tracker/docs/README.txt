Task Tracker
A simple command-line task tracking project.
Author: Nana Bateng
---
# Project Description
`task-tracker` is a text-based task organization project structured to 
demonstrate fundamental Git operations including repository initialization,
 commit tracking, branch creation, feature merging, and file exclusion via `.gitignore`.
---

## Project Structure
task-tracker/
├── .gitignore
├── src/
│   └── tracker.txt
├── data/
│   └── tasks.txt
├── docs/
│   └── README.txt
└── logs/
└── debug.log (ignored by Git)

Create Directories:
- Use mkdir -p to create src/, data/, docs/, and logs/ folders.

Create Starter Files:
- Use touch to create src/tracker.txt, data/tasks.txt, and docs/README.txt.

Populate Tasks: 
- Add initial task entries into data/tasks.txt using echo.

Initialize Git:
- Run git init, stage all files with git add ., and make your initial commit.

Configure .gitignore:
- Add a logs/debug.log file, write logs/ into .gitignore, and commit .gitignore so log files are excluded.

Branch, Edit & Merge:
- Create a feature/add-priority branch, add priority tags to data/tasks.txt, commit the changes, merge the branch back into main, and clean up the feature branch.