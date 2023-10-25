# Regression Task


## Project Overview
-------------------
ML regression tasks are methods of supervised learning where we want to predict the target feature as precisely as possible given some data. Therefore, our target feature is a "continuous" feature in regression tasks.

In this tutorial, I'll apply some of the widely used machine learning regression algorithms like ```LinearRegression```, ```RandomForest```, and ```LightGBM``` using the wine-quality data set, where the task is to predict "the quality of wine" on a scale between 0 and 10.

## Directory Setup
------------------
The folder structure with the relevant scripts and files is demonstrated below:

```markdown
    ├── api
    │    ├── best_model.pkl
    │    ├── Dockerfile
    │    └── main.py
    ├── data
    │    └── winequality-red.csv
    ├── figs
    │    └── ...
    ├── src
    │    ├── Dockerfile
    │    ├── logger.conf
    │    └── main.py
    ├── deployment-ml-app.yml
    ├── docker-compose.yml
    ├── README.md
    └── requirements.txt
```

## Descriptions 
---------------

* **api**: This folder contains the following:
    * **best_model.pkl**: Stored best model based on model training.
    * **Dockerfile**: A Dockerfile to set up a Docker image with Python 3.10.
    * **main.py**: The script that handles the functionality of the API.

* **data**: This folder contains the Wine Quality CSV dataset. 

 * **figs**: This folder contains the plots created in the ```main.py``` script.

* **src**: This folder contains the following:
    * **Dockerfile**: A Dockerfile to set up a Docker image with Python 3.10.
    * **logger.conf**: A file that configures the logging settings for a Python application, specifying log message formatting, output handlers (in this case, console output), and the log level (INFO) for the root logger, ensuring that log messages are displayed with timestamps, log levels, and directed to the console.
    * **main.py**: The script that handles the whole functionality of the project.

* **deployment-ml-app.yml**: A YAML file defining a Kubernetes Deployment named `ml-deployment` with three replicas (adjustable if needed). It specifies a container named `ml-container` using a Docker image `regression-task-regression-task-project:latest` and exposes it on port 80. The deployment ensures that three identical instances of the container are running and manages their lifecycle.

* **docker-compose.yml**: A Docker Compose file defining two services, `api-service` and `src-service`. The `api-service` is built from the `Dockerfile` in the `api` directory, maps port 8000 from the host to the container, and depends on the `src-service`. The `src-service` is built from the `Dockerfile` in the `src` directory, mounts a volume for data, and runs a Python script, `main.py`, when the container starts.


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

### API Execution
-----------------

The model API can be executed using the following command under the `api` folder:

```
uvicorn main:app --reload
```

**Note:** The values provided in the request body should be either of type `float`, or `int`.

The API is provided with an endpoint `predict`:
 - **Endpoint**: ``http://localhost:8000/predict``
 - **Method**: POST
 - **Request Body**: as an example

```
{
  "fixed_acidity": 1.5,
  "volatile_acidity": 3.5,
  "citric_acid": 4,
  "residual_sugar": 5,
  "chlorides": 4.3,
  "free_sulfur_dioxide": 5.7,
  "total_sulfur_dioxide": 3.3,
  "density": 2.3,
  "pH": 5,
  "sulphates": 4.4,
  "alcohol": 7.9
}
```

 - **Response**:

 ```
 {
    "Predicted Wine Quality is": [
      4.34
    ]
 }
 ```

## Execution with Docker
------------------------

To simplify the deployment of the project, Docker containers can be used. **Note** that the model API will be launched when the Docker containers are built and run. Here's how to set up and run the project using Docker:

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

## Deployment to Kubernetes Cluster
-----------------------------------

To deploy your project using Kubernetes, the following steps can be applied:

1. **Install & Enable Kubernetes**: For an easy setup, download and install Docker Desktop for your system from the [Docker website](https://www.docker.com/get-started) and enable Kubernetes. 

2. **Clone the Repository**: Open a terminal and clone the repository:

   ```bash
   git clone https://github.com/kevorks/regression-task.git
   cd regression-task
   ```

3. **Apply the Kubernetes Deployment**: Use `kubectl` to apply the Kubernetes Deployment configuration defined in `deployment-ml-app.yml`. This will create the necessary resources on your Kubernetes cluster:

   ```bash
   kubectl apply -f deployment-ml-app.yml
   ```

4. **Monitor Deployment**: The deployment's progress can be monitored using the following command:

   ```bash
   kubectl get deployment ml-deployment
   ```

5. **Cleaning Up**: To delete the resources created by the deployment, including pods and the deployment itself, execute the following:

   ```bash
   kubectl delete -f deployment-ml-app.yml
   ```

## Author
--------------

* **Sevag Kevork** - *Author/Data Scientist* - [me@sevagkevork.net](https://github.com/kevorks)

