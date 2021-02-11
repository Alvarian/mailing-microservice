FROM python

# Upgrade pip
RUN pip install --upgrade pip

## make a local directory

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /app/src

# now copy all the files in this directory to /code
COPY . ./

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# Define our command to be run when launching the container
CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload