# Your Community Blog

Your Community Blog consists of Member Profiles that have a Role in their Community. That wish to have an About Me Page describing what the do and how they engage with their community. 
This is a great template for other organizations to use for their members. 

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

This webiste is?

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over three weeks.

All projects were assigned to epics, prioritized under the labels. They were assigned to sprints and story points according to complexity & priority. It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here] and can be viewed to see more information on the project cards. 

![Kanban image](docs/readme_images/kanban.PNG)

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

**EPIC 2 - Stand alone Pages**

As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist

As a developer, I need to implement a 500 error page to alert users when an internal server error occurs

As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views

As a Site User, I would like a "About" page so that I can view information on this website

**EPIC 3 - Authentication Epic**

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling

As a Developer, I want to add a Register Page in the Header

As a Developer, I want to add a Sign In Page in the Header

As a Developer, I want to add a Log Out Link in the Navigation Bar- only while logged in.

**EPIC 4 - Member Page**

As a Member, I want to be able to create a new Member Page to display myself as professionally skilled. It will have a comment section.

As a Member, I want to be able to edit a my Member Page when updates are needed.

As a Member, I want to be able to delete my Member Page when it is no longer used.

As an Admin user, I want to be able to delete a Member Page when it is no longer used.

**EPIC 5 - Home Page**

As a Developer, I want to add thumbnails which will display the Member picture.

As a Developer, I want to add Member Blurb/Short Description

As a Developer, I want to add Expertise/Profession

As a Developer, I want to add Email ID/Contact Me

As a Developer, I want to add Go to Member Button

As a Developer, I want to add Like/Heart Button

As a Site User, I would like to be able to view other Members and see what skill they have to offer

Possible inclusion: As a Developer, I want to add Email Button which will open default email compose me page and add the email in 'To' Section

**EPIC 6 - Deployment Epic**

As a developer, I need to set up whitenoise so that my static files are served in deployment

As a developer, I need to deploy the project to heroku so that it is live for customers

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

![Navbar](docs/readme_images/navbar.PNG)

![Hero Image]()

![Welcome Section]()

![Find Us]()


``USER STORY - As a developer, I need to create the footer with social media links and contact information``

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a Twitter and Facebook link so that users can follow the Your Community blog on social media'

![Footer]()

``USER STORY - As an administrator, I want to be able to create a new member when we update the site, and or want to add a new member``

Implementation:

**Create Member Page**

Create member page was implemented to allow staff users to create new members via the UI without having to use the backend admin panel.

![Create Member]()

``USER STORY -As a user, I would like to be able to view member ``

Implementation:

**View Member Page**

A member page has been implemented to allow users to see the current active members.

![View Members](d)

``USER STORY -As an admin I want to be able to edit a member when updates are needed``

Implementation:

**Edit Members Page**

On the manage members page a button was added to allow staff members to edit a members page when changes need to be made.

![Edit Member]()

``USER STORY -As an admin, I would like to receive feedback when a member need to be deleted ``

Implementation:

**Toasts**

Custom toasts were added on successful creation and deletion of members which display success messages to the user to enable them to see that the action completed successfully.

![Member Toasts](d)

``USER STORY -As admin, I want to be able to delete a member when page is used``

Implementation:

**Delete Member Page**

On the manage/admin members page, a delete button has been implemented that will take staff users to a confirmation page to allow them to delete a members. This will allow staff to delete members when they are no longer needed

![Delete Member]()



Implementation:

**Create Member page**

![]()


Implementation:

**Edit Member Page**

On the manage member page an edit button is present that allows the user to direct to a form and update their member page when required. This will allow the user to easily manage their own member page.

For the admin, they can also delete Member from the admin page, even if they did not create it. 


``USER-STORY - As a user, I would like to receive feedback when I create a member or edit one so I know it was completed successfully``

Implementation:

**Toasts**

Custom toasts were implemented on the successful creation and editing of member. 


``USER-STORY - As an admin, I want to be able to search a member by reference to save time searching``

Implementation:

**Searchbox**

A search box was added to the admin member page that is only visible to admin users. This will allow the admin to easily access members page. 

[Search Boxes](docs/readme_images/search.PNG)

``USER-STORY - As a user I would like to delete a member when I no longer require it``

Implementation:

**Delete member Page or popup/ confirmation**

A delete button was added to the manage member pages that will allow customers to delete their member page should they no longer require it.

The administration will also have the abaility to delete any member through the UI as well.

![Delete Member]()

Favicon
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon]()

**Error Pages**

``USER STORY - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist``

Implementation:

**404 Page**

As a developer, I need to implement a 404 error page to redirect users to

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need  of the browsers back button.

``USER STORY - As a developer, I need to implement a 403 error page to alert users when accessing a page/view that they do not have permission to view``

Implementation:

**403 Page**

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete or access pages that are restricted. 

This covers:

* Create Member - Only authorized to staff
* Edit Member - Only authorized to staff
* Delete Member - Only authorized to staff
* Edit Member - Full CRUD TO MEMBER

``USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs``

Implementation:

**500 Page**

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

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

- Home page


![Home Page]()


- Signup page


![Sign up Page]()

- Log in

![Login Page]()

- Log Out

![Logout Page](d)

- Create Member 

![Create Member]()

- Edit Member 

![Edit Member]()

- View Member 

![View Member]()


- Manage Member

![Manage Member]()

- Delete Member 

![Delete Member]()

- 404 Error 

![404 Error]()


**Differences to Design**

On the Members page, the original wireframe was to display the members in a complete linear format but on larger screens this caused a lot of un-neccessary white space on smaller items like drinks and sides. A change was made to have the drinks and sides sit side-by-side on larger screens and stack as originally planned on mobiles.

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The Member model is at the heart of the application as it is connected the the main members page, linked by primary/foreign key relationships.

The Member model holds objects that are linked to the Member Models by a many to many relationship. This allows for admin to create a member also.

Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.

![Entity Relationship Diagram](docs/readme_images/erd.JPG)

### Security


## The-Surface-Plane
### Design

### Colour-Scheme

The main color schemes for the website is a clean white background (#ffffff). Black font rgb(17, 17, 17), violet alert messages rgb (17, 17, 17), button text and hover affects to add a hint of color to the website.

### Typography



### Imagery

The Website logo was was taken from Adobe Stock and a license wsa purchased for up too 500,000 views.

The hero image was taken from Adobe Stock and a license wsa purchased for up too 500,000 views.


## Technolgies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to make the custom slider on the members page change and the bootstrap date picker.
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
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- Canva
  - This was used to create the logo in header 
- TinyPNG
  - This was used to compress the hero image for optimal load times

**Python Modules Used**

* Django Class and function based views (Member List, Member Detail, Edit Member, Delete Member, MemberLike) - Used for the classes to create, read, update and delete
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

Test cases and results can be found in the [TESTING.md](TESTING.md) file. This was moved due to the size of the file.

## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

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


