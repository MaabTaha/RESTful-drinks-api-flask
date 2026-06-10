# run "pip install requests"
# create venv
# run "pip install flask"
# run "pip install flask-sqlalchemy" # for database
# print("hhh")
import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
)

# print(response) # output: <Response [200]>
# print(response.json()) # output: {'items': [...], 'has_more': True, 'quota_max': 10000, 'quota_remaining': 9999}
# print(response.json()['items']) 

# for question in response.json()['items']:
#     print(question['title'])
#     print(question['link'])
#     print()


for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])

    else:
        print("This question has answers, skipping...")
    print()