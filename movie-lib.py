##class ClassName(object):
    #"""docstring for """
    #def __init__(self, arg):
        #super(, self).__init__()
        #self.arg = arg
all_movies={}
all_users={}





class User:
        def __init__(self,user_id):
            self.id_num = user_id
            all_users[self.user_id] = self


class Movie:
        def __init__(self,**kwargs):
            self.movie_id = ''
            self.name = ''
            self.genres = []
            all_movies{self.id] = self}
        def rating(self):
            return self.ratings.values()

class Rating:
        def __init__(self, user_id, movie_id, stars)
            self.user_id = user_id
            self.item_id = movie_id
            self.item_id = stars
            all_movies[self.movie_].add_rating[self]
