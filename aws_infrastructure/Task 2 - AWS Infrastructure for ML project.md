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

 + Redução de 54% no TCO (Total Coast Ownership)
 + Fornece containers otimizados de frameworks como Tensorflow, capazes de gerar uma redução de até 90% no custo de treinamento
 
### Tuning
HPO - Hyper parameter Optimization
Optimiza automaticamente os hiperparâmetros desde a parte da infraestrutura (mpaquinas rodando o treinamento) até a  distribuição do processamento do treino.

### Model Management
Salva os artefatos do modelo na S3. Modelo: Container + artefato do S3. 
O sagemaker sobe o container e, se existir, puxa os artefatos da S3. A partir daí, o modelo está pronto para realizar inferências.

### Sagemaker in Dev
 + Possível desenvolver em instâncias do Jupyter Notebooks gerenciadas pelo Sagemaker
 + Notebooks dentro do ```Sagemaker Studio``` (IDE) online com o Jupyter Lab integrado com todos os outros componentes do Sagemaker - gráficos de erro ao longo do treino
 + ```Sagemaker Debuging``` - Salva todos os estados intermediários conforme o modelo está sendo treinado. Permite debugar o comportamento da aprendizado e, se for o caso, interromper o treinamento para não consumir tempo da equipe e, principalmente, não consumir custo de treinamento. Permite a criação de regras para emitir alertas de monitoramento e interromper a execução do treinamento de forma automatizada.
 
### Ground truth
É um serviço de rotulação de datasets. Utiliza rolutadores humanos, mas seu diferencial está nas técnicas de rotulação automática, como o Active Learning. Utiliza os dados já rotulados para criar um modelo preditivo e rotular os dados não rotulados com o valor predito, caso a métrica da predição seja satisfatória.

### Auto Pilet
Auto ML - o usuário indica referencia o dataset na S3 (dados tabulares) e a coluna de target no dataset. A partir daí, o Auto Pilet executa todo o processo de análise dos dados e treinamento do modelo. Ele usa vários algoritmos e otimização de hiperparâmetros e, ao final entrega o melhor modelo obtido. 
Contudo, ele não é caixa preta: é possível visualizar o Notebook que gerou o respectivo modelo.

### MLOps - Model Monitor
Etrutura de pipelines de ML em Produção.
Após o Deploy, o comportamento do modelo precisa ser monitorado. Analisa o dataset de treino e o compara com os dados novos. Se o comportamento dos dados atuais diferem muito dos dados de treino, é um forte indicativo para a realização de retreino.
 + Pipeline de Treinamento
 + Pipelne de Deploy
 + Pipeline de Retreinamento
