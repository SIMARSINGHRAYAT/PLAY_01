import subprocess
import os

REPO_PATH = "."  # Current directory
FILENAME = "demo_commit.txt"  # Change or create any file you like

# Get user inputs
commit_message = input("Enter your commit message: ")
commit_date = input("Enter the commit date/time (YYYY-MM-DD HH:MM:SS): ")

# Make a change to the file (so there is something to commit)
with open(FILENAME, "a") as f:
    f.write(f"\nCommit at intended date: {commit_date}")

# Stage the file
subprocess.run(["git", "add", FILENAME])

# Set up the environment for custom commit date
env = os.environ.copy()
env["GIT_AUTHOR_DATE"] = commit_date
env["GIT_COMMITTER_DATE"] = commit_date

# Make the commit
subprocess.run(["git", "commit", "-m", commit_message], env=env)

# Push to GitHub
subprocess.run(["git", "push"])

print("✅ Commit made and pushed with your selected date!")
