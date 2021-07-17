#Program to get instagram user details using python


#iInstall instagramy Module
#pip install instagramy

#import respective library
from instagramy import InstagramUser

#Take Username as input
name = input("Enter User Name = ")

#instance of Instagram User
user = InstagramUser(name)

#Total Followers
followers = user.number_of_followers
print('Total Followers:- ',followers)

#Total Followings
following = user.number_of_followings
print('Total Followers:- ',following)

#Total  Number of Posts
posts = user.number_of_posts
print('Total posts:- ',posts)



