# registration_form
Write a program for user registration in fastAPI ( Using postgreSQL )

Registration fields – Full Name,Email,Password,Phone,Profile_picture
Create table Users  to store :  First Name,Password,Email,Phone
Create table Profile to store  : Profile_picture
Check Email , Phone already exist

     2.  GET method – get registered user details
	
Hint : Unique user_id, Connect two tables (Users and Profile) using user_id as foreign key

virtual environment: register

for registration : http://127.0.0.1:8000/regapp/register/

for user details : http://127.0.0.1:8000/regapp/user-details/
