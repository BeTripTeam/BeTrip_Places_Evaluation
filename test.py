import foursquare

from Evaluator import Evaluator
from Images_Beauty.ImageAnalytics import ImageAnalytics
from models.Photo import Photo
from models.Place import Place
from models.Tip import Tip

client_id = 'TW0KUEAIOA00ZSGKD2O2TVLIWQXWHJY1DPLI5ZFUGVPN1AKR'
client_secret = '2F2Z40MSGXJDKX0PIDLLU12UDZJ4A1TZWMYICHFUVYQWLD3E'


class Point:
    """ Geo Point
    """
    
    def __init__(self, latitude: float, longitude: float):
        """
        Init Point with lat:float and long:float
        """
        self.latitude = latitude
        self.longitude = longitude


class FProvider:
    def __init__(self):
        self.client = foursquare.Foursquare(client_id, client_secret)
    
    def get_venues_near(self, point: Point, radius: int, n=5):
        poi_type = ['arts', 'outdoors', 'sights']
        limit = 50  # Foursquare limit
        if limit > n: limit = n
        params = {
            'intent': 'browse',
            'll': str(point.latitude) + ',' + str(point.longitude),
            'radius': radius,
            'section': poi_type[0],
            'limit': limit,
            'offset': 0
        }
        
        places = []
        for params['section'] in poi_type:
            try:
                res = self.client.venues.explore(params)
                num_res = res['totalResults']
                if num_res > n: num_res = n
                places.extend(res['groups'][0]['items'])
                
                for params['offset'] in range(limit, num_res, limit):
                    places.extend(self.client.venues.explore(params)['groups'][0]['items'])
            except foursquare.FoursquareException as e:
                pass
        res = []
        for place in places[:2]:
            p = Place(Point(0, 0), [])
            tips = self.get_tips_for_vid(place['venue']['id'])[:5]
            photos = self.get_photos_for_vid(place['venue']['id'])[:15]
            p.set_place_info(place['venue']['name'], place['venue']['rating'], tips, photos)
            res.append(p)
        return res
    
    def get_tips_for_vid(self, vid):
        tip_params = {
            "sort": 'recent',
            'limit': 500,
            'offset': 0
        }
        res = self.client.venues.tips(vid, tip_params).get('tips')
        tips = res.get('items')
        count = res.get('count')
        offset = 0
        while len(tips) < count:
            offset += len(res.get('items'))
            tip_params['offset'] = offset
            res = self.client.venues.tips(vid, tip_params).get('tips')
            tips.extend(res.get('items'))
        return [Tip(tip.get('text'), tip.get('createdAt')) for tip in tips]
    
    def get_photos_for_vid(self, vid):
        params = {
            "group": 'venue',
            'limit': 200,
            'offset': 0
        }
        res = self.client.venues.photos(vid, params).get('photos')
        tips = res.get('items')
        count = res.get('count')
        offset = 0
        while len(tips) < count:
            offset += len(res.get('items'))
            params['offset'] = offset
            res = self.client.venues.photos(vid, params).get('photos')
            tips.extend(res.get('items'))
        return [Photo(self.make_link(tip['prefix'], tip['suffix']), tip.get('createdAt')) for tip in tips]
    
    def make_link(self, prefix, suffix):
        """
        Input:
        'prefix': 'https://igx.4sqi.net/img/user/',
        'suffix': '/13893908-H3NB1YDQ4ZKX3CGI.jpg',
        to link:
        'https://igx.4sqi.net/img/user/13893908-H3NB1YDQ4ZKX3CGI.jpg'
        :param param:
        :return: link to a photo
        """
        return prefix + '500x500' + suffix


fp = FProvider()
places = fp.get_venues_near(Point(59.9538695, 30.2659853), 20000)
e = Evaluator()
marks = [e.evaluate_place(p) for p in places[:5]]
for m, p in zip(marks, places):
    print(p)
    print(m)
    print()

# ia = ImageAnalytics()
# i = ia._load_photo("https://igx.4sqi.net/img/general/500x500/13893908_t7OjS4DdVPAV0gMJL5N6g_qM2UEUZUFndo5uHDtdVD0.jpg")
# print(i)