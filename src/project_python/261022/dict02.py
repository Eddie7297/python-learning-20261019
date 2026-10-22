learner = [
{    "name": "小明",
    "hours_per_week": 8,
    "goal": "學會 Python",
    "courses": ["Python", "AI agent"],
    "newcourses": [["LLM, 4"], ["DB", 3]]
    
},
{    "name": "關你屁事",
    "hours_per_week": 1,
    "goal": "學會 Python",
    "courses": ["Python", "AI agent"],
    "newcourses": [["LLM, 4"], ["DB", 3]]
    
}
]
print(learner[0]["name"])
print(learner[0]["courses"])
print(learner[0]["courses"][0])
print(learner[0]["courses"][1])
print(learner[0]["newcourses"][0][0])
print(learner[0]["newcourses"][0][1])

