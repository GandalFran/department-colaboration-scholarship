import os
import json
import logging
from agents.download_agent import DownloadAgent

if __name__ == '__main__':
    input_topic = os.environ['DOWNLOAD_INPUT_TOPIC']
    output_topic = os.environ['DOWNLOAD_OUTPUT_TOPIC']
    producer_settings = os.environ['KAFKA_PRODUCER_SETTINGS']
    consumer_settings = os.environ['KAFKA_CONSUMER_SETTINGS']
    producer_settings = json.loads(producer_settings)
    consumer_settings = json.loads(consumer_settings)

    logging.basicConfig(level=logging.DEBUG)

    agent = DownloadAgent(producer_settings, consumer_settings, input_topic, output_topic)
    agent.behaviour()
