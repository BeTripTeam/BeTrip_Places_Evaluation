from evluation.PhotoEvaluation import PhotoEvaluator
from evluation.TipEvaluator import TipEvaluator
from models.Place import Place


class Evaluator:
    def __init__(self):
        self.photo_eval = PhotoEvaluator()
        self.tip_eval = TipEvaluator()
        
    def evaluate_place(self, place: Place):
        photo_score = self.photo_eval.evaluate_photos(place.photos)
        tips_score  = self.tip_eval.evaluate_tips(place.tips)
        return ((photo_score + tips_score) * 0.6 + 0.4) * place.rating
