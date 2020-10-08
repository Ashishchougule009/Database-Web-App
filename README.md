# Database-Web-App

Database Web is a survey app, that collects the data i.e. 'email ids' and 'height'(in cm) and stores this data in database and sends response email to the user giving 'average height' of the people on his/her particular id
In this app,'Flask' is used from flask library to create website , 'request' is used for fetching the data from user's in put, then data is stored in 'PostGreSQL' using 'SQLAlchemy' library and 'SQLAlchemy' is used to calculate average height and also access data from PostGreSQL.
And finally 'smtplib' is used to send response email.
