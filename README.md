An automated ML model training process using Docker Compose.



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

#### Project execution:
1. In the terminal, go to the main project's directory and execute the following code to create the images:

```docker bluid -t clean_image -f clean_data/Dockerfile .```

```docker bluid -t transform_image -f transform_data/Dockerfile .```

```docker bluid -t train_image -f train_model/Dockerfile .```

```docker bluid -t predict_image -f app_prediction/Dockerfile .```

2. Finally, execute the docker comand to run the ML pipeline:

```docker-compose up```

At the end of this pipeline, the prediction service will be running in the host at this endpoint: ```http://<host_address>:5000```


### Part II: Create a Rest API documented with Swagger that serves a ML model predictions
The REST API has been created using the ```FastAPI```, that is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 
It also includes an interactive API documentation (Swagger). 
How to access the online documentation:
+ Main documentation - <host_address>/docs. Ex.: ```http://<host_address>:5000/docs```
+ Alternative documentation - <host_address>/redoc. Ex.: ```http://<host_address>:5000/redoc```

#### Usage examples
1. Access the API documentation at ```http://<host_address>:5000/docs``` and click on the ```predict``` POST method

![prediction](/images/usage_examples1.png)

2.  Click on ```Try it out``` and paste the json below in the "Request body". Then, click on ```Execute```
```
{
  "suburb": "Elsternwick",
  "rooms": 4,
  "typeH": "h",
  "postcode": "3185.0",
  "address": "15 Murray St",
  "buildingArea": 204.0
}
```

![execute](/images/usage_examples2.png)

The related predicted price will show up in the ```Response body```, like the following image:

![response](/images/usage_examples3.png)

## Task 2: AWS infrastructure
*Description* - Propose an AWS architecture to serve a solution for the previous task.

## Task 3: Coding challenge (Bonus)
TODO
