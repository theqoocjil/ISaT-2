from neo4j import GraphDatabase
from dotenv import load_dotenv
import os 
import requests
import json

load_dotenv()


URI = os.getenv('URI')
DATABASE = os.getenv('DATABASE')
AUTH = (DATABASE, os.getenv('PASSWORD'))
TOKEN = os.getenv('TOKEN') 


def add_friend(user_id, friend_id, friend_name, friend_surname):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query(
            "MERGE (a:Person {idf: $user_id}) "
            "MERGE (friend:Person {name: $friend_name, surname: $friend_surname, idf: $friend_id}) "
            "MERGE (a)-[:KNOWS]->(friend)",
            user_id=user_id, friend_name=friend_name, friend_surname=friend_surname, friend_id=friend_id, database_="{DATABASE}",
        )

def get_friends(user_id, n):
    if n != 2:
        url = 'https://api.vk.com/method/friends.get/?fields=nickname&'\
        'access_token={TOKEN}'\
        f'&v=5.199&user_id={user_id}'
        r = requests.get(url)
        n+=1
        response = json.loads(r.text)
        if response.get('response', None):
            for i in response['response']['items']:
                add_friend(user_id, i['id'], i['first_name'], i['last_name'])
                get_friends(i['id'], n)

def main():
    get_friends(450153997, -1)


if __name__ == "__main__":
    main()