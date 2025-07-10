import matplotlib.pyplot as plt


year = [2021,2022,2023,2024,2025]
students_enrolled = [110,115,120,125,130]
students_passed = [90,100,105,110,120]

colors = [0, 10, 20, 30, 40]

plt.scatter(year,students_enrolled,c=colors, cmap='viridis')
plt.scatter(year,students_passed)
plt.colorbar()
plt.show()