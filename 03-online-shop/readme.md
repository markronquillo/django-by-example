
## Chapter 7: Building an Online Shop

You will create a catalog of products and implement a shopping cart using Django sessions. You will also learn how to create custom context processors and launch asynchronous tasks using Celery.

- Create Product catalog
- Build shopping cart using Django sessions
- Manage customer orders
- Send asynchronous notifications to customers using Celery


In customizing the admin page, we can use the `list_editable` to set the fields that can be editted in the list display page of the admin module.


#### Using Django sessions

The session framework allows you to store arbitrary data for each visitor. Session data is stored on the server side, and cookies contain the session ID, unless you use the cookie-based session engine.

The session middleware manages sending and receiving cookies.

```python
	request.session['foo'] = 'bar'
	request.session.get('foo')
	del request.session['foo']
```

Django offers the following options for storing session data:
	•	 Database sessions: Session data is stored in the database. This is the default session engine.
	•	 File-based sessions: Session data is stored in the file system.
	•	 Cached sessions: Session data is stored in a cache backend. You can specify cache backends using the CACHES setting. Storing session data in a cache system offers best performance.
	•	 Cached database sessions: Session data is stored in a write-through cache and database. Reads only use the database if the data is not already in the cache.
	•	 Cookie-based sessions: Session data is stored in the cookies that are sent to the browser


#### Context processors

A context processor is a python function that takes the request object as an argument and returns a dictionary that gets added to the request context.


Celery and RabbitMQ

#### Integrating a payment gateway

A payment gateway allows you to process payments online. 

The checkout process should work as follows:
1. User add items to their shopping cart.
2. User checkout their shopping cart
3. Users are redirected to Paypal for payment
4. Paypal sends a payment notification to our site
5. Paypal redirects u sers back to our website.



#### Getting payment notifications
IPN is a method offered by most payment gateways to track purchases realtime.

A notification is instantly sent to yoru server when the gateway processes a payment. 


#### Exporting orders to CSV files

