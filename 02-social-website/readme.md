Creating a social website project


This chapter will cover the following points:
- Using the authentication framework
- Creating user registration views
- Extending the User model with a custom profile model
- Adding social authentication with python-social-auth


#### using django auth framework

`django.contrib.auth` 

AuthenticationMiddleware: Associates user with requests using sessions
Sessionmiddleware: Handles the current session across requests.



#### Posting content from other websites
We are going to allow users to bookmark images from external websites. The user will provide the URL of the image, a title, and optional description. Our application will download the image and create a new Image object in the database.


#### Building a bookmarlet with jQuery

This is how your users will add a bookmarklet to their browser and use it.
1. The user drags a link from your site to his browser's bookmarks.
2. The user navigates to any website and clicks the bookmark.


## Chapter 6: Tracking User Actions

This chapter will cover the following points:
- Creating many-to-many relationships with an intermediary model
- Building ajax views
- creating an activity stream application
- adding generic relatinos to models
- optimizing QuerySets for related objects
- using signals for denormalizing counts
- storing item views in Redis


#### Building a follower system

A follower system enables users to follow other users for them to see the posts shared by those users.


#### Building a generic activiy stream application

An activity stream is a list of recent activities performed by a user or a group of users.

#### Using signals for denormalizing counts

Denormalization is making data redundant in a way that it optimizes read performance

Django comes with a signal dispatcher that allows receiver functions to get notified when certain actions occur. Signals are very useful when you need your code to do something every time something else happens.

`django.db.models.signals`

`pre_save` and `post_save` - sent before or after calling the save() 
`pre_delete` and `post_delete` - Sent before or after calling delete()
`m2m_changed` - Sent when a ManyToManyField on a model is changed

Django signals are synchronous and blocking. Don't confuse signals with async tasks. However you can combine both to launch async tasks when your code gets notified by a signal.

The recommended method for registering your signals is by importing them in the ready() method of yoru application configuration class.


#### Basic Redis

SET total 1
DEL total
GET total
EXPIRE total 2 
EXISTS total

Next steps with Redis

- Counting using incr() and incrby()
- Storing latest items: lpush and rpush, lpop and rpop -- ltrim
- Queues: blocking queue commands
- Caching: expire and expireat
- Pub/Sub:
- Rankings and leadersboards
- Real-time tracking

