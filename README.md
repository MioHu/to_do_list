# To Do List
## Overview
A simple to-do list webapp based on Python and Flask. It used Bootstrap for frontend components and was deployed to Amazon EC2. This is my first solo project and the process is fun :)


## Technologies Used
* Python
* Flask
* Jinja2
* MySQL
* HTML
* CSS
* Bootstrap
* Amazon EC2

## Features
* User: register, log in, update password
* List & Task CRUD
* Set task due date
* Mark task compelete
* Mark list or task with a star
* Share list to other users
* Sort tasks by due date/alphabetically/creation date
* Bootstrap Collapse component
* Delete confirmation modal

## Screenshots
### Register, log in

![regis_login](/screenshots/register_login.jpeg)

### List

![list](/screenshots/list.png)
![list_crud](/screenshots/list_crud.gif)

### Task

![list](/screenshots/task.png)
![list](/screenshots/task_crud.gif)
![sort](/screenshots/sort.gif)

### Share list to another user

* Search user by email

![sort](/screenshots/share1.png)
![sort](/screenshots/share2.png)
* After sending the request, the message will be displayed on the message board of both the sender and receiver
    * Sender
    
    ![sort](/screenshots/share3.png)
    * Receiver can either accept or reject the request. If accept, the list will appear in the user's lists
    
    ![sort](/screenshots/share4.png)
    ![sort](/screenshots/share4.gif)
