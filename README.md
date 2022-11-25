# Your Community Blog

Your Community Blog consists of Member Profiles that have a Role in their Community. That wish to have an About Me Page describing what the do and how they engage with their community. 
This is a great template for other organizations to use for their members.

![Mock Up](docs/readme_images/multi-screen-mockup.png)

## Table of Contents
* [User Experience Design (UX)](#User-Experience-Design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Agile Planning](#Agile-Planning)
          * [Epics](#Epics)
          * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
      * [Features](#Features)
      * [Future Features](#Features-Left-to-Implement)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
        * [Security](#Security)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment) 
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

This webiste is a simple Community Blog that gives it's members the ability to share themselves with other community members. Community members are given the opportunity to upload a picture,
and add a description of themselves like who they are and what they do. If so share conact information. Those who login can comment and like a member. 


### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over three weeks.

All projects were assigned to epics and user stories, prioritized under the labels. User Stories were assigned to Epics and Epics were assigned to sprints. It was done this way to ensure that all core requirements were completed first to maintain completion. More aesthetic User Stories were added near last sprint (This is a personal decision as per how my mind and anxieties work)
Initial Design comes parrarelel with tech and more aesthetic design continues until completion.


The Kanban board was created using github projects and can be located [here] and can be viewed to see more information on the project cards. 

![Kanban image](docs/readme_images/kanban.png)

This Flow chart was created as a visual representation of user processes.

![Flow Chart](docs/readme_images/flow-chart-res.png)

#### Epics

The project had 7 main Epics (milestones):

**EPIC 1 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

**EPIC 2 - "About" Page**

The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

**EPIC 3 - Authentication**

The authentication epic is for all stories related to the registration, login and logout. This epic provides critical functionality and value as without it the members will not be able to create their member page/post.

**EPIC 4 - "Member" Page**

The Member epic is for all stories that relate to the creating, deleting, editing and viewing of the Members of Your Community. This allows for regular users to view Members and for Regitered users to manage "Member" pages with a simple UI interface. It will have a comment section

**EPIC 5 - "Home Page"**

The Home Page epic is for all stories that relate to view all member profiles with thumbnails, summary, profession, contact, Member Page Button, like Button . 

**EPIC 6 - Deployment**

This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

**EPIC 7 - Read Me File**

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application. Photos, Charts and links.

#### User Stories

The following user stories (by epic) were completed over the 3 sprints:

**EPIC 1 - Base Setup** 

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

As a developer, I need to create static resources so that images, css and javascript work on the website

As a developer, I need to set up the project so that it is ready for implementing the core features

As a developer, I need to create the footer with social media links and contact information

As a developer, I need to create the navbar so that users can navigate the website from any device

**EPIC 2 - Home Page**

As a Developer, I want to add thumbnails which will display the Member picture.

As a Developer, I want to add the Members Role

As a Developer, I want to make all Member Information a link to their personal page

As a Developer, I want to add Like/Heart to view

As a Site User, I want to see likes and when the member was created.

As a Site User, I want to see a paginated and neat.

Possible inclusion: As a Developer, I want to add Email Button which will open default email compose me page and add the email in 'To' Section

**EPIC 3 - Page Functions and Site Pagnination**

As a Member, I want to be able to delete my Member Page when it is no longer used.

As an Admin user, I want to be able to delete a Member Page when it is no longer used.

As a Developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist

As a Site User, I would like a "About" page so that I can view information on this website

Aa a Site Admin, I can approve comments so that we can moderate appropriate content.

As a Site Admin I can approve edit and delete members

As a Site User, I can view a paginated list of members so that I can easily view community member.

As a Site User I can **view that my page is awaiting approval through a message on the screen

As a Site User I can view that my page is awaiting approval through a message on the screen

**EPIC 4 - Authentication Epic**

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling

As a Developer, I want to add a Register Page in the Header

As a Developer, I want to add a Sign In Page in the Header

As a Developer, I want to add a Log Out Link in the Navigation Bar- only while logged in.

As a site user I want my page and my interactions with website safe.

**EPIC 5 - Member Page**

As a Site User, I want to be able to create a new Member Page to display myself as professionally skilled. It will have a comment section.

As a Site User, I want to be able to edit a my Member Page when updates are needed.

As a Site Uer, I want to be able to delete my Member Page when it is no longer used.

As an Admin user, I want to be able to delete a Member Page when it is no longer used.

Aa a Site Developer, I need to** create an edit page that the user can upload a photo, contact information, description and a blurb** so that the user can have full CRUD and maintain the desire of the site owner.

Aa a Site User, I can upload a photo, contact information, description and a blurb so that I can manage my post.

**EPIC 6 - Deployment Epic**

As a developer, I need to deploy at the beginning to assure that my project deploys correctly

As a developer, I need to deploy the project to heroku so that it is live for my members and the correct settings are added to settings.py for example DEBUG=False etc.

**EPIC 7 - Read Me File**

Tasks:
* Complete readme documentation


## The-Scope-Plane

* Fully Functioning application
* Backend administration controls.
* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices and a reduced screen size
* Ability to perform CRUD functionality for Members 
* Restricted role based features
* Home page with member information

## The-Structure-Plane

### Features

``USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device``

Implementation:

**Navigation Menu**

 The Navigation contains links for Home, About, Log In, Log Out and has allauth options.

The following navigation items are available.

  * Home -> index.html - View All members at all times
    * About Page -> about.html - Viewed at al times
    * Create Member Page -> create_member.html - Visible after Registration and 
  * Login -> login.html - Visible to users that are logged out.
  * Register -> signup.html - Visible to users that are logged out. 
  * Logout -> logout.html - Visible to logged in users

``USER STORY - As a site owner/ community member, I would like a home page so that the community can find eachother``

Implementation:

**Home Page**

The home page contains a hero image of community members holding bright letters and a lovely Logo. The Navigation bar is eligent and petit fixed to the top while you scroll.
 
This will immediately make it evident to the user, what the purpose of the website is.

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

* Navigation Bar
![Navbar](docs/readme_images/navbar.png)

* Hero Image

![Hero Image](docs/readme_images/hero.png)

* Welcome Section

![Welcome Section](docs/readme_images/welcome.png)

* PAginated Site

![Paginated Site](docs/readme_images/paginated-site.png)

* Social Media Links

![social media links](docs/readme_images/social-media-links.png)

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a Twitter and Facebook link so that users can follow the Your Community blog on social media'

![Footer](docs/readme_images/footer.png)

`` User Story - As a user I would like to Sign- In``

* Sign in Page 

![Sign In Page](docs/readme_images/sign-in-page.png)

``USER STORY - As an Site User, I want to be able to create my own member page``

Implementation:

**Create Member Page**

Create member page was implemented to allow staff users to create new members via the UI without having to use the backend admin panel.

![Create Member](docs/readme_images/create-member-pages.png)

``USER STORY -As a user, I would like to be able to view a member or my member page ``

Implementation:

**View Member Page**

A member page has been implemented to allow users to see the current active members.

* Not Signed In 

![Intro member page](docs/readme_images/introduction-message.png)

* Not Signed In Member Photo and Description

![View Members](docs/readme_images/memberpage-notlogged-in.png)

* Not Signed in Comment section

![Comment Section](docs/readme_images/comment-section-not-signed-in.png)

* Signed In Member Photo and Description

![Intro member page](docs/readme_images/Intro-member-signedin.png)

* Signed in adds Comment section 

![Comment Section](docs/readme_images/signedin-comment.png)


* Signed Out Promt

![sign Out Prompt](docs/readme_images/signout-prompt.png)

``Site User - as a site user I would like to edit and or delete my page``

**Edit Members Page**

* Edit Button and Delete Button

![Edit Member Button](docs/readme_images/edit-button.png)

* Edit Page

![Edit Member](docs/readme_images/edit-page.png)

**Delete Member**

No Page was created. A message alert was created notifying the user that the page was deleted.

Implementation:

**Alert Message**

Generic Alert messages were used to inform members of their actions

* Signed In Message

![Alert Messages](docs/readme_images/signed-in.png)

* Signed-out Message

![Alert Messages](docs/readme_images/signed-out.png)

* Deleted Message

![Alert Messages](docs/readme_images/deleted-message.png)

* Unauthorized to Edit

![Alert Messages](docs/test_images/unauthorized-to-edit.png) 



Implementation:

Favicon
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon](static/media/site_images/favicon.png)

**Error Pages**

``USER STORY - As a developer, I need to implement a 404 error message``

* You are not logged in error page while member is not loged in. 

![You are not logegd In](docs/readme_images/not-loggedin.png)

Implementation:

**404 Message**

As a developer, I need to implement a 404 error page to redirect users to

The 404 message will allow the user to easily understand what is occuring.
This covers:

* Member Detail 
* Delete Member
* Edit Member 

``USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs``

Implementation:

**Base Setup User Stories**

The following stories were implemented in order to set up a base structure for all the HTML pages and the core installations and configurations needed to run the application. While these do not show as individual features, they were stories completed that were needed to implement all of the stories above.

``As a developer, I need to create the base.html page and structure so that other pages can reuse the layout``

``As a developer, I need to create static resources so that images, css and javascript work on the website``

``As a developer, I need to set up the project so that it is ready for implementing the core features``

**Favicon**

A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

### Features Left To Implement

## The-Skeleton-Plane

### Wireframes

Wire frames were also created as a rough sketch to represent obejects within the site.

This is the home page when user is not registered and not logged in.. 

![wire Frame](docs/readme_images/home-first-time.png)

This is a wire frame of a member logged in on the home page.

![wire Frame](docs/readme_images/registered-login-home.png)

This is a wire frame of the member page that is not signed in.

![wire Frame](docs/readme_images/member-page-not-regist.png)

This is a wire frame of the member page with the member logged in and viewing another members page with the ability to comment.

![wire Frame](docs/readme_images/member-pages-logged-in.png)


### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The Member model is at the heart of the application as it is connected the the main members page, linked by primary/foreign key relationships.

The Member model holds objects that are linked to the Member Models by a many to many relationship. This allows for admin to create a member also.

Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.

![Entity Relationship Diagram](docs/readme_images/erd-diagram.png)

### Security Tests 

* Security Methods were written into views.py - In the edit_member and delete_member functions an if statement was used to check that the member, author and user are stictly equal
to the member user and the author editing or deleting that page. Error messages are presented when user does not match.
* Different scenarios were carried out. Copying and pasting member **A's** edit url while member **B** was logged in. The function worked and displayed the message successfully.


![Unauthorized to edit](docs/testing/test_images/unauthorized-to-edit.png) 


* Within the create function the ability to create a page is not available if you are not logged in as it **does not** appear in the navigation bar and that is written within the base.html template code. 

![Nav Bar Not signed in](docs/readme_images/navbar.png)

* edit_member.html and create_member.html have authorization if statements written in and messages are displayed.  

![You are not logegd In](docs/readme_images/not-loggedin.png)







## The-Surface-Plane
### Design

### Colour-Scheme

The main color schemes for the website is a clean white background (#ffffff). Black font rgb(17, 17, 17), violet alert messages rgb (17, 17, 17), button text and hover affects to add a hint of color to the website. The Logo, Hero Image and Favicon have a colorful red thread through through out the website and I am lucky to have found matching content that represents the idea of the blog. WE ARE ALL COLORFUL PEOPLE AND WE NEED bright imagery in todays world. 

### Typography
I am using a default HTML Typography that is New Times Roman and it one of the safest Fonts to use. I really like New Times Roman it is simple clean and does not distract from the members
info and writings.

### Imagery

The Website logo was was taken from Adobe Stock and a license was purchased for up too 500,000 views.

The hero image was taken from Adobe Stock and a license was purchased for up too 500,000 views.

Default Member image taken from Adobe Stock and a license was purchased for up too 500,000 views.

## Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to make the Site Pagination.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://icons8.com/ and no license is required if I share this link with the whole world. 
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- Canva
  - The Diagram at the top of the page
- TinyPNG
  - This was used to compress the hero images for optimal load times

**Python Modules Used**

* Django Class and def function based views (Member List, Member Detail, Edit Member, Delete Member, MemberLike) - Used for the classes to create, read, update and delete
* Allauth - was used to integrate a set of Django applications addressing authentication, registration and account authentication.
* Alert Messages - Login, Log Out to ensure that the user understands what actions have taken place.


**External Python Modules**

*asgiref==3.5.2
*cloudinary==1.30.0
*dj-database-url==0.5.0
*dj3-cloudinary-storage==0.0.6
*Django==3.2.16
*django-allauth==0.51.0
*django-crispy-forms==1.14.0
*django-summernote==0.8.20.0
*gunicorn==20.1.0
*oauthlib==3.2.2
*psycopg2==2.9.5
*PyJWT==2.6.0
*python3-openid==3.2.0
*pytz==2022.6
*requests-oauthlib==1.3.1
*sqlparse==0.4.3



## Testing

Test cases and results can be found in the [TESTS.md](TESTS.md) file. This was moved due to the size of the file.

## Deployment

### Version Control

The site was created using the Github!

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site]()

## Credits 


