
# Fundamentals of AI and ML

## Introducing Basic AI and ML Concepts

**Definitions:**
- **Artificial intelligence** (AI, 1950s): An overarching term for enabling computers to **mimic human intelligence**. 
- **Machine Learning** (ML, 1980s): Enabling computers to learn on their own using data.
- **Deep Learning** (DL, 2010s): Using **neural networks** to learn without intervention.
- **Generative AI** (Gen-AI, 2020s): Generating new content to expand on the input data (training data).

### How Do Machines Learn?

- Models go through a 'training' stage to learn and reach an 'intelligent' state.

#### Foundation Models
- Large, general-purpose pre-trained models are known as **foundation models**. 
- They're the **blueprint** that you can adapt for various tasks by training on smaller, task-specific datasets via **fine-tuning**. 
- It costs **millions of dollars** to create a foundation model from scratch.

#### Large Language Models (LLMs)
- A foundation model for understanding and generating language
- Use DL (transformers) to analyze and predict word sequences
- They can process complex language patterns and nuances
- Advanced models have billions or even trillions of parameters (the model's internal settings)

#### Training Data
- Training data consists of **input variables** and **target variables**
- The goal is to use training data to create a well-trained model.
- The trained model should be able to apply trained data to make predictions on new unseen data (inferencing).
- For Gen-AI, the goal is to training generative AI models to generate content based on user requests and requirements.

#### Model Fit
- How well a model has learned and how accurately it can make predictions on new, unseen data.
- Patterns:
	- **Underfitting**: A model doesn't learn enough from the training set and performs poorly on both the training and test data.
	- **Overfitting**: A model learns the data too well, including the noise. It does well on the training set, but poorly on unseen data.
	- **Balanced**: A good middle ground where the model is complex enough to learn from the training data without being so complex that it overfits.
- Fairness and Bias
	- Unfair models can be driven by bias, like training data, historical data, or algorithms, which can lead to unfair predictions.

### Different Types of Machine Learning
- **Supervised Learning**: The model trains on data that has the input and the correct output (label).
	- **Classification**
		- **Multiclass**: The machine learns to categorize inputs into one of several possible classes.
		- **Binary**: The machine categorizes inputs into one of two possible outcomes.
	- **Regression**: Relies on predicting continuous values.
- **Unsupervised Learning**: The model trains on unlabeled input data to find patterns and groupings.
	- **Clustering**: Groups data into clusters based on similar features.
	- **Anomaly Detection**: Finds outliers in data.
- **Semi-supervised Learning**: The model is trained on a small amount of labeled data along with a large amount of unlabeled data.
- **Self-supervised Learning**: The model creates its own labels based on the data through tasks like predicting missing information.
- **Reinforcement Learning**: The model learns by interacting with an environment and receiving feedback in the form of rewards or penalties.
	- The algorithm receives feedback and adapts accordingly.

### Types of Data in AI Models
- **Structured Data**
	- **Tabular data**: Data is organized in clear structured format, typically in rows and columns.
		- Rows represent data points
		- Columns represent features
	- **Time-series data**: Great for forecasting and trend analysis.
- **Unstructured Data**: Doesn't have a clear structure; harder to analyze than structured data.
	- Text (emails, documents, social media posts)
	- Images and videos
	- Audio


## The Machine Learning Pipeline

- Stages
	- Generating data: Fetching, cleaning, preparing data
		- Fetching: Gather all the data related to patients from various sources
		- Cleaning: Ensure that the data is accurate and usable by handling:
			- Missing values: Filling in or removing null values
			- Inconsistent data: standardize data types (integers, floats), units of measurement, or time formats; standardize column names
			- Duplicates: Removing or merging duplicates or irrelevant data entries
		- Exploratory Data Analysis (EDA)
			- Identify patterns, correlations, and anomalies in data before any model training or analysis
		- Correlation Matrix: Allows you to quantify relationships between variables using a score between 1 and -1.
			- Positive numbers indicate a positive correlation.
			- Negative numbers indicate a negative correlation.
			- Zero indicates the lack of a linear relationship.
	- Training model: Train and tune model, evaluate model
	- Deploying model: Deploy to production, monitor/collect data/evaluate

### What is Feature Engineering?
- Feature Selection
	- Select the most relevant features
		- Having unnecessary features can slow the training process
		- The model might also learn from irrelevant data and become inaccurate
	  You can rely on domain experts or EDA for feature selection
- Feature Extraction
	- Deriving new features from existing variables
- Dimensionality Reduction
	- Simplifying the dataset into a lower dimensional space
	- You can use Principal Component Analysis (PCA) to combine features into smaller dimensions
- Categorial Encoding
	- Most ML models require numerical input
	- Convert the categorical values into numerical format
- Handling Scale
	- Normalization: Rescale the data to make the values between 0 and 1.
	- Standardization: Calculate the mean and standard deviation.

### Hyperparameters & Parameters
- Training a Model
	- Using a machine learning (ML) algorithm to learn patterns from a training dataset
	- The goal of enabling the model to predict outputs on new unseen data
- Parameters
	- Automatically learned from the data during training
	- The model keeps on adjusting them to minimize the error on the training data and improve predictions
	- Examples
		- Neural networks have weights and biases
			- Weights determine the importance of each feature
				- Higher weights have a higher impact on the prediction
			- Biases provide extra adjustment to fine-tune the model
				- They can set minimum and maximum thresholds
- Tuning a Model
	- Adjusting a machine learning model's configurations to improve its performance on a specific task
- Hyperparameters
	- Control the behavior of the learning algorithm
	- You configure them before training
	- Once set, they remain fixed during training
	- You can optimize them through hyperparameter tuning
	- They can impact the speed and quality of the learning process
	- Different algorithms have different hyperparameters
	- Learning Rate
		- Controls how quickly or slowly the model updates its weights and biases during training
		- A higher rate can result in frequent changes, which can cause the model to skip over the best solution
		- A lower rate is likely to be more accurate, but it will take longer to achieve the desired results
	- Batch Size
		- Refers to the number of training examples the model processes at one time before updating its weights
			- A larger batch size = more examples at once
				- Speeds up training
				- Might miss some details
			- A smaller batch size = fewer examples
				- Takes longer
				- More fine-tuned learning
	- Number of Epochs
		- Refers to the number of times the model will iterate over the entire training dataset. How many times will it study the data?
		- Too few epochs can lead to underfitting (where the model fails to learn enough)
		- Too many epochs can lead to overfitting (where the model memorizes the training data)
		- Proper tuning helps find a balance between overfitting and underfitting
		- To avoid overfitting, you can:
			- Set a maximum number of epochs for the training model
			- Define a patience period for early stopping, which indicates how many epochs to wait for an improvement.

### Metrics for Classification Models
- **True Positive**: Is supposed to be True and classified as True
- **True Negative**: Is supposed to be False and classified as False
- **False Negative**: Is supposed to be True but classified as False
- **False Positive**: Is supposed to be False but classified as True
- Imbalanced Datasets: One class is significantly more represented than the others
- Accuracy:
	- Measure the % of correct predictions out of the total predictions
	- Simple and intuitive, but can be misleading for imbalanced datasets
- Precision
	- Measure the number of predicted positives that were actually correct
	- Primarily used for
		- When you care more about the accuracy of positive predictions, such as fraud detection
		- Ideal for when false positives are costly
- Recall (Sensitivity)
	- Measure the proportion of actual positives that were correctly identified by the model
	- Primarily used for
		- When missing positives (false negatives) is costly
- F1 Score
	- Measure the harmonic mean of precision and recall
	- Gives a balanced measure for
		- When both precision and recall are important
		- Suitable for imbalanced datasets
- AUC-ROC
	- Area Under the Curve for the Receiver Operator Curve
		- Graphical curve showing a model's ability to distinguish between classes
		- Plots the curve for true positive rate (sensitivity) against the false positive rates

### Metrics for Regression Models
- Mean Absolute Error (MAE)
	- Tells you, on average, how far off your model's predictions are from the actual values
- Mean Squared Error (MSE)
	- Squares the errors before averaging them
	- Penalizes larger errors more than smaller ones
- Root Mean Squared Error (RMSE)
	- Square root the previous mean squared error
- $R^2$ (R-Squared)
	- Explains how well your model predicts outcomes using a specific input variable
	- Values range between 0 and 1
		- Closer to 0 means that knowing the input variable doesn't help much in predicting the output
		- Closer to 1 means that knowing the input variable yield in accurate predictions

### Fundamentals of ML Operations
- MLOps is a set of practices that manage the ML lifecycle, from development to deployment, and monitoring
- Automation and Standardization
	- MLOps allows you to automate the process across the ML lifecycle
	- This includes model development, packaging, and deployment. 
- Consistency and Reliability
	- Version control for both models and datasets
	- Ensures that the same model is deployed across multiple environments without any inconsistencies
	- Version control allows you to roll back if needed
- Continuous Deployment (CD) of Models
	- MLOps pipelines automatically handle testing, validation, and deployment of updated models into production.
	- MLOps can monitor the model in production to track performance
	- Metrics such as response time and accuracy are tracked to ensure that the model meets the requirements


## AWS Managed AI/ML Services and Applications

- **Amazon Rekognition**: Helps computers "see" and make sense of images and videos using ML.
- **Amazon Textract**: Automatically extracts any form of text from:
	- Scanned forms
	- Images
	- Tables and grids
- **Amazon Comprehend**: Natural language processing (NLP) service; can break down text via:
	- *Tokenization* splits sentences into individual words or phrases called *tokens*
	- *Parts of Speech* (PoS) figures out what role each word plays in a sentence

## AWS SageMaker
- A fully managed service for developers and data scientists
- Enables users to prepare, build, train, tune, and deploy ML models from scratch
- It supports version control
- It supports supervised, unsupervised, reinforcement, and deep learning
- Comprehensive toolbox for ML
	- It offers an IDE
	- A one-stop shop for building, training, and deploying ML models
		- Notebooks
		- Canvas
		- Data preparation and visualization
		- Collaboration tools
- ML Workflows
	- Designed to orchestrate and automate the entire machine learning workflow, from data preparation to model deployment
	- Supports versioning and tracking
	- Allows you to define and manage the steps involved in building, training, evaluation, and deployment
	- You can integrate AutoML as a step
		- Automates the model selection and hyperparameter tuning process
		- Allows you to quickly generate a model with minimal manual intervention
			- You upload your data
			- Specify the target variable (e.g., Is_Spam)
			- AutoML handles the rest