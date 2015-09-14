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
        def recommendations(self, num):
            recs = {}
        while len(recs) < num*5:
            for usr in self.get_similar_users():
                for rat in usr.ratings.values():
                    if rat.item_id not in self.ratings and rat.stars > 3:
                        if rat.item_id in recs:
                            holder = rat.stars*euclidean_distance(*euclid_prep(self, usr))
                            if holder > recs[rat.item_id][1]:
                                recs[rat.item_id] = [rat, holder]
                        else:
                            recs[rat.item_id] = [rat, rat.stars*euclidean_distance(*euclid_prep(self, usr))]
                            sort_recs = sorted(recs.values(), key=lambda r: r[1], reverse=True)
                                return ([all_movies[x[0].item_id] for x in sort_recs][:num])


        def get_top(self, num):
            return sorted([mov for mov in all_movies.values()
                          if mov.ident not in self.ratings],
                     key=lambda m: m.avg_ratings(), reverse=True)[:num]


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
        reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', '', '', 'something_else' ], delimiter='|')
        for row in reader:
            Movie(int(row['movie_id']), row['movie_title'])

        def euclidean_distance(list_1, list_2):
            if len(list_1) is 0:
                return 0
            differences =[list_1[idx] - list_2[idx] for idx in range(len(list_1))]
            squares =[diff ** 2 for diff in differences]
            sum_of_squares =sum(squares)
            return 1/(1 + math.sqrt(sum_of_squares))
        def euclid_prep(user_1, user_2):
            list_1=[y.stars for y in sorted([x for x in user_1.ratings.values() if x.item_id in user_2.ratings], key=lambda r:r.item_id)]
            list_2=[y.stars for y in sorted([x for x in user_2.ratings.values() if x.item_id in user_1.ratings], key=lambda r:r.item_id)]
    return list_1, list_2
    def load_users():
            with open('ml-100k/u.user') as f:
                reader = csv.DictReader(f, fieldnames=['user_id'], )
                for row in reader:
                    User(int(row['user_id']))

    def load_ratings():
        with open('ml-100k/u.data') as f:
            reader =csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating'])
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
            all_movies[self.movie_].add_rating(self)
            all_users[self.user.id].add_rating(self)
        def __repr__(self):
            return self.__str__()


        def __str__(self):
            return 'Rating(rating_user={}, rating_movie={}, rating={})'.format(self.user_id, self.movie_id, self.stars)

def main():
    load_data()
    print(all_users[1].recommendations(10))


if __name__ == '__main__':
    main()
