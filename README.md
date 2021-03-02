# Ifood ML Engineer Exercise
An automated ML model training process using Docker Compose

## Task 1: ML model serving
There are two goals for this task:
### Part I: Create an automated ML model training process
+ *Problem description:* House Price Prediction
+ *Metrics:* Root Mean Squared Error (RMSE)
+ *Language:* Python
+ *Pipeline orquestration:* Docker Compose

#### Prerequisites:
Must have Docker Compose installed in the host.

#### Installation:
Download the project by cloning the Git repository: 

```https://github.com/TBSantana/Ifood_Exercise.git```

#### Usage:
1. In the terminal, go to the main project's directory and execute the following code to create the images:

```docker bluid -t clean_image -f clean_data/Dockerfile .```

```docker bluid -t transform_image -f transform_data/Dockerfile .```

```docker bluid -t train_image -f train_model/Dockerfile .```

```docker bluid -t predict_image -f app_prediction/Dockerfile .```

2. Finally, execute the docker comand to run the ML pipeline:

```docker-compose up```

#### Make predictions
At the end of this pipeline, the prediction service will be running in the host at this endpoint: 

```http://localhost:5000```


### Part II: Create a Rest API documented with Swagger that serves a ML model predictions
The REST API has been created using the ```FastAPI```, that is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 
It also includes an interactive API documentation (Swagger). 
How to access the online documentation:
+ Main documentation - <host_address>/docs. Ex.: ```http://127.0.0.1:8000/docs```
+ Alternative documentation - <host_address>/redoc. Ex.: ```http://127.0.0.1:8000/redoc```

## Task 2: AWS infrastructure
*Description* - Propose an AWS architecture to serve a solution for the previous task.

## Task 3: Coding challenge (Bonus)
