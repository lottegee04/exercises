# Write your code here
def process_data(string_data):
    new_dict ={}
    for i in string_data:
        list = i.split(",")
        new_dict[list[0]] = {"age": int(list[1]), "courses": list[2:]}
    return new_dict

def average_age(data):
    sum = 0
    for i in data.values():
        sum+=i["age"]
    return sum/len(data)

def courses(data):
    setje = set()
    for i in data.values():
        for j in i["courses"]:
            setje.add(j)
    return setje

def most_common_courses(data):
    setje =set()
    counter = 0
    count = {}
    for i in data.values():
        for j in i["courses"]:
            if j not in count:
                count[j] =0
            count[j] = count[j] + 1
    setje.add(list(count.keys())[0])
    counter  = list(count.values())[0]
    for course , count in list(count.items())[1:]:
        if count > counter:
            setje = set()
            setje.add(course)
            counter = count
        if count == counter:
            setje.add(course)
    return setje
data = {'Alan Smithee': {'age': 29, 'courses': ['Math', 'Latin', 'Economics']}, 'Jane Doe': {'age': 18, 'courses': ['Math', 'German', 'Physics', 'Biology']}, 'John Smith': {'age': 20, 'courses': ['Math', 'Latin', 'Physics']}}
most_common_courses(data)
