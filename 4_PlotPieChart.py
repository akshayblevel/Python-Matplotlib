import matplotlib.pyplot as plt


year = [2021,2022,2023,2024,2025]
students_enrolled = [110,115,120,125,130]
myexplode = [0, 0, 0, 0, 0.2]

def show_values(pct, allvals):
    total = sum(allvals)
    value = int(round(pct * total / 100.0))
    return f"{value} students"


plt.pie( students_enrolled, labels= year, explode=myexplode, autopct=lambda pct: show_values(pct, students_enrolled))
plt.legend()
plt.show()