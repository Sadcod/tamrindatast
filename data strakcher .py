#bakhshe aval project 
def bubble_sort(names):
    for i in range(len(names)-1):
        min_index = i
        for j in range(i+1, len(names)):
            if names[j]['Last Name'] < names[min_index]['Last Name']:
                min_index = j
            elif names[j]['Last Name'] == names[min_index]['Last Name']:
                if  names[j]['First Name'] < names[min_index]['First Name']:
                    min_index = j
        names[i], names[min_index] = names[min_index], names[i]
    return names

# meghdar
names = (
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}

)
sort_names = bubble_sort(names)
print(sort_names)
#bakhshe dovome 
import matplotlib.pyplot as plt
import random
import time

def bubble_sort(mardom):
    n = len(mardom)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if mardom[j]["First Name"] < mardom[min_index]["First Name"]:
                min_index = j
        mardom[i], mardom[min_index] = mardom[min_index], mardom[i]


def generate_random_data(n):
    data = []
    for _ in range(n):
        first_name = ''.join(random.choices('#', k=2))
        last_name = ''.join(random.choices("#", k=2))
        data.append({ "First Name": first_name, "Last Name": last_name})
    return data

def measure_sorting_time(data):
    start_time = time.time()
    bubble_sort(data)
    end_time = time.time()
    return end_time - start_time


data_sizes = list(range(10, 1001,))
sorting_times = []

for size in data_sizes:
    data = generate_random_data(size)
    sorting_time = measure_sorting_time(data)
    sorting_times.append(sorting_time)


plt.plot(data_sizes, sorting_times)
plt.xlabel('Meghdar dada vorod shodeh ')
plt.ylabel('time mohasebe dagigh')
plt.title( " tedad data vorodi modat  mohasebe \\ time   doktor:Eskandari")
plt.show()
