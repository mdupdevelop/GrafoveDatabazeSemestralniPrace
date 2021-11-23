# Script was successfully tested runnning localhost 4.35 neo4j instance connected to via bolt protocol

import os
import json
from neo4j import GraphDatabase
import yaml


with open(r'./conf_graph.yaml') as file:
    conf_yaml     = yaml.safe_load(file)
    conf_server   = conf_yaml['server']
    conf_username = conf_yaml['username']
    conf_password = conf_yaml['password']
    conf_dir_name = conf_yaml['dir_name']


class Neo4jDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_page_node(self, page_title, page_url):
        with self.driver.session() as session:
            session.write_transaction(self._create_page_node, page_title, page_url)

    def create_author_node(self, author):
        with self.driver.session() as session:
            session.write_transaction(self._create_author_node, author)
    
    def create_topic_node(self, topic):
        with self.driver.session() as session:
            session.write_transaction(self._create_topic_node, topic)
    
    #Relationships
    def create_article_author_relationship(self, page_url, author):
        with self.driver.session() as session:
            session.write_transaction(self._create_article_author_relationship1, page_url, author)
    
    def create_article_topic_relationship(self, page_url, topic):
        with self.driver.session() as session:
            session.write_transaction(self._create_article_topic_relationship, page_url, topic)
    
    def create_article_article2_relationship(self, page_name1, page_name2):
        with self.driver.session() as session:
            session.write_transaction(self._create_article_article2_relationship, page_name1, page_name2)
    
    # Delete
    def delete_entire_db(self):
        with self.driver.session() as session:
            session.write_transaction(self._delete_entire_db)
    
    #Static methods
    
    #Nodes
    @staticmethod
    def _create_page_node(tx, page_title, page_url):
        tx.run(f"MERGE (a: Article {{page_title: '{page_title}'}}) "
                f"SET a.page_url = '{page_url}'")
        return None
    
    @staticmethod
    def _create_author_node(tx, author):
        tx.run(f"MERGE (a: Author {{name: '{author}'}})")
        return None

    @staticmethod
    def _create_topic_node(tx, topic):
        tx.run(f"MERGE (n:Topic {{topic: '{topic}'}})")
        return None
    
    # Relationships
    @staticmethod 
    def _create_article_author_relationship1(tx, page_url, author):
        tx.run(f"MATCH (a:Article), (b:Author) WHERE a.page_url = '{page_url}' AND b.name = '{author}' AND NOT (a)-[:WRITTEN_BY]->(b) CREATE (a)-[r:WRITTEN_BY]->(b)")                      
        return None

    @staticmethod 
    def _create_article_topic_relationship(tx, page_url, topic):
        tx.run(f"MATCH (a:Article), (b:Topic) WHERE a.page_url = '{page_url}' AND b.topic = '{topic}' AND NOT (a)-[:IS_ABOUT]->(b) CREATE (a)-[r:IS_ABOUT]->(b)")                      
        return None

    @staticmethod 
    def _create_article_article2_relationship(tx, page_name1, page_name2):
        tx.run(f"MATCH (a:Article), (b:Article) WHERE a.page_title = '{page_name1}' AND b.page_title = '{page_name2}' AND NOT (a)-[:REFERENCES_TO]->(b) CREATE (a)-[r:REFERENCES_TO]->(b)")                      
        return None

    @staticmethod 
    def _delete_entire_db(tx):
        tx.run(f"MATCH (n) DETACH DELETE n")                      
        return None


def main():
    db = Neo4jDB(f"{conf_server}", f"{conf_username}", f"{conf_password}")

    for file in os.listdir(f'./{conf_dir_name}/'):
        with open(f'./{conf_dir_name}/{file}') as json_file:
            print(file)
            data = json.load(json_file)['pages']
            for i in range(len(data)):
                page_title = data[i]['page_title']
                page_url   = data[i]['page_url']
                author     = data[i]['written_by']

                db.create_page_node(data[i]['page_title'], data[i]['page_url'])
                db.create_author_node(data[i]['written_by'])
                print(page_title)
                print('URL__________' + page_url +  '_____AUTHOR_______' + author)
                db.create_article_author_relationship(page_url, author)

                for j in range(len(data[i]['topics'])):
                    topic = data[i]['topics'][j]
                    db.create_topic_node(topic)
                    db.create_article_topic_relationship(page_url, topic)



    # Create relationships between pages second round of iteration
    for file in os.listdir(f'./{conf_dir_name}/'):
        with open(f'./{conf_dir_name}/{file}') as json_file:
            data = json.load(json_file)['pages']
            for i in range(len(data)):
                page_title = data[i]['page_title']
                for j in range(len(data[i]['references_to'])):
                    db.create_article_article2_relationship(page_title, data[i]['references_to'][j]['page_name'])

    db.close() 

def clear_db():
    db = Neo4jDB(f"{conf_server}", f"{conf_username}", f"{conf_password}")
    db.delete_entire_db()
    db.close() 


if __name__ == "__main__":
    main()

