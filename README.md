# restapi-getting-data-in-xlsheet


Here are the various end points that I created in this project<br>
POST-http://127.0.0.1:8000/api/account/create/user/<br>
This endpoint is used to create user by providing the user details<br>
Body Request:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "string"<br>
}<br>
Responses:<br>
HTTP_201_CREATED<br>

Response Body:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>POST-http://127.0.0.1:8000/api/account/user/token/</h4><br>
This is used to generate the token for the user which can be used for the authentication<br>

Request Body:<br>

{<br>
  "email": "user@example.com",<br>
  
  "password": "string"<br>
}<br>

Responses:<br>

STATUS_200_OK<br>

Response Body:<br>

{<br>
    "token": "string"<br>
}<br>


<h4>GET-http://127.0.0.1:8000/api/account/user/manage/</h4><br>
It will retrieve the user information 
Request Body:<br>
In the headers of the request with the field name of authorization sending user's token<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
RESPONSES:<br>
STATUS:200<br>
RESPONSE_BODY:<br>
{<br>
    "email": "string",<br>
    "name": "string"<br>
}<br>

<h4>PATCH:http://127.0.0.1:8000/api/account/user/manage/</h4><br>

This API endpoint is used to update the user object partially<br>

Request Body:
Addd the authorization token to the header for authentication purpose<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
and the user's information in the body of the request:<br>

{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringt"<br>
}<br>

RESPONSES:<br>
STATUS:200<br>

Response Body:<br>
The Response contains the user information with updated fields<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>PUT:http://127.0.0.1:8000/api/account/user/manage/</h4><br>

This API endpoint is used to update the entire user object<br>

Request Body:
Addd the authorization token to the header for authentication purpose<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
and the user's information in the body of the request:<br>

{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringt"<br>
}<br>

RESPONSES:<br>
STATUS:200<br>

Response Body:<br>
The Response contains the user information with updated fields<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>




<h1>GET:/api/excelapp/excel/import</h1><br>

This API endpoint is used to retreive the details of the user from the User Model in the SPREADSHEET file.<br>

Header:<br>
{<br>
'authorization':"Token adminusertoken"<br>
}<br>

Responses:<br>

STATUS:200_OK<br>

Response Body:<br>
It returns the excel file contains the column names of the model and the data<br>

<h1>POST:/api/excelapp/excel/export</h1><br>
This API endpoint is used to when the user send the data in the Json Format and it returns the data in the excel file.<br>
It won't create the data in the server it only sends the excel data<br>

Request Body:<br>
[<br>
{<br>
 "field1": "value",<br>
 "field2": "value"<br>
},<br>
{<br>
 "field1": "value",<br>
 "field2": "value"<br>
}<br>

]<br>

RESPONSES:<br>
status:200<br>

Response Body:<br>

Excel file with column names as keys of Json Data and the row values as key values<br>

























