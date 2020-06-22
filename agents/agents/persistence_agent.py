import json
from typing import List
from agents.agent import Agent
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class PersistenceAgent(Agent):

    def __init__(self, producer_settings, consumer_settings, input_topic, output_topic):
        super().__init__(producer_settings, consumer_settings, input_topic, output_topic)
        self._analyzer = SentimentIntensityAnalyzer()

    def task(self, message: str) -> List[str]:
        article = json.loads(message)
        self._mongo(article)
        self._neo4j(article)
        return ['']

    def _mongo(self, article: dict):
    	uri = os.environ['MONGO']
    	db = os.environ['MONGODB']
    	collection = os.environ['MONGOCOLLECTION']
    	mongo = MongoClient(uri)[db][collection]
    	mongo.update(
            {
                "$push": {
                    f"news": {
                        "url": article['url'],
                        "title": article['title'],
                        "author": article['author'],
                        "sentiment": article['sentiment']
                    }
                }
            },
            upsert=True
        )

   	def _neo4j(self, article: dict):
    	uri = os.environ['NEO4J']
    	u = os.environ['NEO4JUSER']
    	p = os.environ['NEO4JPASSWD']
   		# generate nodes
   		news =  Node('NEWS', url=article['url'])
   		orgs = [Node('ENTITY', name=e, type='org') for e in article['ner']['org']]
   		people = [Node('ENTITY', name=e, type='people') for e in article['ner']['people']]
   		# generate relationships
   		relations_orgs = [Relationship(n, 'CONTAINED_IN', news) for n in orgs]
   		relations_people = [Relationship(n, 'CONTAINED_IN', news) for n in people]
   		# join
   		relations = relations_orgs + relations_people
   		# store
   		neo4j = Graph(uri, username=u, password=p)
   		neo4j.merge(news, 'NEWS', 'url')
   		for n in orgs:
			neo4j.merge(n, 'ENTITY', 'name')
   		for n in people:
			neo4j.merge(n, 'ENTITY', 'name')
   		for r in relations:
            neo4j.create(relationship)