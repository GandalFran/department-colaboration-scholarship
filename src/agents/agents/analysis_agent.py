import json
from typing import List
from agents.agent import Agent
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class AnalysisAgent(Agent):

    def __init__(self, producer_settings, consumer_settings, input_topic, output_topic):
        super().__init__(producer_settings, consumer_settings, input_topic, output_topic)
        self._analyzer = SentimentIntensityAnalyzer()

    def task(self, message: str) -> List[str]:
        article = json.loads(message)
        # sentiment
        article['sentiment'] = self._analyzer.polarity_scores(article['text'])
        # ner
        article['ner'] = self._ner(article['text'])
        response = json.dumps(article)
        return [response]

    def _ner(self, article: str):
        clasified = {
            'org': [],
            'people': []
        }
        ner = None
        try:
           	ner = spacy.load("en_core_web_sm")
        except:
            os.system('python3 -m spacy download en_core_web_sm')
            ner = spacy.load("en_core_web_sm")

        result = ner(article)
        for r in result.ents:
            if r.label_ == 'ORG':
                clasified['org'].append(r.text)
            elif r.label_ == 'PERSON':
                clasified['people'].append(r.text)

        clasified['org'] = list(set(clasified['org']))
        clasified['people'] = list(set(clasified['people']))

        return clasified