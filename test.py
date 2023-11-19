import json
from pprint import pprint
a = {'list_applications': [
    {'user_id': 1172020269, 't_name': 'Денис', 't_surname': 'Дорофеев', 'name': 'Денис', 'surname': 'Дорофеев', 'status': 'Заявка', 'role': 'awdawd'}

], 
     'list_participants': [
         
     ], 
     'list_administrators': [
         
     ], 
     'list_creators': [
         
     ]}

with open(file="list.json", mode="w") as f:
    json.dump(a, f, ensure_ascii=False, indent=2)


fields = ["user_id", "t_name", "t_surname", "name", "surname", "status", "role"]
{
  "list_applications": [],
  "list_participants": [],
  "list_administrators": [],
  "list_creators": []
}

pprint(a, sort_dicts=False)