# The Creek.
# Author
### [Kelvin-Kiplagat](https://github.com/kelvin-daniel)

# Description
A python-flask application that allows writers to post blogs, edit and delete blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to receive email every time a new blog is posted by a writer.

## Live Link
[View Site](https://????????????.herokuapp.com)

## Features
- A user can view the most recent posts.
- View and comment the blog posts on the site.
- A user should an email alert when a new post is made by joining a subscription.
- Register to be allowed to log in to the application
- A user sees random quotes on the site
- A writer can create a blog from the application and update or delete blogs I have created.

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/kelvin-daniel/blog.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd D-Blog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  ./start.sh
  ```
5. Testing the application
  ```bash
  python manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* Python
* Flask
* Javascript
* Css
* Html
* Heroku for deployment

## Known Bugs.
* There are no known bugs currently.

## version 1.0

## Contact Information 

Email: kaymutor@gmail.com

## License
* *MIT License:*
* Copyright (c) 2020 **kelvin kiplagat**