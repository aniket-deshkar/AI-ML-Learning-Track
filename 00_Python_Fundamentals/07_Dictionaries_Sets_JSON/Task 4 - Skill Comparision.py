emp1 = {"python", "sql","ml"}
emp2 = {"python", "excel", "powerbi"}
common_skill = emp1 & emp2
print("Common skills: ",common_skill)
unique_skill = emp1 - emp2
print("Unique skills for emp1: ",unique_skill)
all_skills = emp1 | emp2
print("All skills: ",all_skills)