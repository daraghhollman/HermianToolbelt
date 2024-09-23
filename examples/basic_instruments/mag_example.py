import datetime as dt

import matplotlib.pyplot as plt

from hermpy import mag, plotting_tools

root_dir = "/home/daraghhollman/Main/data/mercury/messenger/mag/avg_1_second/"

# Loading data, downloaded from PDS
# Should think about using a glob tool to select data
# between certain doy.
# i.e. "****/*****/MAGMSOSCIAVG*****_01_V08.TAB"
data = mag.Load_Messenger(
    [
        root_dir + "2012/01_JAN/MAGMSOSCIAVG12001_01_V08.TAB",
        root_dir + "2012/01_JAN/MAGMSOSCIAVG12002_01_V08.TAB",
    ]
)

start = dt.datetime(year=2012, month=1, day=1, hour=10)
end = dt.datetime(year=2012, month=1, day=2, hour=10)

# Isolating only a particular portion of the files
data = mag.StripData(data, start, end)

# Converting to MSM
data = mag.MSO_TO_MSM(data)

# Accounting for solar wind aberration angle
#data = mag.AdjustForAberration(data)

"""
This data object is a Pandas DataFrame, and has the following columns:

date:  a datetime object of the time of the measurement
frame: the current coordinate system
eph_x: the x coordinate of the spacecraft (km)
eph_y: the y coordinate of the spacecraft (km)
eph_z: the z coordinate of the spacecraft (km)
range: the distance of the spacecraft from Mercury (km)
mag_x: the magnetic field strength in x (nt)
mag_y: the magnetic field strength in y (nt)
mag_z: the magnetic field strength in z (nt)
mag_total: the total magnetic field strength (nt)
"""

# This data can then be plotted using external libraries
fig, ax = plt.subplots()

ax.plot(data["date"], data["mag_total"])

ax.set_yscale("log")

# Plotting ephemeris information
# We need a metakernel to retrieve ephemeris information
metakernel = "/home/daraghhollman/Main/SPICE/messenger/metakernel_messenger.txt"
plotting_tools.Add_Tick_Ephemeris(ax, metakernel)

plt.show()
