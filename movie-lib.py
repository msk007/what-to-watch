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
            self.ratings={}

        def get_user_rating(self, rating):
            return self.ratings

        def add_user_rating(self):
            self.ratings[rating.movie]=rating.score

class Movie:
        def __init__(self,**kwargs):
            self.movie_id = ''
            self.name = ''
            self.genres = []
            all_movies{self.id] = self}
        def rating(self):
            return self.ratings.values()
        def __repr__(self):
            return self.__str__()
        def get_movie_ratings(self):
            return sorted(self.ratings.values(),reverse=True)
        def get_movie_title(self):
            return all_movies[self.id].title


class Rating:
        def __init__(self, user_id, movie_id, stars):
            self.user_id = user_id
            self.item_id = movie_id
            self.item_id = stars
            all_movies[self.movie_].add_rating[self]
