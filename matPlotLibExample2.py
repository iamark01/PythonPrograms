import matplotlib.pyplot as plt
import numpy as np
from mysql.connector import (connection)

# establishing the connection
conn = connection.MySQLConnection(user='root', password='@taurKhan1', host='127.0.0.1')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute("USE mydatabase")
sql = '''SELECT INCOME, CONCAT(FIRST_NAME, ' ', LAST_NAME) AS EMPLOYEE FROM EMPLOYEE'''
cursor.execute(sql)
result = cursor.fetchall()
# print(result)

varList = []
labelList = []
for row in range(len(result)):
    varList.append(result[row][0])
    labelList.append(result[row][1])

y = np.array(varList)
mylabels = labelList

'''
plt.gca().axis("equal")
plt.pie(y)
plt.legend(title= cursor.description[0][0], labels = mylabels, bbox_to_anchor=(1,0.5), loc='center right', fontsize=10,
           bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=0.0, bottom=0.1, right=0.8)
'''


def func(pct, allvals):
    int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%"


# Create the pie chart
fig, ax = plt.subplots()
fig.subplots_adjust(left=0.0, bottom=0.1, right=0.8)
patches, texts, autotexts = ax.pie(varList, autopct=lambda pct: func(pct, varList), startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax.legend(patches, mylabels, title="Income Salary", loc='upper right', bbox_to_anchor=(1, 1), fontsize=10,
          bbox_transform=plt.gcf().transFigure)
# Create annotation object
bbox_props = dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8)
arrowprops = dict(arrowstyle="-|>", connectionstyle="angle,angleA=0,angleB=90,rad=0")
annotation = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                         bbox=bbox_props, arrowprops=arrowprops, visible=False)


# Hover function
def hover(event):
    if event.inaxes == ax:
        for i, patch in enumerate(patches):
            if patch.contains_point((event.x, event.y)):
                x, y = patch.center
                annotation.xy = (x, y)
                label = mylabels[i]
                value = varList[i]
                annotation.set_text(f"{label}: {value}")
                annotation.set_visible(True)
        fig.canvas.draw_idle()


# Connect the event
fig.canvas.mpl_connect("motion_notify_event", hover)

# Show the plot
plt.show()

conn.close()
