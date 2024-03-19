# The Recipe Exchange
**A Code Institute fullstack project**

![Mockup](/static/images/readme_files/mockup.png)

The Recipe Exchange is a web application designed for users to discover, share, and exchange their favorite recipes. Whether you're a cooking enthusiast or simply looking for meal ideas, The Recipe Exchange offers a platform to connect with others and explore a variety of recipes.

For the basic structure of this Django project I have been borrowing code from Code Institutes' "I Think, Therefore I Blog" project and modified it, as well as added my own code.

# A Deadline To Remember 

The deadline for this school project was on the 18th of December. However, on the 18th of December at 10:58 AM I gave birth to my second son, Henry. :) Doing this project while being pregnant and taking care of a toddler has been a challenge. Finalizing this project with a toddler and a baby was even harder.

This will not be the prettiest project I have submitted - but it will forever be the most memorable in many ways.

With that said, I apologize for the retro 90's look - enjoy the Swedish recipes though. :) 

## Contents

- [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [Target Audience](#target-audience)
- [Pages](#pages)
  - [Home](#home)
  - [Login](#login)
  - [Register](#register)
  - [Find Recipe](#find-recipe)
  - [Create Recipe](#create-recipe)
  - [Profile](#profile)
  - [Logout](#logout)
- [User Stories](#user-stories)
  - [Creating an Account](#creating-an-account)
  - [Logging In and Out](#logging-in-and-out)
  - [Uploading a Recipe](#uploading-a-recipe)
  - [Editing and Deleting Recipes](#editing-and-deleting-recipes)
  - [Browsing and Searching for Recipes](#browsing-and-searching-for-recipes)
  - [Interacting with Recipes](#interacting-with-recipes)
  - [Managing Profile](#managing-profile)
  - [Admin Actions](#admin-actions)
- [Planning](#planning)
  - [Issue Tracking Tool](#issue-tracking-tool)
  - [Project Board](#project-board)
  - [User Story Template](#user-story-template)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
  - [Database Scheme](#database-scheme)
- [Security](#security)
- [Wireframes](#wireframes)
- [Design](#design)
- [Structure](#structure)
- [Features](#features)
  - [Home](#home-1)
  - [Login](#login-1)
  - [Register](#register-1)
  - [Find Recipe](#find-recipe-1)
  - [Create Recipe](#create-recipe-1)
  - [Profile](#profile-1)
  - [Log out](#log-out)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Django Testing](#django-testing)
  - [Validator Testing](#validator-testing)
- [Credits](#credits)


# Project Goals
The project aims to create a user-friendly recipe sharing platform that allows users to discover, share, and explore a variety of recipes. It seeks to provide an intuitive interface for users to find recipes based on different categories and preferences.

## User Goals
- Find and discover new recipes easily.
- Share their own recipes with the community.
- Interact with other users by liking and commenting on recipes.
- Easily navigate the platform and access relevant information.
- Have a visually appealing and responsive user interface.

## Site Owner Goals
- Create a vibrant community around cooking and recipe sharing.
- Engage users by providing valuable content and features.
- Increase user retention through interactive features and personalized experiences.
- Collect insights into user preferences and behavior for continuous improvement.

## Target Audience
The target audience includes cooking enthusiasts, home cooks, food bloggers, and anyone interested in exploring and sharing recipes. It caters to individuals of all skill levels, from beginners to experienced chefs, who are passionate about cooking and experimenting with new dishes.


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

Throughout the project planning phase, I have employed GitHub's issue tracking tool and project board to facilitate an agile working methodology. By leveraging these tools, I have streamlined project management processes, enabling effective collaboration, task prioritization, and iterative development cycles.

## Issue Tracking Tool
![Issues](/static/images/readme_files/issues.png)

## Project Board
![UserStories](/static/images/readme_files/userstories.png)

## User Story Template
![UserStory](/static/images/readme_files/userstory.png)

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



## Database Scheme
![Flowchart](/static/images/readme_files/diagram.png)


### Entity Relationship Diagram (ERD)

| Entity   | Attributes                                                                       |
|----------|----------------------------------------------------------------------------------|
| Category | id (PK) <br> title (Unique)                                                     |
| Post     | id (PK) <br> title (Unique) <br> slug (Unique) <br> author_id (FK to User) <br> category_id (FK to Category, nullable) <br> featured_image <br> excerpt <br> updated_on <br> content <br> created_on <br> status <br> likes (Many-to-Many relationship with User) |
| PostLike | id (PK) <br> post_id (FK to Post) <br> user_id (FK to User)                     |
| Comment  | id (PK) <br> post_id (FK to Post) <br> name <br> email <br> body <br> created_on <br> approved |
| Profile  | user_id (PK, FK to User) <br> bio <br> liked_posts (Many-to-Many relationship with Post) <br> profile_picture |

## Security

### Cross-Site Request Forgery (CSRF) Protection
- Implementing CSRF protection helps prevent malicious websites from executing unauthorized actions on behalf of authenticated users.
- Django provides built-in CSRF protection by including a CSRF token with each form submission and verifying it on the server side.

### Django Allauth for Authentication and Authorization
- Django Allauth is an authentication and authorization framework that provides features like registration, login, password management, and social authentication.
- It ensures secure user authentication and authorization processes.

### Restricted Features for Authenticated Users
- Certain features, such as creating, editing, or deleting recipes, are reserved for authenticated users only.
- By requiring users to be logged in to access these features, the application enhances security and ensures that sensitive operations are performed by authorized individuals only.


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
![CreateRecipe](/static/images/readme_files/create_recipe.png)

## Profile
- View and manage your profile, including your posted recipes and saved recipes.
![Profile](/static/images/readme_files/profile.png)

## Log out
- Log out of your account for security and privacy.
![SignOut](/static/images/readme_files/signout.png)

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
| Likes Functionality                    | Likes feature not functioning as expected. Likes not being registered or counted correctly due to issues in the `views.py` and `models.py` files. Investigated and fixed logic related to registering and counting likes. Resolved issues related to the display of liked recipes on the user's profile page. |
| Profile Management                    | Issues with user profile management. Problems with profile creation, login, mechanisms due to errors in `views.py` settings. Reviewed and debugged profile creation. Made necessary adjustments in `views.py` and `settings.py` to ensure smooth user profile management. |
| Post Creation        | Various errors and unexpected behaviors in posts. Bugs and glitches in post creation functionality due to code inconsistencies and errors in `views.py` and `forms.py` files. Identified and addressed specific issues in post creation functionality in `views.py` and `forms.py`. Implemented comprehensive error logging and monitoring in the application to track and resolve issues quickly. |
| Search Functionality     | Problems with search functionality due to inconsistencies in code. Search functionality not returning expected results due to code inconsistencies and errors in `views.py` and `forms.py` files. Identified and addressed specific issues in search functionality in `views.py` and `forms.py`. Implemented comprehensive error logging and monitoring in the application to track and resolve issues quickly. |
| Typo in URLs.py                        | Initially, there was a typo in the urls.py file, which caused an AttributeError. Identified and corrected the typo in the urls.py file, resolving the AttributeError. |
| Add Recipe                             | Difficulty in adding new recipes       . Identified issues with form validation and database interaction in `views.py` and `forms.py`. Implemented necessary changes to ensure proper validation and saving of new recipe data. |
| Categories Implementation             | Difficulty in implementing category functionality. Category filtering not working properly due to incorrect logic in the `views.py` file. Updated `views.py` to ensure proper association of posts with categories. Made changes in `models.py` to handle category data in the database correctly. Implemented validation in the front-end forms to ensure accurate category selection by users. |





# Testing

## Manual Testing

| Input                                    | Expected Output                                         | Actual Output                               |
|------------------------------------------|----------------------------------------------------------|---------------------------------------------|
| Registering a new user                  | New user registered successfully.                        | Pass. No errors.                           |
| Registering a new admin                 | New admin registered successfully.                       | Pass. No errors.                           |
| Sign in/sign out                        | Signing in/out successfully with confirmation showing on page. | Pass. No errors.                           |
| Creating a new recipe                   | Adding recipes with relevant information.               | Pass. Various errors but now resolved.     |
| Managing recipes                        | Editing, deleting, liking, and commenting recipes.      | Pass. Various errors but now resolved.     |
| Searching for recipes                   | By title, keywords, category, author                    | Pass. Various errors but now resolved.     |
| Managing profile page                   | Add/edit profile image, bio, and get an overview of liked and created recipes. | Pass. Various errors but now resolved.    |
| Links working                           | All links are working when clicked.                      | Pass. No errors.                           |




## Django Testing
- `test_views.py`.
The test_views.py file contains test cases for the views in The Recipe Exchange project. These tests ensure the proper functioning of key features, such as post listing, detailed post viewing, and user interactions like liking posts. 

- `test_models.py`.
The test_models.py file includes tests for the project's models. It ensures the correct creation of categories, posts, and comments with expected attributes. The tests cover aspects such as category string representation, post creation with user and category relationships, and comment creation with associated posts. These tests validate the integrity of the database models, guaranteeing the accurate storage and retrieval of essential data within The Recipe Exchange.

- `test_forms.py`.
In the test_forms.py file, various scenarios are tested for different forms, including comments, searches, post creation, signup, and profile editing. The tests ensure that the forms validate and handle both valid and invalid user input, maintaining the functionality and integrity of The Recipe Exchange web application.

## Future features to implement

| Feature                                      | Description                                                                |
|----------------------------------------------|----------------------------------------------------------------------------|
| E-mail Confirmation                         | Implement mandatory e-mail verification upon registration to enhance account securitgit ay and user validation.                                       |
| CSS Styling                                 | Refine CSS styling to address spacing and padding issues for improved visual consistency and user experience.                                 |
| Community Development                       | Enable members to interact by allowing profile visits and forum posting, fostering a sense of community engagement and user interaction.   |


## Validator Testing

Validator testing ensures that the HTML, CSS, and JavaScript used in the project meet web standards.

### Lighthouse
Warnings due to 3rd party cookies - in this case Cloudinary. As well as large images when uploading images to Cloudinary. Resizing images automatically is possible, but I ran out of time to make it work - however, I will look into it further in the future.

![Lighthouse](/static/images/readme_files/lighthouse.png)

### W3C Validator
No errors.
![HTMLChecker](/static/images/readme_files/htmlchecker.png)

### CSS Validator
No errors.
![Jigsawt](/static/images/readme_files/jigsaw.png)

## Code Institute - CI Python Linter
No errors.

# Credits

- Recipe images and background images are from [Jooinn.com](https://www.jooinn.com/).
- Favicons are created by using icons from [Icon8](https://icons8.com/) and [FaviconGenerator.com](https://www.favicon-generator.org/).
- Flowchart from [Draw.io](https://app.diagrams.net/). 
- The basic code structure of this project has been borrowed from Code Institutes project "I think, therefore I blog" and has been modified.
- Troubleshooting with the help from [Stack Overflow](https://stackoverflow.com/).
- [Codemy.com](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw)'s YouTube tutorials:
  - [Create a Simple Blog with Python and Django](https://www.youtube.com/watch?v=x1iqcV3Wgnw)
  - [Django Blog](https://www.youtube.com/watch?v=zb4fIvtn4tY)
  - [Create a Simple Blog with Python and Django Playlist](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
- [KSDunne](https://github.com/KSDunne)'s Statement Beauty project - [GitHub Link](https://github.com/KSDunne/statement_beauty)
- [Dennis Ivy's tutorial](https://www.youtube.com/watch?v=llbtoQTt4qw) - Forms, registrations, user etc.
