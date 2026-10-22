learner = {
    "name": "小明",
    "hours_per_week": 8,
    "goal": "學會 Python",
    "courses": ["Python", "AI agent"],
    "newcourses": [["LLM, 4"], ["DB", 3]]
    
}
print(learner["name"])
print(learner["courses"])
print(learner["courses"][0])
print(learner["courses"][1])
print(learner["newcourses"][0][0])
print(learner["newcourses"][0][1])