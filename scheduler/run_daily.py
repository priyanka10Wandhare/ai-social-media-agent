import time
import sys
import os

# Ensure project root is on sys.path so `from main import ...` works
# when running this script from the `scheduler` directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import main_agent_run

INTERVAL_SECONDS = 10 # daily

def run_scheduler():
    print("📅 Scheduler started (auto-approval enabled).\n")

    while True:
        print("▶ Running scheduled agent job...\n")
        main_agent_run(auto_approve=True)
        print("\n⏳ Waiting for next run...\n")
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    run_scheduler()

