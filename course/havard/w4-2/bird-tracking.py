import  datetime

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
birddata = pd.read_csv("bird_tracking.csv", index_col=0)
birddata.head()

# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby("bird_name")

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds["speed_2d"].mean()

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds["altitude"].mean()


birddata.date_time = birddata.date_time.str[:-3]
birddata["date"] = birddata.date_time.str[:10]
grouped_bydates = birddata.groupby("date")

# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])
# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday["altitude"].mean()
mean_speed_perday = grouped_birdday["speed_2d"].mean()
print(mean_speed_perday["Nico"]["2014-04-04"])

def caculateSpeed(bird_name):
    data = birddata[birddata.bird_name == bird_name]
    times = pd.to_datetime(data.date_time, format="%Y-%m-%d %H:%M:%S")
    elapsed_time = [time - times[0] for time in times]
    elapsed_days = np.array(elapsed_time) / datetime.timedelta(days= 1)
    next_days = 1
    inds = []
    daily_mean_spped = []
    for i,t in enumerate(elapsed_days):
        if t < next_days:
            inds.append(i)
        else:
            daily_mean_spped.append(np.mean(data.speed_2d[inds]))
            next_days += 1
            inds = []
    return daily_mean_spped
# eric_daily_speed  = caculateSpeed("Eric")
# sanne_daily_speed = caculateSpeed("Sanne")
# nico_daily_speed = caculateSpeed("Nico")

# plt.plot(eric_daily_speed)
# plt.xlabel("day")
# plt.ylabel("speed")
# # sanne_daily_speed.plot(label="Sanne")
# # nico_daily_speed.plot(label="Nico")
# plt.legend(loc="upper left")
# plt.show()