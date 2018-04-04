from BeTrip_Images.ImageAnalytics import ImageAnalytics
from BeTrip_Images.image_analysis.image_helper import open_img


ia = ImageAnalytics()
im = open_img("../../instagram/1/1/1.jpg")
score = ia.get_score(im)
print(score)