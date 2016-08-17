# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:29:58 2016

@author: MrP
"""
import webbrowser

class Movie():
    """This is the class Movie for movies"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Initiates movie objects with four attributes:
        title, description, image url, trailer url. """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

                                                                                
