import pandas as pd 
import json
import sys
file_name = sys.argv[1]
xlsx = pd.read_excel(file_name + '.xlsx')
problem = {}
for i in range(len(xlsx['problem'])):
  problem[str(i)] = {'question':xlsx['problem'][i]}

with open('problem'+file_name + '.json', 'w', encoding='UTF-8-sig') as file:
  file.write(json.dumps(problem, ensure_ascii=False,indent=4))
