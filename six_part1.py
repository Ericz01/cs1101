employees = ["John Duck", "Lisa Doe", "Spencer Johnson", "Mark Steve", "Cate Poe", 
            "Tom Lake", "David Stewart", "Ben Khan", "Stella Dynn", "Mary Atieno"]

# Split list into sublist 1 and 2
sublist1 = employees[:5]
sublist2 = employees[5:]
print("Two lists:\n", sublist1, sublist2)

# Add an employee to the sublist2.
sublist2.append("Kriti Brown")
print("Add Kriti Brown:\n", sublist2)

#Remove an employee from sublist1
removed = sublist1.pop(1)
print("Remove an employee from 1:\n", sublist1)

# Merge the lists.
sublist1.extend(sublist2)
print("Merged:\n", sublist1)

# Make a salary list and raise each salary by 4%. Print the top 3 salaries.
salaryList = [4000, 6000, 8600, 4500, 9200, 4800, 7200, 6600, 4000, 4700]
raised_salary = []
for salary in salaryList:
    salary = (0.04 * salary) + salary
    raised_salary.append(salary)
sorted_salaries = sorted(raised_salary, reverse=True)
print(f"Top 3 salaries:\n {sorted_salaries[:3]}")
