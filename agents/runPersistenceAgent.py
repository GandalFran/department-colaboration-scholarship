import os
import json
import logging
from agents.scraping_agent import PersistenceAgent

if __name__ == '__main__':
    input_topic = os.environ['PERSISTENCE_INPUT_TOPIC']
    producer_settings = os.environ['KAFKA_PRODUCER_SETTINGS']
    consumer_settings = os.environ['KAFKA_CONSUMER_SETTINGS']
    producer_settings = json.loads(producer_settings)
    consumer_settings = json.loads(consumer_settings)

    logging.basicConfig(level=logging.DEBUG)

    agent = PersistenceAgent(producer_settings, consumer_settings, input_topic, 'foo')
    agent.behaviour()
