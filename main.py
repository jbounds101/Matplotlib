from matplotlib import pyplot as plt

# Median Developer Salaries by Age
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


plt.style.use('fivethirtyeight')
plt.plot(age_x, dev_y, 'b', linewidth=3, label='All Devs')  # k--. first color, then line style, then markers
plt.plot(age_x, py_dev_y, color='#444444', linewidth=3, label='Python Devs')  # can also do this
plt.plot(age_x, js_dev_y, color='#adad3b', linestyle='--', linewidth=3, label='JavaScript Devs')  # can also do this
plt.legend()
plt.tight_layout()
plt.grid(True)

plt.title('Median Salary (USB) by Age')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.savefig('plot.png')

plt.show()
