import seaborn as sns
from matplotlib import pyplot as plt

import fastf1
import fastf1.plotting

def getLaps(year, race, session, driver):

    session = fastf1.get_session(year, race, session)
    session.load()

    return session.laps.pick_driver(driver)

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

    # The y-axis increases from bottom to top by default
    # Since we are plotting time, it makes sense to invert the axis
    ax.invert_yaxis()
    plt.suptitle("Alonso Laptimes in the 2024 Bahrain Testing S1x1")

    # Turn on major grid lines
    plt.grid(color='w', which='major', axis='both')
    sns.despine(left=True, bottom=True)

    plt.tight_layout()
    plt.show()