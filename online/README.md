# How to run client and server

```python
# Basically install packages run both client and server separately
# note: packages to install

flask
flask-socketio

pygame
requests
python-socketio
```

## How to run on pycharm

1. Open `Class-example-code` folder inside pycharm

2. Expand the `online` folder

3. Expand `client` > `src` > `main.py` (then `right click and select "run main"`), if it doesnt work yet ITS OKAY, follow next steps

4. `File` > `Settings` > `Project: Class-example-code` > `Python Interpreter` (Select your python interpreter)

5. Click on `+` sign to add packages to your project, and search for the packages above to download

6. Try step 3 again, aka. try running `main.py`

7. Now lets expand `server` > `application.py` (then `right click and select "run application"`)

8. Should work now, if not then ask mentor for help or try googling error message

## How to setup through terminal (Not needed if followed pycharm setup)

```python
# run this in your terminal with your preferred python enviroment
pip install requests pygame flask flask-socketio python-socketio

# If already have requirements installed follow steps below

# from root of dir(as in from inside Class-example-code folder)
# make two terminals

# terminal 1: for client terminal
cd online/client/src
python main.py

# terminal 2: for server terminal
cd online/server
python application.py
```
