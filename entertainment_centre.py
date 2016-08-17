# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:40:46 2016

@author: MrP
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy_Story", "Toys that come to life", 
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://youtu.be/KYz2wyBy3kc")



avatar = media.Movie("Avatar", "Stuff about aliens",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://youtu.be/5PSNL1qE6VY")
                     
                     

                     
movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)

