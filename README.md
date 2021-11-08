# Seefood part 3: Flask tutorial

## Set up

1. Clone the repo.

    `git clone https://github.com/nikhil-ajjarapu/convergent-seefood-flask.git` 


2. Navigate to the repository directory within the terminal.

    `cd convergent-flask`

3. Run these commands to set up a virtual environment with pip (full documentation + troubleshooting [here](https://flask.palletsprojects.com/en/2.0.x/installation/)):

    `python3 -m venv venv`

    `. venv/bin/activate` (just need to run this after creating the venv once)

    `pip install -r requirements.txt`

4. Run the app:

    `flask run`

## Test the server locally

1. Start the flask server with `flask run`.
2. Open up a new terminal in the same folder and try these CURL commands to hit your server with a test image:

    `curl -v -F filename=test_data/dinesh.jpg -F upload=@test_data/dinesh.jpg http://localhost:5000/api/uploadPicture`

