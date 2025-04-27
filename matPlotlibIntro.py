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
print(result)

varList = []
labelList = []
for row in range(len(result)):
    varList.append(result[row][0])
    labelList.append(result[row][1])

y = np.array(varList)
mylabels = labelList

plt.gca().axis("equal")
plt.pie(y)
plt.legend(title= cursor.description[0][0], labels = mylabels, bbox_to_anchor=(1,0.5), loc='center right', fontsize=10,
           bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=0.0, bottom=0.1, right=0.8)
plt.show()

conn.close()
