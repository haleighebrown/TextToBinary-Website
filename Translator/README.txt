**********************************************************************
*                                                                    * 
*  README for pages app                                              *
*  By: Haleigh Brown                                                 *
*                                                                    *
**********************************************************************


	This app is responsible for the main bulk of the website. It includes all of 
views for making and showing off translations. TranslationListview associates with the 
scrolling list of translations available to a logged-in user. TranslationDetailView 
connects with the in-depth view available for every translation a logged-in user has 
made. TranslationDeleteView is where a logged-in user can choose to delete translations
that they have made. TranslationCreateView is where a new translation can be made 
and filled in so that depending on the users choice of 'Test to Binary' or 'Binary 
to Text' output can be correctly generated and sent to the user via 
translation_detail.html and translation_list.html. TranslationUpdateView is simply 
where users can go back and edit translations that they have already made without 
making a whole new one.

	For these last two views, it's necessary to ensure that the field author 
is automatically set the user so that users can not view each other's translations.
These views also have to refer to translator.py which is a python file that translates
Text to Binary or Binary to Text depending on what method is called. This makes it 
so that if the user puts in proper text or binary, depending on their choice,
the update and create views can output the correct translation.

	The associated URLs for the views can be found in urls.py and use <int:pk> 
to correctly direct the user to the edit, detail, and delete functions for a particular
translation. The models.py of this app supports the creation of translation by 
specifying the fields Input, Output, choice, date, and author. Finally, the testing portion 
of this app is largely dedicated to ensuring that the fields of translation are not left 
unchanged or empty. There are also tests to check that the translation model is vailed and
that the list of translations shows up correctly. 


