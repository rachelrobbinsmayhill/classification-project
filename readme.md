Classification Project - Telco Churn
Codeup - Innis Cohort - March 2022


## I. PROJECT OVERVIEW


#### 1.  Goal:
The goal of this project is to identify key drivers of churn for Telco, a telecommunications company, and make recommendations to reduce churn in order to increase customer retention, and ultimately increase revenue. Churn is another term for attrition and is represented by the percentage of customers who stop doing business with the company. Through machine learning and statistical analysis, predictions of future churn will be identified and recommendations for prevention will be made in order to improve customer retention.



#### 2. DESCRIPTION:

With an ever-competitive telecommunications market, it is vital to understand your customer base in order to prevent customer churn and maximize retention.  It is far less expensive to keep an existing customer than it is to acquire a new one for the long term when marketing costs are included. Therefore, it is important to identify drivers of churn in an effort to prevent attrition; thus, retaining current customers for the long term.  Ultimately, customer retention is important for maintaining and increasing profit.  This project will identify key drivers of churn for the Telco dataset and use modeling and statistics to identify ways to prevent churn in the future. Ultimately it will provide a recommendation that could be used by Telco or other customer-based service companies to maximize retention.


### INITIAL QUESTIONS:

The focus of the project is on decreasing customer churn and increasing retention, which can have a significant impact on revenue and entity reputation. Below are some of the initial questions this project looks to answer throughout the Data Science Pipeline.

##### Data-Focused Questions

- What types of customers do we have?
- What services do we offer?
- What customer base contributes the most to churn?
- What service types contribute most to churn?
- What is our total revenue?
- What amount of revenue is impacted by the overall churn?
- What amount of revenue is impacted by the customer base that churns the most?
- What amount of revenue is impacted by the service type that churns the most?

##### Overall Project-Focused Questions

- What will the end product look like?
- What format will it be in?
- Who will it be delivered to?
- How will it be used?
- How will I know I'm done?
- What is my MVP?
- How will I know it's good enough?


#### 3. DELIVERABLES:
README file - provides an overview of the project and steps for project reproduction.  
Draft Jupyter Notebook - provides all steps taken to produce the project.
Python Module File - provides reproducible code for acquiring,  preparing, exploring, & testing the data.
acquire.py - used to acquire data
prepare.py - used to prepare data
Report Jupyter Notebook - provides final presentation-ready assessment and recommendations.
.csv File - provides primary data used to make predictions & recommendations.




## II. DATA CONTEXT


## DATA DICTIONARY:

The final DataFrame used to explore the data for this project contains the following variables (columns).  The values of the Features, as well as their data types, are defined below:

|   Series / Column Name   |   Data Type   |    Description    |


To BE CONTINUED







## III. PROCESS:
This explains the steps taken through the Data Science Pipeline.  

Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver

#### 1. Planning
Review project expectations
Draft project goal to include measures of success
Create questions related to the project
Create questions related to the data
Create a plan for completing the project using the data science pipeline
Create data dictionary to define variables and data context
Draft starting hypothesis

#### 2. Acquisition


#### 3. Preparation
Features need to be turned into numbers
Categorical features or discrete features need to be numbers that represent those categories
Continuous features may need to be scaled to not compare different units like dollars to cm to age
#### 4. Exploration


#### 5. Modeling & Evaluation


#### 6. Delivery



## IV. MODULES:

Python Module File - provides reproducible code for acquiring,  preparing, exploring, & testing the data.
acquire.py - used to acquire data
prepare.py - used to prepare data



## V. REPRODUCIBILITY:

### Steps to Reproduce

You will need an env.py file that contains the hostname, username, and password of the mySQL database that contains the telco_churn database.

Store that env file locally in the repository.

Make .gitignore and confirm .gitignore is hiding your env.py file.

Clone my repo (including the acquire.py and prepare.py)

Import python libraries:  pandas, matplotlib, seaborn, numpy, and sklearn.

Follow steps as outlined in the README.md. And Churn_Work.ipynb

Run Churn_Report.ipynb to view the final product.
