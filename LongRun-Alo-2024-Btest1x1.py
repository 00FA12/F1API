import seaborn as sns
from matplotlib import pyplot as plt

import fastf1
import fastf1.plotting


# The misc_mpl_mods option enables minor grid lines which clutter the plot
fastf1.plotting.setup_mpl(misc_mpl_mods=False)

session = fastf1.get_testing_session(2024, 1, 1)
session.load

alo_laps = session.laps.pick_driver("ALO").pick_accurate().pick_wo_box().reset_index()

fig, ax = plt.subplots(figsize=(8, 8))

sns.scatterplot(data=alo_laps,
                x="LapNumber",
                y="LapTime",
                ax=ax,
                hue="Compound",
                palette=fastf1.plotting.COMPOUND_COLORS,
                s=80,
                linewidth=0,
                legend='auto')
