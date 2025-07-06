import matplotlib.pyplot as plt

## Covid cases per month

month = [1, 2, 3, 4, 5]
monthly_cases = [100, 500, 1000, 2000, 5000]


plt.plot(monthly_cases, month)
plt.title("Monthly COVID-19 Cases in India (Sample Data)")
plt.xlabel("Number of Cases")
plt.ylabel("Month")
plt.show()
