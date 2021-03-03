# Machine Learning Engineering Project

This is the project of an automated ML model training process using Docker Compose.

## Index

 [Task 1 - ML model serving](#task-1---ml-model-serving) 

  * [Part I: Create an automated ML model training process](#part-i---create-an-automated-ml-model-training-process)

    * [Prerequisites](#prerequisites)

    * [Installation](#installation)

    * [Project execution](#project-execution)

  * [Part II: Rest API documentation and Swagger](#part-ii---rest-api-documentation-and-swagger)

[Task 2 - AWS infrastructure](#task-2---aws-infrastructure)

[Task 3 - Coding challenge (Bonus)](#task-3---coding-challenge-bonus)

[Project improvements](#project-improvements)



## Task 1 - ML model serving
There are two goals for this task:

### Part I - Create an automated ML model training process
+ *Problem description:* House Price Prediction
+ *Metrics:* Root Mean Squared Error (RMSE)
+ *Language:* Python
+ *Pipeline orchestration:* Docker Compose


<details><summary>Click here to see the details of the installation process.</summary>
<p>

#### Prerequisites
Docker Compose must be installed on the host.

#### Installation
Download the project by cloning the Git repository: 

```https://github.com/TBSantana/ML_Automated_Pipeline.git```

#### Project execution
1. In the terminal, go to the main project's directory and execute the following code to create the Docker images:

```docker bluid -t clean_image -f clean_data/Dockerfile .```

```docker bluid -t transform_image -f transform_data/Dockerfile .```

```docker bluid -t train_image -f train_model/Dockerfile .```

```docker bluid -t predict_image -f app_prediction/Dockerfile .```

2. Finally, execute the docker comand to run the ML pipeline:

```docker-compose up```

At the end of this pipeline, the prediction service will be running in the host at this endpoint: ```http://<host_address>:5000```

</p>
</details>

### Part II - Rest API documentation and Swagger
The REST API has been created using the ```FastAPI```, that is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 
It also includes an interactive API documentation (Swagger). 
How to access the online documentation:
+ Main documentation - <host_address>/docs. Ex.: ```http://127.0.0.2:5000/docs```
+ Alternative documentation - <host_address>/redoc. Ex.: ```http://127.0.0.2:5000/redoc```

<details><summary>Click here to see a usage example.</summary>
<p>

#### Usage example
1. Access the API documentation at ```http://<host_address>:5000/docs``` and click on the ```predict``` POST method.

2.  Click on ```Try it out```, copy the following json and paste it in the "Request body" section. Then, click on ```Execute```.

The related predicted price will show up in the ```Response body```.

![prediction](/images/usage_examples1.png)

```
{
  "suburb": "Elsternwick",        # The suburb where the house is located
  "rooms": 4,                     # The number of rooms
  "typeH": "h",                   # The type of the house
  "postcode": "3185.0",           # The postal code of the house
  "address": "15 Murray St",      # The address of the house
  "buildingArea": 204.0           # The size of the house
}
```

![try it out](/images/usage_examples2.png)

![execute](/images/usage_examples4.png)

![response](/images/usage_examples3.png)

</p>
</details>

## Task 2 - AWS infrastructure
*Description* - Propose an AWS architecture to serve a solution for the previous task.

See the details of the proposed infrastructure [here](https://github.com/TBSantana/ML_Automated_Pipeline/blob/master/aws_infrastructure/Task%202%20-%20AWS%20Infrastructure%20for%20ML%20project.md).

## Task 3 - Coding challenge (Bonus)
Sadly there were no time to deliver this part of the exercise.

## Project improvements
As can be seen, this project is pretty simple. It works, but do not covers the entire ML pipeline. The time was short, so I had to focus on have a deliverable. The improvements to be made are as follows:
+ Storage the training set on some database
+ Do a deeper analysis on the raw data
+ Create more new features during the transformation step
+ Correct the cqtegorical encoding, witch does not follows the best practices of ML
+ Select more algorithms during the training step
+ Develop a Tuning step and select the model that presents the best performance
+ Add a logging feature to monitoring the containers execution
+ Create a script do automatize the Docker images building

