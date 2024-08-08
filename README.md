# chess-backend
[Chess Master](https://github.com/Jin2oo2/chessboard)'s backend Web API (RESTful)\
This API is developed with Django REST framework and JSON Web Token for authentication scheme
## Endpoints
POST `/singup`\
Register a user with username and password\
<br>
POST `/login`\
Login a user with username and password\
<br>
GET `/logout`\
Logout a user\
<br>
POST `/newgame`\
Create a new game with payload: level, result\
<br>
GET `/games`\
List all games created
