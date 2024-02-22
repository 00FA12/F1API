import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

import fastf1
import fastf1.plotting

def getLaps(year, race, session, driver):

    session = fastf1.get_session(year, race, session)
    session.load()

    return session.laps.pick_driver(driver).pick_quicklaps().reset_index()

def format_time(x, pos=None):
    minutes = int(x // 60)
    seconds = int(x % 60)
    milliseconds = int((x * 1000) % 1000)
    return f'{minutes:02}:{seconds:02}:{milliseconds:03}'

def createPlotGraph(dataSample):
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.scatterplot(data=dataSample,
                    x="LapNumber",
                    y="LapTime",
                    ax=ax,
                    hue="Compound",
                    palette=fastf1.plotting.COMPOUND_COLORS,
                    s=80,
                    linewidth=0,
                    legend='auto')

    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time")
    ax.set_facecolor('xkcd:black')

    # The y-axis increases from bottom to top by default
    # Since we are plotting time, it makes sense to invert the axis
    ax.invert_yaxis()

    # Turn on major grid lines
    plt.grid(color='w', which='major', axis='both')
    sns.despine(left=True, bottom=True)

    # Create a formatter
    formatter = ticker.FuncFormatter(format_time)

    # Set the formatter
    ax.yaxis.set_major_formatter(formatter)   

    plt.tight_layout()
    plt.show()