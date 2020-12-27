import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

count = []
dice_result = []

for i in range(0, 10000):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_result.append(dice_1 + dice_2)
    count.append(i)

mean = sum(dice_result)/len(dice_result)
print(mean)

median = statistics.median(dice_result)
print(median)

mode = statistics.mode(dice_result)
print(mode)

std_deviation = statistics.stdev(dice_result)
print(std_deviation)

fig = ff.create_distplot([dice_result], ["Dice Results"])
# fig = px.bar(x=dice_result, y=count, title="Dice Results")
fig.show()