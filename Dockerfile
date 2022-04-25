# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.10


RUN apt-get update && apt-get install build-essential postgresql-client binutils libproj-dev libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 gdal-bin binutils -y

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /cars

# set the working directory to /geoapi
WORKDIR /cars

# copy the current directory contents into the container at /geoapi
COPY requirements.txt requirements.txt

# install packages in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /cars/

# make script executable
RUN chmod +x entrypoint.sh

# entry point
RUN /cars/entrypoint.sh

#ENTRYPOINT ["entrypoint.sh"]
