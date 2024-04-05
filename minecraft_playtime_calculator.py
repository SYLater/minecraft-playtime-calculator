import os

# Prompt the user to enter the age of their Minecraft world in days
days = int(input("How old is your Minecraft world?   "))
print(days, "days, wow!")

# Calculate the total minutes, hours, days, and weeks of playtime
minutes = (days * 20)
hours = (minutes / 60.000)
days = (hours / 24)
weeks = (days / 7)

# Print the playtime in various time units
played = "You've played"
print(played, minutes, "minutes of Minecraft")
print(played, "%.2f" % hours, "hours of Minecraft")
print(played, "%.2f" % days, "days of Minecraft")
print(played, "%.2f" % weeks, "weeks of Minecraft")

# Pause the program to allow the user to view the output
os.system("pause")