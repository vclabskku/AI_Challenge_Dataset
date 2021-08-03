

import json
answer = {}
for i in range(17):
  try:
    with open('answer'+str(i)+'.json',encoding='UTF-8-sig') as json_file:
        answer.update(json.load(json_file))
  except:
      pass

with open('answer_final.json', 'w', encoding='UTF-8-sig') as file:
  file.write(json.dumps(answer, ensure_ascii=False,indent=4))
