# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:40:46 2016

@author: MrP
"""

import media
import fresh_tomatoes

# Movie constructor is called to initiate instances of movies

toy_story = media.Movie("Toy_Story", "Toys that come to life", 
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",  #NOQA
                        "https://youtu.be/KYz2wyBy3kc")



avatar = media.Movie("Avatar", "Stuff about aliens",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  #NOQA
                     "https://youtu.be/5PSNL1qE6VY")
                     


click = media.Movie("Click", "Remote control that works for people/life",
                    "http://www.gstatic.com/tv/thumb/movieposters/159128/p159128_p_v8_aa.jpg", #NOQA
                    "https://youtu.be/9_VrHQ026wA")
                    

# a list of movies is created to pass to open_movies_page function                   
movies = [toy_story, avatar, click]

# html page is generated using this function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)

