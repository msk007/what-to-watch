


from movie_lib import *
rufus=User(1)
jobin =User(2)
movie1 =Movie(02, 'Good Will Hunting')
movie2 =Movie(03, 'Titanic')
rating1 =Rating(will.id, movie1.id, 3)
rating2 =Rating(will.id, movie2.id, 5)
rating3 =Rating(steve.id, movie1.id, 4)
rating4 =Rating(steve.id, movie2.id, 5)
kelly =User(3)
list1 =[1,2,3,4,5]
list2 =[1,2,3,4,5]

def test_user_creation():
    assert will.id == 1
    assert steve.id == 2
    assert will.id != steve.id

def test_movie_creation():
    assert movie1.id ==02 and movie1.title == 'Good Will Hunting'
    assert movie2.id ==03 and movie2.title == 'Titanic'
    assert movie1.id !=movie2.id

def test_user_list():
    assert all_users== {1:User(1),2:User(2), 3:User(3)}

def test_movie_list():
    assert all_movies== {02:Movie(02, 'Good Will Hunting'), 20:Movie(20, 'Brick')}

def test_rating_creation():
    assert rating1.score== 3 and rating1.user == 1 and rating1.movie == 15
    assert rating2.score== 5 and rating2.user == 1 and rating2.movie == 20
    assert rating3.score== 4 and rating4.score == 5 == rating2.score

def test_movie_rating():
    assert movie1.ratings== {1:3,2:4}
    assert movie2.ratings== {1:5,2:5}

def test_user_ratings():
    assert rufus.ratings== {15:3, 20:5}
    assert jobin.ratings== {15:4, 20:5}


def test_get_rating():
    assert movie1.get_movie_ratings() == [4,3]
    assert movie2.get_movie_ratings() == [5,5]

def test_get_average_rating():
    assert movie1.get_average_rating() == 3.5

def test_get_movie_title():
    assert movie1.get_movie_title() == 'Good Will Hunting'

def test_get_user_ratings():
    assert will.get_user_ratings() == {15:3,20:5}

def test_euclidean_distance():
    assert euclidean_distance(list1, list2) == 1
    assert euclidean_distance([], [1,2,3,4,5]) == 0
