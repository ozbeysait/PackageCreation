# Create a pip package and use it another project

This project creating pip package.


## Set up your LICENCE, MANIFEST.in, README.rst, setup.cfg and setup.py files for your pip package

LICENCE<br>
![image](https://user-images.githubusercontent.com/41578459/198900133-806c57bd-ec54-42d7-a313-7a26e0d3daf1.png)

README.rst<br>
![image](https://user-images.githubusercontent.com/41578459/198900190-05ea3df1-93cc-4640-843e-73c922e8ace0.png)

MANIFEST.in<br>
![image](https://user-images.githubusercontent.com/41578459/198900149-84ce4edf-17c2-481f-88e9-65d2036e6205.png)

setup.cfg <br>
![image](https://user-images.githubusercontent.com/41578459/198900208-31297c37-6492-4a58-a08e-772f99eb1f12.png)

setup.py <br>
![image](https://user-images.githubusercontent.com/41578459/198900217-c65302ba-cf79-4bf6-9bfb-6a967f94359e.png)

## Create your pip package

STEP 1. <br>
```
py setup.py sdist
py setup.py bdist_wheel
```

STEP 2. <br>
install twine and check your files, then fix them <br>
```
pip install twine
twine check dist/*
```

STEP 3. <br>
Your package ready under dist directory, 'django_books-2.0-py3-none-any.whl' <br>
![image](https://user-images.githubusercontent.com/41578459/198900502-fe5175f6-0adc-41a1-9372-7cc0df0b08be.png)


## Use your pip package in sample project
Create a new sample project and move 'django_books-2.0-py3-none-any.whl' under directory <br>
![image](https://user-images.githubusercontent.com/41578459/198900578-3607583d-cf45-4333-8202-eb7dd08adef2.png)

Run this command and install your package <br>
```
pip install .\django_books-2.0-py3-none-any.whl -f ./ --no-index --no-deps
```

And apply this steps <br>
![image](https://user-images.githubusercontent.com/41578459/198900614-223d9932-8791-40f2-8ad5-d518d25d68b4.png)

DONE!

## Setup Full Repo
virtualenv -p python3 /.<br>
source bin/activate<br>
git clone https://github.com/ozbeysait/PackageCreation<br>
cd PackageCreation<br>
pip install -r requirements.txt<br>

## Runserver
```
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```
