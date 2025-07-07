import matplotlib.pyplot as plt


year = [2021,2022,2023,2024,2025]
students_enrolled = [110,115,120,125,130]
students_passed = [90,100,105,110,120]

plt.plot(year, students_enrolled, marker='o')
plt.plot(year, students_passed, marker='x')

plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Number of Students Enrolled & Passed Per Year')

plt.legend(['Students Enrolled', 'Students Passed'])
plt.grid(True)
plt.show()