# Regression Task


## Project Overview
-------------------
ML regression tasks are methods of supervised learning where we want to predict the target feature as precisely as possible given some data. Therefore, our target feature is a "continuous" feature in regression tasks.

In this tutorial, I'll apply some of the widely used machine learning regression algorithms like ```LinearRegression```, ```RandomForest```, and ```LightGBM``` using the wine-quality data set, where the task is to predict "the quality of wine" on a scale between 0 and 10.

## Directory Setup
------------------
The folder structure with the relevant scripts and files is demonstrated below:

```markdown
    ├── data
    │    └── winequality-red.csv
    ├── figs
    │    └── ...
    ├── src
    │    ├── Dockerfile
    │    ├── logger.conf
    │    └── main.py
    ├── docker-compose.yml
    ├── README.md
    └── requirements.txt
```

## Descriptions 
---------------

* **data**: This folder contains the Wine Quality CSV dataset. 

 * **figs**: This folder contains the plots created in the ```main.py``` script.

* **src**: This folder contains the following:
    * **Dockerfile**: A Dockerfile to set up a Docker image with Python 3.10
    * **logger.conf**: A file that configures the logging settings for a Python application, specifying log message formatting, output handlers (in this case, console output), and the log level (INFO) for the root logger, ensuring that log messages are displayed with timestamps, log levels, and directed to the console.
    * **main.py**: The script that handles the whole functionality of the project.

* **docker-compose.yml**: A docker-compose.yml file that defines a service named regression-task-project, configures it to build an image using the Dockerfile located in the src directory, sets up volume mappings for data and source code directories, and specifies the command to run when starting the service, which is ```python3 main.py```.


## Execution without Docker
### Prerequisites
----------------

This project involves development using python `3.10` version. The necessary requirements needs to be installed to develop.

It is highly recommended setting up a virtual environment.

After setting up the virtual environment, you can install the requirements through following command:

```
pip install -r requirements.txt
```

### Execution
------------

To be able to run the script for training purposes, execute the following commands under the `src` folder:

```
python3 main.py
```

## Execution with Docker
------------------------

To simplify the deployment of the project, Docker containers can be used. Here's how to set up and run the project using Docker:

1. **Install Docker and Docker Compose**: Download and install Docker for your system by following the instructions on the [Docker website](https://www.docker.com/get-started).

2. **Clone the Repository**: Open a terminal and clone the repository:

   ```bash
   git clone https://github.com/kevorks/regression-task.git
   cd regression-task
   ```

3. **Build and Run the Docker Container**: In the root directory of the project, run the following command to build and start the Docker container defined in the `docker-compose.yml` file:

   ```bash
   docker-compose build
   docker-compose up
   ```

The commands above will create and start the container.

4. **Stop the Container**: To stop the container and remove it, run:

   ```bash
   docker-compose down
   ```

## Maintainers
--------------

* **Sevag Kevork** - *Maintainer/Data Scientist* - [me@sevagkevork.net](https://github.com/kevorks)

