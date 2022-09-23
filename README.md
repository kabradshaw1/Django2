It's recommending that you work in a virtual invoronment when workign with django.  Not sure why.  
I tried to make a virtual invironment by typing <mkvirtualenv myapp>. I just got an error saidly.
I ended up creating a new invironment with the command <python -m venv venv> (second venv here appears to be a name).  
I then use the command <venv\Scripts\activate> to move 
into the virtual invironment.  Ithen installed django onto this vitrual invironment with <pip install django>
Tutorial is now telling me to exit my inv with <deactivate>
I left this inv, and can tell becaues (venv) is no longer to the left of my directory in the cmd.  Turns out that
<venv\Scripts\activate> only works in the directory you used <python -m venv> in.
<django-admin startproject name> is the next cammand I put in the cmd, and it created the folder that had the manage.py.  I used cd to get into that directory

Next we make an app.  I'm checking to make sure that I'm in the correct directory (with manager.py), and that I'm in my virtual console.  in the cmd <python manage.py startapp name> I named mine myapp.  We created a file in the myapp folder called urls.py

In the myapp/urls.py I added from django.urls import path.  I then added urlpatterns = [path('', views.index, name='index')].  He pointed out that the empty quotes implies we are on the home page, but that I could add '/download' as an example, and I can add as many pages as I want. We put from . import views

We then went to views, and put in def index(request): pass.  He then added from django.http import HttpResponse to the top.  We changed pass to return HttpResponse('<h1>hi<hi>')

We then ran python manage.py runserver in the cmd. I
got an error, so I used ctrl c and then did their suggested mython manage.py migrate command.  tried putting the ip address in the browswer, and it didn't load.

Went to test/urls.py added include to the imports from django.urls and tried the page again, and it loaded.  Hope I didn't miss a step here.

We made a folder in the root directory called templates

Went to test/test/setting.py and went to TEMPLATES and found the 'DIR' property and put [BASE_DIR, 'templates"] in the list already provided.

Made an index.html file in the templates folder and put some example text in it.

went to myapp/views.py and changes the return to render(request, 'index.html')