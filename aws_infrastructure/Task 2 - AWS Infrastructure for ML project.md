# AWS Infrastructure for ML

The proposed AWS Infrastructure for this project is as follow:

<img src = "images/AWS Infra.png">

This model consists on up all the code under the AWS Sagemaker Management and storage the pipeline artefacts on the AWS Simple Cloud Storage (S3). But why? 

*Amazon Simple Storage Service (Amazon S3)* is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics.

*Amazon Sagemaker* is a managed service to support the end-to-end ML pipline from labeling, training, testing, deploying and monitoring the model in Production. 

Since AWS Sagemaker offers a lot of products to support ML automated pipeline, I will focus this discussion on this platform.

### Sagemaker advantages
 +  Collect and Prepare Training Data
    +  Security and Privacy 
    +  Feature Store 
    +  Data Labeling 
    +  Data Processing at Scale 
 +  Build Models
    +  One-click Jupyter Notebooks
    +  Built-in Algorithms
    +  Pre-Built Solutions and Open Source Models 
    +  AutoML 
    +  Optimized for Major Frameworks (Tensorflow, Pytorch, MXNet, Keras, etc)
+ Train and Tune Models
    + Experiment Management and Tracking
    + Managed Spot Training (**reduce training costs by up to 90%**)
    + One-Click Training 
    + Distributed Training 
+ Deploy Models to Production
    + CI/CD support
    + Continuously Monitor Models 
    + Integration with Kubernetes 
    + Human review 
    + One-Click Deployment 
 + **Reduction of 54% on TCO (Total Coast Ownership)**

**Note:**
If the project delivered on Task 1 were a full ML pipeline, the colected training data would be storaged on AWS S3 as well.

