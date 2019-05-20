# News Highlight
News highlight is an application that gives a user an easy time locating the kind of news they
want to follow up on by the category or by the source

#### Author
*Bright Mukonesi*
#### Date made
*17/5/2019*

## Technologies used
1. Python3.7
2. Html
3. Bootstrap
4. Python extensions
5. Flask

## Using the application
* you can view the live demo at https://bnewshub.herokuapp.com/
* You require a minimum python version 3.6 to run the application on your local machine
* clone the repository and get to install flask using _git clone https://github.com/Brightmuk/News-highlight_
* Run the application using _./start.sh_ command
* Click on the link on the terminal as you press ctrl and use the application in the browser

##### Creating a virtual environment
* sudo apt-get install python3.6-venv
* python3.6 -m venv virtual
* source virtual/bin/activate
##### Installing dependencies
* pip install -r requirements
##### Running Tests
* python -m unittest tests/test_models.py
##### Running in development
* python run.py
* Open the app on your browser, by default on 127.0.0.1:5000.

* Deploying to heroku
Make sure you have requirements.txt
# should be in virtual
* pip freeze > requirements.txt
* create a Procfile with the following content
* web: gunicorn 'app:create_app()' --access-logfile - --error-logfile -
* If deploying for the first time, make sure you have heroku cli installed then create app by running
heroku create appname
* Make sure you have committed all changes then run
* git push heroku master

# License
### GNU GENERAL PUBLIC LICENSE ###
                       _Version 3, 29 June 2007_

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                     Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.
_For more info about the license visit the site at this link_
https://choosealicense.com/licenses/gpl-3.0/
