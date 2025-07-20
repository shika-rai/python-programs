from tabulate import tabulate
headers=["Name","Age","Department"]
data=[
    ["Ravi",25,"HR"],
    ["Anjali",30,"Finance"],
    ["Mohan",28,"IT"],
    ["Sneha",24,"Marketing"],
    ["Arun",32,"logistics"]
    
]
print(tabulate(data,headers=headers,tablefmt="fancy_grid"))

print("*" * 30)
for row in data:
    print(f"{row[0]:<12}{row[1]:<5}{row[2]:<15}")
    print("-" * 30)