# Tinder clone app

This is a simple clone of Tinder’s mobile application. It allows users to like and dislike other users and see their list of matches.

### Features:

1. Users will be able to create an account and login with their credentials.
2. A list of other users will available for each user to like or dislike.
3. Users will be able to see a list of their matches.
4. The app also allows users to update their profile information.

This app was built using ReactJS for the front-end side and Python Flask for the backend side.

The app builds on top the following Hasura APIs:
* Hasura Data API
* Hasura Auth
* Hasura File APIs
* Postgres instance in the cluster

 
## Instructions on using the app
1. Go to this URL:
[Tinder App](https://ui.acrophobia73.hasura-app.io/)

You will see the Login/Signup page. Enter your the Username and Password for creating a new account or logging in.

![Login/Signup page](https://drive.google.com/file/d/1HTkE47tApCKxW3BTimlyWfZMc-bDm7BK/view?usp=sharing)

2. Create Account Page

This page will appear if you are creating a new account for the app. Users already having their accounts for the app will not see this page. On this page, users need to enter data in the corresponding field and upload their profile picture.

![create account](https://drive.google.com/file/d/1TcBpkibLf8NQRxuMulhYP0KBorQLxZ98/view?usp=sharing)

3. Suggestions Page

After logging in, the users will be taken to Suggestions page. On this page, users will see other users they can like or dislike based on their preference. There are two buttons at the bottom of the page and two button at the top. Clicking on the bottom right button indicated a “like” whereas clicking on the bottom left indicates a “dislike”. Clicking on the top right button, takes the user to his/her Matches page. Clicking on the top left, takes the user to his/her Profile page.

![suggestions page](https://drive.google.com/file/d/1Hws-gm2X7LR5jIKfCDOb_vwi8ZcYRbVR/view?usp=sharing)

4. Matches Page

When a user clicks on the top right button, he/she is taken to his/her Matches page. This page shows a list of users with whom he/she matched and liked. After viewing the users list, the user can navigate back to the Suggestions page by clicking on the back button on the top left side of app.

![matches page](https://drive.google.com/file/d/1k6JJByXEXoqj-RBMConta8OPxk7tKGNH/view?usp=sharing)

5. Profile Page

The users can go to their profile page by clicking on the top left button on the Suggestions page.

![profile page](https://drive.google.com/file/d/1mhI05v1uhkLl0-1LLYxmYdfTDRJ-1HNP/view?usp=sharing)


On this page, users can see their profile picture, name and age. Clicking on the settings button, takes the users to their Settings page. Settings page allows the users to update the information for the city field and enter the gender of the other users they are looking for. After updating the information for these two fields, users can click on done button to go back to the Profile page. Users can also logout of the app and delete their app account as well.

![settings page](https://drive.google.com/file/d/1TYcfcwB1RA4n5G3L5jyc3JS8RAbHDYMa/view?usp=sharing)

Back on the Profile page, users can click on the Edit Info button and go to their Account page to update their profile information. After updating their profile information, the users can click on the Update or Cancel button to navigate back to the Profile page.

![profile page](https://drive.google.com/file/d/1mhI05v1uhkLl0-1LLYxmYdfTDRJ-1HNP/view?usp=sharing)

If the users are done using the Profile page, they can navigate to the Suggestions page by clicking on the top right button.


## Prerequisites
* We will use Node.js along with the express framework to build our server. Ensure that you have Node installed on your computer, do this by running `node-v` in the terminal. If you do not have Node installed you can get it from https://nodejs.org

* Before you begin, ensure that you have the latest version of the `hasura cli` installed. You can find instructions to download the `hasura cli` from [here](https://docs.hasura.io/0.15/manual/install-hasura-cli.html)


## Future Scope
Currently, our app is quite simple but we want to improve it further by implementing few changes in the future. We aspire to refine its UI further and eventually add few more features to it.

