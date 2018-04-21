from Text_Sentiment.SentimentAnalyzer import SentimentAnalyzer
from numpy import array


class TipEvaluator:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        
    def evaluate_tips(self, tips):
        """
        Gives a mark to tips list according to
        - number of tips
        - beauty of tips
        :param tips: list of strings
        :return: mark in range [0, 1]
        """
        self.update_texts_scores(tips)
        if not tips:
            return 0
        if len(tips) <= 3:
            w = 0.5
        else:
            w = 1
        return (array([tip.mark for tip in tips]).mean()/2 + 0.5) * w

    def update_texts_scores(self, tips):
        for tip in tips:
            if tip.mark < 0:
                ts = self._tags_sentiment_score(tip)
                if ts:
                    tip.mark = (self._text_sentiment_score(tip) + ts)/2
                else:
                    tip.mark = self._text_sentiment_score(tip)
                
    def _text_sentiment_score(self, tip):
        return self.sentiment_analyzer.get_text_sentiment(tip.text)

    def _tags_sentiment_score(self, tip):
        if tip.tags:
            return array(self.sentiment_analyzer.get_tags_cluster_sentiment(tip.tags)).mean()
        else:
            return 0


# from models.Tip import Tip
# te = TipEvaluator()
# print(te.evaluate_tips([Tip('Wonderful place! I want to live there', 0.0, [])]))