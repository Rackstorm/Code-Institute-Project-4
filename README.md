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

# Project Goals
## User Goals
## Site Owner Goals
## Target Audience

## User Stories

* As a user, I want to create an account with a unique username and password, so I can start sharing and managing my recipes.
* As a registered user, I want to log in and out of my account to access my saved recipes and submit new recipes.
* As a user, I want to upload a recipe with a title, ingredients, steps, and an optional photo.
* As a user, I want to edit my existing recipes, so I can update them with new information or corrections.
* As a user, I want to delete my recipes if I no longer want them to be available on the platform.
* As a user, I want to browse and search for recipes submitted by other users.
* As a user, I want to like and save recipes I find interesting, so I can access them later in my saved recipes.
* As a user, I want to leave comments on recipes to ask questions, provide feedback, or share my thoughts.
* As a user, I want to view my profile, where I can see the recipes I've submitted, my liked recipes, and saved recipes.
* As an admin, I want the ability to moderate content, including the ability to remove inappropriate or spammy recipes and comments.


# Planning

## 1. Strategy:
- **Project Goals:** Define objectives for sharing, discovering, and managing recipes.
- **User-Centric Approach:** Understand the needs of users interested in cooking.
- **Engagement Strategy:** Encourage actions like liking recipes and fostering a sense of community.

## 2. Scope:
- **Feature Set:** Clearly define features including recipe management and user profiles.
- **User Restrictions:** Establish limitations on modifying or deleting posts.
- **Content Guidelines:** Set quality standards for recipe content.

## 3. Structure:
- **Information Architecture:** Organize recipes and profiles logically.
- **Intuitive Navigation:** Create user-friendly menus for easy exploration.
- **Workflow Design:** Design clear workflows for recipe actions.

## 4. Skeleton:
- **Wireframes:** Develop visual layouts emphasizing simplicity.
- **Prototypes:** Create interactive models to test user interactions.
- **User Feedback:** Gather input to refine wireframes and prototypes.

## 5. Surface:
- **Visual Design:** Implement an appealing design with culinary-themed elements.
- **Consistent UI Elements:** Ensure a cohesive design across all pages.
- **Responsive Design:** Optimize visuals for various devices.

Aligning "The Recipe Exchange" with these UX planes ensures a delightful experience for users passionate about sharing and exploring new recipes.

## Database
## Wireframes

![Index](/static/images/readme_files/wireframes/index.png)
![Signup](/static/images/readme_files/wireframes/signup.png)
![Login](/static/images/readme_files/wireframes/login.png)
![Create](/static/images/readme_files/wireframes/create.png)
![Search](/static/images/readme_files/wireframes/search.png)
![Profile](/static/images/readme_files/wireframes/profile.png)
![Signout](/static/images/readme_files/wireframes/signout.png)

## Design
The project design utilizes the "Poppins" font for a modern appearance and a color scheme featuring contrasting colors like white and hot pink for readability. It employs responsive layout techniques for compatibility with various screen sizes. Navigation elements maintain consistency in design and responsiveness. 

Forms are styled for clarity and ease of use, while images feature rounded corners and box-shadow effects. Media queries ensure adaptability across devices, and the footer section stands out with a distinctive background color. Overall, the design focuses on usability, readability, and visual appeal.

## Structure

The webpage structure includes a navigation bar for easy site navigation, a container for housing main content and Bootstrap alert messages, a main content section for dynamically rendering page-specific content, a footer displaying project information and social media links, and a script section for managing the dismissal of Bootstrap alert messages. This structure ensures a cohesive layout, responsive design, and improved user experience throughout the website.

# Features

## Home
- The landing page where you can explore featured recipes and discover new culinary ideas.

![LandingPage](/static/images/readme_files/landingpage.png)

## Login
- Log in to your account to access your profile and create or manage your recipes.

![Login](/static/images/readme_files/signin.png)

## Register
- Create a new account and join the Recipe Exchange community.

![Register](/static/images/readme_files/register.png)

## Find Recipe
- Search for recipes based on keywords, ingredients, or categories.

