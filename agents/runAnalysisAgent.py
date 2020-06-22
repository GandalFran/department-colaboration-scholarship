import os
import json
import logging
from agents.analysis_agent import AnalysisAgent

if __name__ == '__main__':
    input_topic = os.environ['ANALYSIS_INPUT_TOPIC']
    output_topic = os.environ['ANALYSIS_OUTPUT_TOPIC']
    producer_settings = os.environ['KAFKA_PRODUCER_SETTINGS']
    consumer_settings = os.environ['KAFKA_CONSUMER_SETTINGS']
    producer_settings = json.loads(producer_settings)
    consumer_settings = json.loads(consumer_settings)

    logging.basicConfig(level=logging.DEBUG)

    agent = AnalysisAgent(producer_settings, consumer_settings, input_topic, output_topic)
    agent.behaviour()
