import os
import json
import logging
from agents.persistence_agent import PersistenceAgent

if __name__ == '__main__':
    input_topic = os.environ['PERSISTENCE_INPUT_TOPIC']
    consumer_settings = os.environ['KAFKA_CONSUMER_SETTINGS']
    consumer_settings = json.loads(consumer_settings)

    logging.basicConfig(level=logging.DEBUG)

    agent = PersistenceAgent(consumer_settings, consumer_settings, input_topic, 'foo')
    agent.behaviour()