![SearchRecipe](/static/images/readme_files/search.png)

## Create Recipe
- Share your favorite recipes with the community by creating your own.


## Profile
- View and manage your profile, including your posted recipes and saved recipes.

## Logout
- Log out of your account for security and privacy.

# Technologies

The Recipe Exchange is built using various technologies:

- Django: A Python web framework for building web applications.
- Bootstrap: A front-end framework for responsive and visually appealing design.
- PostgreSQL: An open-source relational database for data storage.
- Cloudinary: Cloud-based image storage for recipe images.
- Heroku: The platform where the project is deployed.
- Git and GitHub: Version control and code repository management.
- Visual Studio Code (VS Code).

# Deployment

The project is deployed on Heroku, a cloud platform for hosting web applications. It can be accessed online at [Heroku Recipe Exchange](https://myurl.com).

## Deployment process:
1. Create a Heroku account and install the Heroku CLI.
2. Set up a new Heroku app and connect it to my project's Git repository.
3. Configure environment variables for settings like database connection and secret keys.
4. Deploy my project to Heroku manually by logging in and connecting it to the GitHub repository directly on the site.
5. Migrate your database and run any necessary setup tasks.
6. Opened up my app on Heroku.

# Bugs

| Problem | Resolution |
|---------|------------|
| **Autoslug Issue:** Autoslug wasn't functioning as expected. | Added the `autoslug` package to the project by including it in the project's dependencies. Incorporated `AutoSlugField` in the `models.py` file for the `Post` model to generate slugs based on the post title. Verified that the slug field was populated correctly. Updated the corresponding URL patterns to use slugs for better SEO-friendly URLs. |
| **Slug Generation:** The manual process of creating slugs was time-consuming. | Utilized the `AutoSlugField` provided by the `autoslug` package in the `Post` model to automate the generation of slugs based on the post title. This not only streamlined the workflow but also ensured consistent and SEO-friendly URLs for each post. |
| **Search Functionality:** Needed a search functionality for recipes. | Implemented a search form (`SearchForm`) and a corresponding view (`PostSearch`) to filter recipes based on search terms. Enhanced user experience by allowing users to find relevant recipes efficiently. |
| **Image Upload Issue:** Difficulty with image upload in the `PostCreateForm`. | Configured the `PostCreateForm` to handle file inputs for image uploads. Added appropriate widget attributes to the form fields related to file uploads. Ensured that the `MEDIA_ROOT` and `MEDIA_URL` settings in Django were correctly configured to handle uploaded media files. |
| **Pylint Error (Post and Profile Classes):** `Class 'Post' has no 'objects' member` and `Class 'Profile' has no 'objects' member` | Ignored the pylint errors related to the absence of `objects` member for the `Post` and `Profile` classes. These errors are due to the use of custom managers in Django models, and the issue has already been defined in the `models.py` file. The code is functioning as intended, and these errors do not impact the application's behavior. |



# Testing

## Manual Testing
- Registering user.
- Creating Recipes (*Note: Not functioning*).
- Saving Recipes.

## Django Testing
- `test_views.py`.
The test_views.py file contains test cases for the views in The Recipe Exchange project. These tests ensure the proper functioning of key features, such as post listing, detailed post viewing, and user interactions like liking posts. 

- `test_models.py`.
The test_models.py file includes tests for the project's models. It ensures the correct creation of categories, posts, and comments with expected attributes. The tests cover aspects such as category string representation, post creation with user and category relationships, and comment creation with associated posts. These tests validate the integrity of the database models, guaranteeing the accurate storage and retrieval of essential data within The Recipe Exchange.

- `test_forms.py`.
In the test_forms.py file, various scenarios are tested for different forms, including comments, searches, post creation, signup, and profile editing. The tests ensure that the forms validate and handle both valid and invalid user input, maintaining the functionality and integrity of The Recipe Exchange web application.

## Validator Testing

Validator testing ensures that the HTML, CSS, and JavaScript used in the project meet web standards.

# Credits

- Recipe images and background images are from Jooinn.com.
- Favicons are created by using icons from Icon8 and FaviconGenerator.com.
