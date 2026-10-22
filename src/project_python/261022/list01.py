#串列初始化
course_names = [
    "Python",
    "FastAPI",
    "MySQL",
    1
]
#串列可以混和不同型態使用
tmp = []

print(course_names[0])
print(course_names[3])
for course_name in course_names:
    print(course_name)

mystr = "I Love Python"
print(mystr[0])


for course_name in course_names:
    print(course_name)

courses = [ 
    ["Pyhon", 4], 
    ["Java", 6], 
    ["LLM, 4"], 
    ["DB", 3]
]
print(courses[0])
print(courses[0][0])
print(courses[0][1])

newcourse = "AI Security"
newcourses = ["PA", "Fuck"]
courses.append(newcourse)
print(courses)
courses.extend(newcourses)
courses.extend(courses)
print(courses)
print(len(courses))