%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

city_data = pd.read_csv(city_data_to_load)
ride_data = pd.read_csv(ride_data_to_load)



# Read the City and Ride Data

# Combine the data into a single dataset

# Display the data table for preview


city_data.head()

ride_data.head()

merge_data = pd.merge(city_data, ride_data, on="city")
merge_data

group_data= merge_data.groupby(["type","city"])
group_data
group_data.count()


## Bubble Plot of Ride Sharing Data

# Obtain the x and y coordinates for each of the three city types

# Build the scatter plots for each city types

# Incorporate the other graph properties

# Create a legend

# Incorporate a text label regarding circle size

# Save Figure


total_number_rides = group_data["ride_id"].count()
total_number_rides

total_fares = group_data["fare"].sum()
total_fares

average_fare = total_fares / total_number_rides
average_fare

drop_data = merge_data.drop_duplicates(['city'])
drop_data

drop_data_group = drop_data.groupby(["type","city"])
drop_data_group

driver_counts = drop_data_group["driver_count"].sum()
driver_counts

plt.scatter(total_number_rides['Rural'], average_fare['Rural'], marker="o", facecolors="gold", edgecolors="black", linewidths=0, s=driver_counts['Rural'], label="City Types"+ "\n" +"  Rural", alpha=0.75)
plt.scatter(total_number_rides['Suburban'], average_fare['Suburban'], marker="o", facecolors="blue", edgecolors="black", linewidths=0, s=driver_counts['Suburban'], label="  Suburban", alpha=0.75)
plt.scatter(total_number_rides['Urban'], average_fare['Urban'], marker="o", facecolors="coral", edgecolors="black", linewidths=0, s=driver_counts['Urban'], label="  Urban", alpha=0.75)
plt.grid()
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare(S)")
plt.title("Pyber Ride Sharing Data (2016)")
plt.legend(loc="upper right")
plt.savefig("../Images/scatterpicture.png")
plt.show()




## Total Fares by City Type

# Calculate Type Percents

# Build Pie Chart

# Save Figure


citytype_group = merge_data.groupby("type")
citytype_group

total_fares_citytype = citytype_group["fare"].sum()
total_fares_citytype

total_fares = total_fares_citytype.plot(kind='pie', colors = ['gold', 'blue', 'coral'], autopct="%1.1f%%", explode = (0, 0, 0.1, ), shadow=True, startangle=100)

plt.axis("equal")
plt.title("Total Fares by City Type")
plt.savefig("../Images/piechart.png")
plt.show()
plt.tight_layout()

## Total Rides by City Type

# Calculate Ride Percents

# Build Pie Chart

# Save Figure


total_rides_citytype = citytype_group["ride_id"].count()
total_rides_citytype

total_rides = total_rides_citytype.plot(kind='pie', colors = ['gold', 'blue', 'coral'], autopct="%1.1f%%", explode = (0, 0, 0.1, ), shadow=True, startangle=110)

plt.axis("equal")
plt.title("Total Rides by City Type")
plt.savefig("../Images/totalrides.png")
plt.show()
plt.tight_layout()

## Total Drivers by City Type

# Calculate Driver Percents

# Build Pie Charts

# Save Figure


drop_data_citytype_group = drop_data.groupby("type")
drop_data_citytype_group

total_drivers_citytype = drop_data_citytype_group["driver_count"].sum()
total_drivers_citytype

total_drivers = total_drivers_citytype.plot(kind='pie', colors = ['gold', 'blue', 'coral'], autopct="%1.1f%%", explode = (0, 0, 0.1, ), shadow=True, startangle=140)

plt.axis("equal")
plt.title("Total Drivers by City Type")
plt.savefig("../Images/totaldrivers.png")
plt.show()
plt.tight_layout()