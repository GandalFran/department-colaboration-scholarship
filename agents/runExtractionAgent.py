import os
import json
import logging
from agents.extraction_agent import ExtractionAgent

if __name__ == '__main__':
    api_key = os.environ['EXTRACTION_API_KEY']
    input_topic = os.environ['EXTRACTION_INPUT_TOPIC']
    output_topic = os.environ['EXTRACTION_OUTPUT_TOPIC']
    producer_settings = os.environ['KAFKA_PRODUCER_SETTINGS']
    consumer_settings = os.environ['KAFKA_CONSUMER_SETTINGS']
    producer_settings = json.loads(producer_settings)
    consumer_settings = json.loads(consumer_settings)

    logging.basicConfig(level=logging.DEBUG)

    agent = ExtractionAgent(api_key, producer_settings, consumer_settings, input_topic, output_topic)
    agent.behaviour()
