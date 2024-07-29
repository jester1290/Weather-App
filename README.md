# Weather app
#### Video Demo:  <https://youtu.be/NUHWsH44K6c>
#### Description:
The application that I have created for my final project is a web-based application.The main purpose of this app is to let us see the temperature and weather of any city in the world at any given time. You can add a city to the homescreen of this app by entering the name of the city and then pressing the "Add" button. You can also delete the city which have been already added by pressing the "Delete" button right below it.

I have also considered the scenarios where the user should be provided with an error message. I have programmed this app to show appropriate error messages in the following cases:-
1. User does not provide an input and presses the "Add" button
2. User does not provide the name of a proper city as input and presses the "Add" button
3. User provides the name of a city that is already added and presses the "Add" button

The libraries that I have used are as follows:-
1. request
2. cs50
3. flask

I have made this app using the Flask framework and the api that I have used is openweathermap.org.

For styling I have used bootsrap and my own styling sheet as well.

The driving program is in app.py and is written in python. Inside the templates directory there are two .html file which are "weather.html" and "apology.html". Inside the static directory there is a .css file "styles.css" which is the stylesheet created by me. There also is a database "cities.db".

app.py:-
It contains the driving program and is written in python. It is a flask application. It defines only one route that is "/". You will be able to see a lengthy url , which is used to get the data from the api. After the user enters a valid city the value of the input is plugged into the url and the data that it returns is observed. It returns a list from dictionaries from which I have abstracted only the ones that are needed by me. I have designed the path description so as to accept both get and post requests.

When it is a post request, it means that the user have submitted a form. Which means that the user has either pressed the "Add" button or the "Delete" button. So I am checking which of the button has been pressed. If it is the delete button then the specific city is removed from the database using the de.execute() function and the user is directed to the homepage to see the updated list. If it is not the delete button then it must be the "Add" button.
So I would be checking for all possible errors that could happen due to the user's fault. First I am  checking if the user has entered the name of a city at all. If yes then show an appropriate error message. Otherwise, check if the name of the city entered is already added, if yes then show an appropriate error message. Otherwise, check if the name of the city is a valid one, if no then show an appropriate error message. Otherwise it would mean that there is no problem with the user input and so it would be finally added to the database and the user will be redirected to the homepage to see the updated list.

When it is a get request then the names of all the cities in the database are requested. Then I have looped over each of them retrieving the weather information. Then I am passing those values to "weather.html" and then rendering it.

weather.html:-
It is the homepage of my web-application. It is responsible for showing the weather data to the users. I have used two forms in this page. Into this template I am passing the weather information and showing them all together. I have made use of jinja syntax to make this file. I have styled it using bootstrap and my own stylesheet "styles.css".

apology.html:-
It is the page which is displayed when the user has entered an invalid input. It is designed to show the appropriate error message each time

styles.css:-
The css stylesheet which has been used to style both weather.html and apology.html.

cities.db:-
It is the SQL database I have used to store the name of each cities entered by the user. When the user deletes a city then that city is removed from this database. It has a table named "names",  which has two columns "id" and "city". The id column is the primary key and is of type INTEGER and the city column is of type TEXT.

THE END
THANK YOU














