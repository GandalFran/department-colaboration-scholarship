import json
from typing import List
from agents.agent import Agent
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class AnalysisAgent(Agent):

    def __init__(self, producer_settings, consumer_settings, input_topic, output_topic):
        super().__init__(producer_settings, consumer_settings, input_topic, output_topic)
        self._analyzer = SentimentIntensityAnalyzer()

    def task(self, message: str) -> List[str]:
        article = json.loads(message)
        # sentiment
        article['sentiment'] = self._analyzer.polarity_scores(article['content'])
        # ner
        article['ner'] = self._ner(article['content'])
        response = json.dumps(article)
        return [response]

    def _ner(article: str):
    	clasified = {
    		'org': []
    		'people': []
    	}
       	ner = spacy.load("en_core_web_sm")
        result = ner(data.content)
        for r in result:
            if r.label_ == 'ORG':
                clasified['org'].append(r.text)
            elif r.label_ == 'PERSON':
                clasified['people'].append(r.text)

        clasified['org'] = list(set(clasified['org']))
        clasified['people'] = list(set(clasified['people']))

        return clasified