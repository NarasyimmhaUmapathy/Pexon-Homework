

import unittest
import requests

from app import movies

class ApiTest(unittest.TestCase):
    API_URL = "http://localhost:5000"
    MOVIES_URL = "{}/movies".format(API_URL)
    
 

    #get request to url
    def test_1_get_all_movies(self):
        r = requests.get(ApiTest.MOVIES_URL)
        self.assertEqual(r.status_code,200)

    post request to url
    def test_2_add_new_movie(self):
        r = request.post(ApiTest.MOVIES_URL,json=ApiTest.MOVIE_OBJ)
        self.assertEqual(r.status_code,201)

   
    #get request-single movie to url
    #def test_3_get_new_movie(self):
     #   title = "Star Trek 2"
      #  r = requests.get("{}/{}".format(ApiTest.MOVIES_URL,title))
       # self.assertEqual(r.status_code,205)
    
 

if __name__ == "__main_":
    unittest.main()

