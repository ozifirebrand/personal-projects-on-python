company_data = [["Name", "Age", "Department"], ["John Mckee", 38, "Sales"],
                ["Lisa Crawford", 29, "Marketing"], ["Sujan Patel", 33, "HR"]]
for item in range(len(company_data)):
    for list_array in range(len(company_data[item])):
        print(company_data[item][list_array], end=' ')
    print()