

import json
problem = {}
for i in range(17):
  try:
    with open('problem'+str(i)+'.json',encoding='UTF-8-sig') as json_file:
        problem.update(json.load(json_file))
  except:
      pass
    
with open('problem_final.json', 'w', encoding='UTF-8-sig') as file:
  file.write(json.dumps(problem, ensure_ascii=False,indent=4))
