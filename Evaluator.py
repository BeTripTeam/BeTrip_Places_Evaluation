from models.Place import Place
from numpy import array


class Evaluator:
    def evaluate_place(self, place: Place):
        photo_score = self.evaluate_photo(place.photos)
        tips_score  = self.evaluate_tips(place.tips)
        return photo_score + tips_score

    def evaluate_photo(self, photos):
        return array([photo.mark for photo in photos]).mean()

    def evaluate_tips(self, tips):
        return array([tip.mark for tip in tips]).mean()