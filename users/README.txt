**********************************************************************
*                                                                    * 
*  README for users app                                              *
*  By: Haleigh Brown                                                 *
*                                                                    *
**********************************************************************


	This app is responsible for keeping track of the users that sign up for
the main application. It's admin.py supports the creation of custom user admin
and it's models.py supports the creation of custom users that have the additional fields 
of age and name. Along with this, its views.py includes a SingUpView since the sign 
up form has to include the custom user parameters.This app's urls.py connects this 
SignUpView to the main application.The testing for this app is to ensure that 
custom users get created correctly and that new users are sent to the correct template 
when they wish to sign up.