import subprocess
import os
from datetime import datetime, timedelta

# --------------- USER CONFIGURATION ---------------

REPO_PATH = "./PLAY_01" # Update this if needed (relative or absolute path)
FILENAME = "heatmap.txt" # File to touch/change every commit
START_DATE = "2025-06-01" # yyyy-mm-dd
END_DATE = "2025-06-15"   # yyyy-mm-dd
COMMITS_PER_DAY = 3      # Set how many commits per day

# --------------- SCRIPT LOGIC ---------------

os.chdir(REPO_PATH)
start = datetime.strptime(START_DATE, "%Y-%m-%d")
end = datetime.strptime(END_DATE, "%Y-%m-%d")
delta = timedelta(days=1)

current = start

while current <= end:
    for c in range(COMMITS_PER_DAY):
        commit_time = current.replace(hour=12, minute=c*2) # Adjust as you like
        commit_date = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

        # Change file so commit has effect
        with open(FILENAME, "a") as f:
            f.write(f"Commit on {commit_date}\n")

        # Stage the change
        subprocess.run(["git", "add", FILENAME])

        # Set commit environment variables
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date

        # Commit!
        subprocess.run(["git", "commit", "-m", f"Heatmap commit for {commit_date}"], env=env)
        print(f"Committed for {commit_date}")

    current += delta

# ---- Push all commits at the end ----
subprocess.run(["git", "push"])
print("✅ All commits made and pushed!")
