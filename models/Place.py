import numpy as np


class Place:
    
    def __init__(self, central_point, points):
        # Social
        self.name   = ''
        self.tips   = []
        self.photos = []
        # Category
        self._category_name = ""
        self._category = -2
        # Stat
        self._tags_relevance_stat  = []
        self._tags_sentiment_stat  = []
        self._texts_relevance_stat = []
        self._texts_sentiment_stat = []
        # Marks
        self.mark = 0
        self.users_marks = []
        # Geo
        self.central_point = central_point
        self.geo_points = points
    
    def set_place_info(self, name, tips, photos):
        self.name = name
        self.tips = tips
        self.photos = photos
    
    # def set_tags_relevance_stat(self, relevance_mask, relevance_stat):
    #     self._tags_relevance_stat = relevance_stat
    #     self._delete_points(relevance_mask)
    #
    # def set_tags_sentiment_stat(self, sentiment_stat):
    #     self._tags_sentiment_stat = sentiment_stat
    #
    # def set_texts_relevance_stat(self, relevance_mask, relevance_stat):
    #     self._texts_relevance_stat = relevance_stat
    #     self._delete_points(relevance_mask)
    #
    # def set_texts_sentiment_stat(self, sentiment_stat):
    #     self._texts_sentiment_stat = sentiment_stat
    
    def _delete_points(self, mask):
        self._texts = self._delete(self._texts, mask)
        self._tags = self._delete(self._tags, mask)
        self._geo_points = self._delete(self._geo_points, mask)
        
        if len(self._tags_sentiment_stat) > 0:
            self._tags_sentiment_stat = self._delete(self._tags_sentiment_stat, mask)
        self._tags_relevance_stat = self._delete(self._tags_relevance_stat, mask)
        if len(self._texts_sentiment_stat) > 0:
            self._texts_sentiment_stat = self._delete(self._texts_sentiment_stat, mask)
        if len(self._texts_relevance_stat) > 0:
            self._texts_relevance_stat = self._delete(self._texts_relevance_stat, mask)
    
    def _delete(self, arr, mask):
        return np.array(arr)[mask]
