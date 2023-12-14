# The Recipe Exchange
**A Code Institute fullstack project**

![Mockup](/static/images/readme_files/mockup.png)

The Recipe Exchange is a web application designed for users to discover, share, and exchange their favorite recipes. Whether you're a cooking enthusiast or simply looking for meal ideas, The Recipe Exchange offers a platform to connect with others and explore a variety of recipes.

## Contents
- [Pages](#pages)
  - [Home](#home)
  - [Login](#login)
  - [Register](#register)
  - [Find Recipe](#find-recipe)
  - [Create Recipe](#create-recipe)
  - [Profile](#profile)
  - [Logout](#logout)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Django Testing](#django-testing)
  - [Validator Testing](#validator-testing)
- [Credits](#credits)

## Pages

### Home
- The landing page where you can explore featured recipes and discover new culinary ideas.

![LandingPage](/static/images/readme_files/landingpage.png)

### Login
- Log in to your account to access your profile and create or manage your recipes.

![Login](/static/images/readme_files/signin.png)

### Register
- Create a new account and join the Recipe Exchange community.

![Register](/static/images/readme_files/register.png)

### Find Recipe
- Search for recipes based on keywords, ingredients, or categories.

![SearchRecipe](/static/images/readme_files/search.png)

### Create Recipe
- Share your favorite recipes with the community by creating your own.


### Profile
- View and manage your profile, including your posted recipes and account settings.

### Logout
- Log out of your account for security and privacy.

## Technologies

The Recipe Exchange is built using various technologies:

- Django: A Python web framework for building web applications.
- Bootstrap: A front-end framework for responsive and visually appealing design.
- PostgreSQL: An open-source relational database for data storage.
- Cloudinary: Cloud-based image storage for recipe images.
- Heroku: The platform where the project is deployed.
- Git and GitHub: Version control and code repository management.
- Visual Studio Code (VS Code).

## Deployment

The project is deployed on Heroku, a cloud platform for hosting web applications. It can be accessed online at [Heroku Recipe Exchange](https://myurl.com).

Deployment process:
1. Create a Heroku account and install the Heroku CLI.
2. Set up a new Heroku app and connect it to my project's Git repository.
3. Configure environment variables for settings like database connection and secret keys.
4. Deploy my project to Heroku manually by logging in and connecting it to the GitHub repository directly on the site.
5. Migrate your database and run any necessary setup tasks.
6. Opened up my app on Heroku.

## Bugs

| Problem | Resolution |
|---------|------------|
| **Autoslug Issue:** Autoslug wasn't functioning as expected. | Added the `autoslug` package to the project and incorporated `AutoSlugField` in the `models.py` file. Ensured it populated the slug field correctly based on the post title. |
| **Search Functionality:** Needed a search functionality for recipes. | Implemented a search form (`SearchForm`) and a corresponding view (`PostSearch`) to filter recipes based on search terms. |
| **Image Upload Issue:** Difficulty with image upload in the `PostCreateForm`. | Configured the form to handle file inputs and added appropriate widget attributes. Ensured that the `MEDIA_ROOT` and `MEDIA_URL` settings were correctly set. |


## Testing

### Manual Testing
- Registering user.
- Creating Recipes (*Note: Not functioning*).
- Saving Recipes.

### Django Testing
- `test_views.py`.
The test_views.py file contains test cases for the views in The Recipe Exchange project. These tests ensure the proper functioning of key features, such as post listing, detailed post viewing, and user interactions like liking posts. 

- `test_models.py`.
The test_models.py file includes tests for the project's models. It ensures the correct creation of categories, posts, and comments with expected attributes. The tests cover aspects such as category string representation, post creation with user and category relationships, and comment creation with associated posts. These tests validate the integrity of the database models, guaranteeing the accurate storage and retrieval of essential data within The Recipe Exchange.

- `test_forms.py`.
In the test_forms.py file, various scenarios are tested for different forms, including comments, searches, post creation, signup, and profile editing. The tests ensure that the forms validate and handle both valid and invalid user input, maintaining the functionality and integrity of The Recipe Exchange web application.

### Validator Testing

Validator testing ensures that the HTML, CSS, and JavaScript used in the project meet web standards.

## Credits

- Recipe images and background images are from Jooinn.com.
- Favicons are created by using icons from Icon8 and FaviconGenerator.com.
