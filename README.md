# CSC333-Brute-Force-Chrome-Extension
A Brute Force Password Cracker that was added to the Web of Trust Chrome Extension

Steps to Run the modified WoT extension:

To run the Django server,ensure that django is installed. Use an installation tool like
pip to download Django. Once that's installed, in command prompt, navigate into the 
"DjangoServer" folder andexecute the "manage.py" file with the option "runserver". 
For example in windows:
".../DjangoServer  manage.py runserver"
Once that is running, open up Google Chrome. Navigate to the Extensions Manager.
Turn on Developer mode, and install the "chrome-master" folder. In order for this to 
communicate with the Django Server, another extension "Allow-Control-Allow-Origin" needs to
be installed and turned on. This will allow chrome to ignore it's single origin policy. 
It can be downloaded t "https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi"


How to the password cracker:

in the top right, click the little WoT ring and a drop-down menu will appear. On the 
bottom of the menu is the password cracker. Type in a password and click the "Crack" button
 
