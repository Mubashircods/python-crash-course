from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows =[], [], []
for row in reader:
    first_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:    
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {first_date}")
    else:
        dates.append(first_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_title("Daily High and Low Temperature, 2021", fontsize=20)
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(labelsize=10)
fig.autofmt_xdate()
plt.show()


