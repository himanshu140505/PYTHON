import requests
from systemcommands import owner, clearscreen

def quiz_icon():
    print("================================================")
    print("||                  QUIZ APP                  ||")
    owner()
    print("================================================")

def quiz_app():
    quiz_icon()
    category = ['artliterature', 'language', 'sciencenature', 'general', 'fooddrink', 'peopleplaces', 'geography', 'historyholidays', 'entertainment', 'toysgames', 'music', 'mathematics', 'religionmythology', 'sportsleisure']

    print("================================================")
    print('''|| 1.artliterature   2.language    3.general  ||  
|| 4.sciencenature   5.fooddrink   6.geography||
|| 7.peopleplaces    8.toysgames   9.music    ||
||10.entertainment  11.historyholidays        ||
||12.mathematics    13.religionmythology      ||
||14.sportsleisure                            ||''')
    print("================================================")
    user_choice_category = category[(int(input("Enter the category number: ")))-1]
    print(user_choice_category)
    api_url = f'https://api.api-ninjas.com/v1/trivia?category={user_choice_category}'
    response = requests.get(api_url, headers={'X-Api-Key': 'EnKiBn6C4joXGXz59AMy7Q==nPXSmx6dtLvDmlZU'})
    print(response.json())
    print(response.status_code)
    print(response.text)
    if response.status_code == requests.codes.ok:
        trivia_data = response.json()
        
        for item in trivia_data:
            print(f"Question: {item['question']}")
            print(f"Answer: {item['answer']}\n")
    else:
        print("Error:", response.status_code, response.text)

quiz_app()