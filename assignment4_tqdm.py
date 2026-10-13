# Assignment 4: Study Progress Tracker (tqdm)
from tqdm import tqdm
import time

delay = 0.1

for task in tqdm(range(20), desc="Study Tasks"):
    time.sleep(delay)

print("All tasks completed!")
