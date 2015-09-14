##class ClassName(object):
    #"""docstring for """
    #def __init__(self, arg):
        #super(, self).__init__()
        #self.arg = arg
all_movies={}
all_users={}
import math
import csv





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
        def __init__(self,name, movie_id):
            self.id=movie_id
            self.name = name
            self.genres = genres
            all_movies[self.id] = self
            self.ratings={}
        def rating(self):
            return self.ratings.values()
        def __repr__(self):
            return self.__str__()
        def __str__(self):
            return 'Movie(movie_id={}, movie_title={})'.format(self.ident, repr(self.title))
        def get_movie_ratings(self):
            return sorted(self.ratings.values(),reverse=True)
        def get_movie_title(self):
            return all_movies[self.id].title
        def get_movies():
            with open('ml-100k/u.item', encoding='latin_1') as f:
                reader =csv.DictReader(f, fieldnames=['movie_id', 'movie_title' ], 
                for row in reader:
                    Movie(int(row['movie_id']), row['movie_title'])

        def euclidean_distance(list_1, list_2):
            if len(list_1) is 0:
                return 0
            differences =[list_1[idx] - list_2[idx] for idx in range(len(list_1))]
            squares =[diff ** 2 for diff in differences]
            sum_of_squares =sum(squares)
                return 1/(1 + math.sqrt(sum_of_squares))

        def load_ratings():
            with open('ml-100k/u.data') as f:
                reader =csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating'], t')
                for row in reader:
                    Rating(int(row['user_id']), int(row['movie_id']), int(row['rating']))
        def load_data():
            load_movies()
            load_users()
            load_ratings()

class Rating:
        def __init__(self, user_id, movie_id, stars):
            self.user_id = user_id
            self.item_id = movie_id
            self.item_id = stars
            all_movies[self.movie_].add_rating[self]
        def __repr__(self):
            return self.__str__()


    def __str__(self):
        return 'Rating(rating_user={}, rating_movie={}, rating={})'.format(self.user_id, self.movie_id, self.stars)

def main():
    load_data()
    print(all_users[1].recommendations(10))


if __name__ == '__main__':
    main()
