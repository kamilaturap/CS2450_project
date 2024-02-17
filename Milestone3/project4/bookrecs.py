'''
Project Name: Book Recommendations
Name: Cameron Hurst
Due Date: 2/2/2022
Course: CS1410-602

This program takes book ratings from a user and gives them recommendations for new books that they might like.

'''

import re


with open('booklist.txt', 'r') as bookfile:
    booklines = bookfile.readlines()
    books = []
    for book in booklines:
        book = tuple(book.strip('\n').split(','))
        books.append(book)

with open('ratings.txt', 'r') as ratingsfile:
    ratinglines = ratingsfile.readlines()
    ratingslst = []
    for rating in ratinglines:
        rating = rating.strip('\n')
        ratingslst.append(rating)
        ratings = {ratingslst[i].lower(): ratingslst[i + 1].strip(' ').split(' ') for i in range(0, len(ratingslst)-1, 2)}
    for key, value in ratings.items():
        map_object = map(int, value)
        ratings[key] = list(map_object)
    userlst= list(ratings.keys())

def dotprod(user):
    '''
    Takes a user as an argument. Returns a dictionary of the dotproduct of all the readers based off of the user's ratings.
    '''
    dotprod_dict = {}
    dotprod_sorted = {}
    user_ratings = ratings[user]
    for reader, reader_ratings in ratings.items():
        if reader != user:
            multiply_list = []
            for i in range(len(user_ratings)-1):
                multiply_list.append(user_ratings[i] * reader_ratings[i])
            dotprod_dict[reader] = sum(multiply_list)
    for key, value in sorted(dotprod_dict.items(), key=lambda item: item[1], reverse=True):
        dotprod_sorted[key] = value
    return dotprod_sorted

def friends(user):
    '''
    Takes a user as an argument. Returns the two readers with the highest dot product in regards to the user.
    '''
    if user in userlst:
        dotprod1 = dotprod(user)
        friends = []
        readerlist = list(dotprod1.keys())
        friends.append(readerlist[0])
        friends.append(readerlist[1])
        friends.sort()
        return friends
    else:
        return 'no'

def friendindexlist (friendnumber, user):
    '''
    Takes 0 or 1 and the user as an argument. Returns a list of book indexs that the input friend has rated 3 or greater and that the user has not read.
    '''
    friends1 = friends(user)
    friend_index_list = []
    for key, value in ratings.items():
        if key == friends1[friendnumber]:
            for rating in enumerate(value):
                if rating[1] >= 3:
                    friend_index_list.append(rating[0])
    return friend_index_list

def recommend(user):
    '''
    Takes a user as an argument. Returns a list of book recommendations for that user.
    '''
    friends1 = friends(user)
    user_index_list = []
    friend_index_list0 = friendindexlist(0, user)
    friend_index_list1 = friendindexlist(1, user)
    recommend_book_idx = []
    recommend_book = []     
    for key, value in ratings.items():
        if key == user:
            for rating in enumerate(value):
                if rating[1] == 0:
                    user_index_list.append(rating[0])
    for j in friend_index_list0:
        if j in user_index_list:
            recommend_book_idx.append(j)
    for j in friend_index_list1:
        if j in user_index_list:
            recommend_book_idx.append(j)    
    for i in range(len(books)):
        if i in recommend_book_idx:
            recommend_book.append(books[i])
    recommend_book.sort(key=lambda item: item[1].split()[1:2])
    recommend_book.sort(key=lambda item: item[1].split()[0])
    recommend_book.sort(key=lambda item: item[0].split()[0])
    recommend_book.sort(key=lambda item: item[0].split()[-1])
    if user in userlst:
        return recommend_book
    else:
        return 'no'
    #print(f'Recommendations for {user} from {friends1[0]} and {friends1[1]}:')
    #for i in recommend_book:
        #print('\t'+i[0]+', '+i[1])
    #print('\n')

def user_input():
    '''
    Requests a user name to be input when running the program. Will return "No such reader : (input)" if the name given does not exist in reader list.
    '''
    user_input = input('Enter a reader\'s name: ').lower()
    if user_input in ratings:
        user = user_input
    else:
        print(f'No such reader: {user_input}')
        exit()
    return user

def report():
    userlst.sort()
    recdict = {}
    for i in range(len(userlst)-1):
        templst = []
        templst.append(friends(userlst[i]))
        tempstring = f'Recommendations for {userlst[i]} from {templst[0][0]} and {templst[0][1]}:\n\t'
        recdict[tempstring] = recommend(userlst[i])
    for key, value in recdict.items():
        newvallst = []
        for i in value:
            newvallst.append(', '.join(i))
        recdict[key] = newvallst
    for key, value in recdict.items():
        newvallst = []
        newvallst.append('\n\t'.join(value))
        recdict[key] = newvallst
    reclst = list(recdict.items())
    recslst = [''.join(j) for i in reclst for j in i]
    for i in recslst:
        i += '\n'
    recstring = ''.join(recslst)
    return recstring