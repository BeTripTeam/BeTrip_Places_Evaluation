from Images_Beauty.ImageAnalytics import ImageAnalytics
from numpy import array


class PhotoEvaluator:
    def __init__(self):
        self.images_analyzer = ImageAnalytics()
        
    def evaluate_photos(self, photos):
        """
        Gives a mark to photo list according to
        - number of photos
        - beauty of photos
        :param photos:
        :return: mark in range [0, 1]
        """
        self.update_photos_scores(photos)
        if not photos:
            return 0
        if len(photos) <= 10:
            w = 0.5
        else:
            w = 1
        m = array([photo.mark for photo in photos]).mean() * w
        if m > 0.85: m = m + 0.2
        return m

    def update_photos_scores(self, photos):
        for photo in photos:
            if photo.mark < 0:
                photo.mark = self._beauty_score(photo)

    def _beauty_score(self, photo):
        return self.images_analyzer.beauty_score_url(photo.photo_link)


# from models.Photo import Photo
# pe = PhotoEvaluator()
# print(pe.evaluate_photos([Photo('https://travelpassionate.com/wp-content/uploads/2017/08/Kirkjufellsfoss-waterfall-Iceland-Europe.-Beauty-world.-min.jpg', 0.0)]))