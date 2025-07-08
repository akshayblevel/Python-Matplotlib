import matplotlib.pyplot as plt


year = [2021,2022,2023,2024,2025]
students_enrolled = [110,115,120,125,130]
students_passed = [90,100,105,110,120]

#Vertical Bar
plt.bar(year, students_enrolled, color="red", width=0.5)
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Number of Students Enrolled')
plt.show()

#Horizontal Bar
plt.barh(year, students_passed, color="blue")
plt.xlabel('Number of Students')
plt.ylabel('Year')
plt.title('Number of Students Passed')
plt.show()