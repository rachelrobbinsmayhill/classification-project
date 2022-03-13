Classification Project - Telco Churn -
Codeup - Innis Cohort - March 2022
 
===
 
Table of Contents
---
 
* I. [Project Overview](##-I.-project_overview)<br>
[1. Goals](#1-goal)<br>
[2. Description](#2-description)<br>
[3. Initial Questions](#3initial-questions)<br>
[4. Formulating Hypotheses](#4-formulating-hypotheses)<br>
[5. Deliverables](#5-deliverables)<br>
* II. [Data Context](#ii-data-context)<br>
[1. Data Dictionary](#1-data-dictionary)<br>
* III. [Data Science Pipeline Process](#iii-data-science-pipeline-process)<br>
[1. Project Planning](#1-plan)<br>
[2. Data Acquisition](#2-acquire)<br>
[3. Data Preparation](#3-prepare)<br>
[4. Data Exploration](#4explore)<br>
[5. Modeling & Evaluation](#5-model--evaluate)<br>
[6. Product Delivery](#6-delivery)<br>
* IV. [Modules](#iv-modules)<br>
* V. [Project Reproduction](#v-reproducibility)<br>
 
 
 
## I. PROJECT OVERVIEW
 
 
#### 1.  GOAL:
The goal of this project is to identify key drivers of churn for Telco, a telecommunications company, and make recommendations to reduce churn in order to increase customer retention, and ultimately increase revenue. Churn is another term for attrition and is represented by the percentage of customers who stop doing business with the company. Through machine learning and statistical analysis, predictions of future churn will be identified and recommendations for prevention will be made in order to improve customer retention.
 
 
 
#### 2. DESCRIPTION:
 
With an ever-competitive telecommunications market, it is vital to understand your customer base in order to prevent customer churn and maximize retention.  It is far less expensive to keep an existing customer than it is to acquire a new one for the long term when marketing costs are included. Therefore, it is important to identify drivers of churn in an effort to prevent attrition. Thus, retaining current customers for the long term.  Ultimately, customer retention is important for maintaining and increasing profit.  This project will identify key drivers of churn for the Telco dataset and use modeling and statistics to identify ways to prevent churn in the future. Ultimately it will provide a recommendation that could be used by Telco or other customer-based service companies to maximize retention.
 
 
#### 3.INITIAL QUESTIONS:
 
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
 
#### 4. FORMULATING HYPOTHESES
- Is month-to-month customer churn related to Fiber Optic Internet Service?
   + H0: The churn rate of Month to month customers who have fiber optic internet <= the churn rate of all customers who have fiber optic internet.
   + H1: The churn rate of Month to month customers who have fiber optic internet > the churn rate of all customers who have fiber optic internet.
 
 
 
#### 5. DELIVERABLES:
- [x] README file - provides an overview of the project and steps for project reproduction. 
- [x] Draft Jupyter Notebook - provides all steps taken to produce the project.
- [x] Python Module File - provides reproducible code for acquiring,  preparing, exploring, & testing the data.
- [x] acquire.py - used to acquire data
- [x] prepare.py - used to prepare data
- [x] Report Jupyter Notebook - provides final presentation-ready assessment and recommendations.
- [x] .csv File - provides primary data used to make predictions & recommendations.
- [x] 5 minute presentation to stakeholders
 
 
## II. DATA CONTEXT
 
#### 1. DATA DICTIONARY:
 
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
 
|  Variables             |    Data Type                                |    Definition             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
customer_id           |               object             | unique identifier for each customer | 
is_senior                |                 integer (whole #)    |  senior citizen (65+), 0= no, 1=yes|
tenure_months       |                      integer (whole #)    | length of customer service in months|
monthly_charges     |                    float (decimal)    | current monthly charges in USD |
total_charges            |               float (decimal)    | sum of all charges for tenure in USD |
contract_type             |               object    | type of contract customer signed: month-to-month, One year, Two year|
internet_service_type |               object    | type of internet service customer has or had: Fiber optic, DSL, None|
payment_type |   object | type of payment method customer uses or used: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) |
is_male_Male         |   boolean int. (0, 1)    | binary gender identity 0= male, 1=female|    
has_partner_Yes    |                       boolean int. (0, 1)  | has spouse, partner, or significant other, 0= no, 1=yes||
has_dependents_Yes     |  boolean int. (0, 1)   | has dependent(s), children or otherwise, 0= no, 1=yes|
has_phone_service_Yes |                    boolean int. (0, 1)  | is or was a phone customer, 0= no, 1=yes|
has_multiple_lines_No phone service |      boolean int. (0, 1)  | didn’t or doesn’t have phone service, 0= no, 1=yes|
has_multiple_lines_Yes   |                 boolean int. (0, 1)  | has or had multiple phone lines, 0= no, 1=yes|
has_online_security_Yes   |  boolean int. (0, 1)| internet option: has or had service add-on, 0= no, 1=yes|
has_online_backup_Yes  | boolean int. (0, 1) | internet option: has or had service add-on, 0= no, 1=yes|
has_device_protection_Yes  |  boolean int. (0, 1)|  internet option: has or had service add-on, 0= no, 1=yes|
has_tech_support_Yes  |               boolean int. (0, 1)   | internet option: has or had service add-on, 0= no, 1=yes|
has_streaming_tv_Yes   |          boolean int. (0, 1)   | internet option: has or had service add-on, 0= no, 1=yes|
has_streaming_movies_Yes  |       boolean int. (0, 1)   | internet option: has or had service add-on, 0= no, 1=yes|
has_paperless_billing_Yes |    boolean int. (0, 1)|  customer bill is or was paperless, 0= no, 1=yes |
did_churn_Yes (target) |            boolean int. (0, 1) | customer services have been canceled, 0= no, 1=yes|  
contract_type_One year  |                  integer ( boolean 0,1|  customer has or did have 1 year contract, 0= no, 1=yes|
contract_type_Two year  |                  boolean int. (0, 1) | customer has or did have 2 year contract, 0= no, 1=yes|   
internet_service_type_Fiber optic  | boolean int. (0, 1)|  is or was a fiber optic internet customer,  0= no, 1=yes |
internet_service_type_None     | boolean int. (0, 1)| is or was an internet customer,  0= no, 1=yes |
payment_type_Credit card (automatic)   |   boolean int. (0, 1)  | payment type is or was credit card, 0= no, 1=yes |   
payment_type_Electronic check     |        boolean int. (0, 1)  | payment type is or was electronic check, 0= no, 1=yes |  
payment_type_Mailed check       |          boolean int. (0, 1)  | payment type is or was check via post, 0= no, 1=yes |
 
 
## III. DATA SCIENCE PIPELINE PROCESS:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver
 
#### 1. PLAN
- [x]  Review project expectations
- [x] Draft project goal to include measures of success
- [x]  Create questions related to the project
- [x]  Create questions related to the data
- [x] Create a plan for completing the project using the data science pipeline
- [x] Create a data dictionary to define variables and data context
- [x] Draft starting hypothesis
 
 
#### 2. ACQUIRE
- [x]  Create .gitignore
- [x]  Create env file with log-in credentials
- [x]  Store env file in .gitignore to ensure security of sensitive data
- [x]  Create acquire.py module
- [x]  Store functions needed to acquire the Telco dataset from mySQL
- [x]  Ensure all imports needed to run the functions are inside the acquire.py document
- [x] Using Jupyter Notebook
- [x]  Run all required imports
- [x] Import functions from aquire.py module
- [x]  Summarize dataset using methods and document observations
 
#### 3. PREPARE
- [x] Create prepare.py module
- [x] Store functions needed to prepare the Telco data such as:
   - [x] Split Function: to split data into train, validate, and test
   - [x] Cleaning Function: to clean data for exploration
   - [x] Encoding Function: to create numeric columns for object column
   - [x] Feature Engineering Function: to create new features
 
- [x] Ensure all imports needed to run the functions are inside the prepare.py document
Using Jupyter Notebook
- [x] Import functions from prepare.py module
- [x] Summarize dataset using methods and document observations
- [x] Clean data
- [x] Features need to be turned into numbers
- [x] Categorical features or discrete features need to be numbers that represent those categories
- [x] Continuous features may need to be standardized to compare like datatypes
- [x] Address missing values, data errors, unnecessary data, renaming
- [x] Split data into train, validate, and test samples
 
 
#### 4.EXPLORE
 
 
#### 5. MODEL & EVALUATE
In Jupyter Notebook:
- [x] Establish baseline accuracy
- [x] Train and fit multiple (3+) models with varying algorithms and/or hyperparameters
- [x] Compare evaluation metrics across models
- [x] Remove unnecessary features
- [x] Evaluate best performing models using validate set
- [x] Choose best performing validation model for use on test set
- [x] Test final model on out-of-sample testing dataset
- [x] Summarize performance
- [x] Interpret and document findings
 
 
#### 6. DELIVERY
 
 
 
## IV. MODULES:
 
- [x] Python Module Files - provide reproducible code for acquiring,  preparing, exploring, & testing the data.
   - [x] acquire.py - used to acquire data
   - [x] prepare.py - used to prepare data
 
 
 
## V. REPRODUCIBILITY:
### Steps to Reproduce
 
- [x] You will need an env.py file that contains the hostname, username, and password of the mySQL database that contains the telco_churn database.
- [x] Store that env file locally in the repository.
- [x] Make .gitignore and confirm .gitignore is hiding your env.py file.
- [x] Clone my repo (including the acquire.py and prepare.py)
- [x] Import python libraries:  pandas, matplotlib, seaborn, numpy, and sklearn.
- [x] Follow steps as outlined in the README.md. and Churn_Work.ipynb
- [x] Run Churn_Report.ipynb to view the final product.