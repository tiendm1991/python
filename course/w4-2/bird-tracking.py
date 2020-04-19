import pandas as pd
import numpy as np
birddata = pd.read_csv("bird_tracking.csv", index_col=0)
birddata.head()

# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby("bird_name")

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds["speed_2d"].mean()

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds["altitude"].mean()

birddata.date_time = pd.to_datetime(birddata.date_time)
birddata["date"] = birddata.date_time.strftime("%Y%m%d")
print(birddata.head())