import pandas as pd
import matplotlib.pyplot as plt  

CSV_FILE_LOCATION = ""
MONTH_COLOUM_NAME = ""
PRODUCT_COLOUM_NAME = ""


df = pd.read_csv(CSV_FILE_LOCATION)
monthList  = df [MONTH_COLOUM_NAME].tolist()
productSalesData = df [PRODUCT_COLOUM_NAME].tolist()
plt.scatter(monthList, productSalesData, label = 'Product Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Product Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()
