# Project_1





***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___
## <a name="project_description"></a>Project Description:
Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook Final Report.

Create modules (acquire.py, prepare.py) that make your process repeateable and your report (notebook) easier to read and follow.

Ask exploratory questions of your data that will help you understand more about the attributes and drivers of customers churning. Answer questions through charts and statistical tests.

Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers.

Refine your work into a Report, in the form of a jupyter notebook, that you will walk through in a 5 minute presentation to a group of collegues and managers about the work you did, why, goals, what you found, your methdologies, and your conclusions.

Be prepared to answer panel questions about your code, process, findings and key takeaways, and model.


[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
1) Begin with looking for information what Churn prediction in Buisness is and what type of thing are indicators for churn. 
Articles read include:

https://www.linkedin.com/pulse/most-powerful-question-business-greg-daines/

https://baremetrics.com/blog/churn-analysis

2) Next lets go a head and look a the data, which will require creating an acquire.py and function to import CSV from MYSQL.
3) Move on to manipulating the data to try and make some pretty pictures this will help you build a prepare.py 
4) Next lets take the data and explore it some more to get an idea of how you want to prove you hypothesis. 


[[Back to top](#top)]

### Project Outline:
Acquire data
Prepare Data
Explore Data
Create Hypothesis
Build Model
Train Model
Validate Model
Test Model 
Conclusion

        
### Hypothesis
Why are customers churning?

Is the monthly bill for customers who churn higher than for customers who do not churn.
Do customers who churn have more than services provided than customers who dont churn 
Does contract type relate to if a customer will churn



### Target variable
number_services
monthly_avg
monthly_charges

### Need to haves (Deliverables):
acquire.py
prepare.py
predictions.csv
Final_notebook.ipybn
this readme.md


### Nice to haves (With more time):
Functions to so no code is shown 
Find a better color palette I want vibrant colors. 
Finish the third question and try and get a better understanding 


***

## <a name="findings"></a>Key Findings:
There is more than one way to predict but simple is better and diving to deep will cause you to drown.



[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  


### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|Unnamed: 0||int64|
|internet_service_type_id| |int64|
|payment_type_id||int64 |
|contract_type_id | |int64|
|customer_id|| object|
|gender | |object |
|senior_citizen | |int64 |
|partner| |object |
|dependents| |object|
|tenure| | int64|
|phone_service| |object |
|multiple_lines| |object |
|online_security| |object |
|online_backup| |object |
|device_protection| |object |
|tech_support| |object |
|streaming_tv| |object |
|streaming_movies| |object |
|paperless_billing| |object |
|monthly_charges| | float64|
|total_charges| |object |
|churn| |object |
|contract_type| |object |
|payment_type| |object |
|internet_service_type| | object|
|number_services||int64|
|monthly_avg||int64|
***
[[Back to top](#top)]
## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 
Try to Make pretty pictures
Repeat until you get something you understand.

*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:

    - explore.py



### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]


### Stats Test 1: T-Test:

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is There is no difference in churn between those whose monthly bill is above or below Average monthly bill
- The alternate hypothesis (H<sub>1</sub>) is There is a significant difference in churn between those wwhose monthly bill is above or below Average monthly bill

#### Alpha value:

- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:
We reject the null hypothesis.

#### Summary:
While I still do not fully grasp this process it was completed
***
### Stats Test 2: Chi2


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is Churn is independent of the number services a customer has
- The alternate hypothesis (H<sub>1</sub>) is Churn is dependent of the number services a customer has

#### Alpha value:
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
We reject the null hypothesis.


#### Summary:
While I still do not fully grasp this process it was completed


## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
Our baseline accuracy for churn in all cases on the Telco Dataset is 0.734

- Selected features to input into models:
    - features = ['internet_service_type_id',
 'payment_type_id',
 'contract_type_id',
 'tenure',
 'phone_service',
 'multiple_lines',
 'online_security',
 'online_backup',
 'device_protection',
 'tech_support',
 'streaming_tv',
 'streaming_movies',
 'paperless_billing',
 'monthly_charges',
 'total_charges',
 'number_services',
 'monthly_avg']

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
### Model 1: Random Forest


- Model 1 results:
### Tree with max depth of 6|
---
||0|1|accuracy|macro avg|weighted avg|
| ----- | ----- | ----- | ----- | ----- | ----- |
|precision     |0.842781     |0.731183 | 0.821692    | 0.786982     | 0.813131|
|recall        |0.930820    | 0.520076 | 0.821692   |  0.725448     | 0.821692|
|f1-score      |0.884615   |  0.607821 | 0.821692  |   0.746218     | 0.811075|
|support    |2891.000000  |1046.000000 | 0.821692 | 3937.000000  | 3937.000000|
***

### Model 2 : Logistic Regression


- Model 2 results:
### Validation set|
---
| |precision|recall|f1-score|support|
| ----- | ----- | ----- | ----- | ----- | ----- |
|0     |  0.84    |  0.88   |   0.86    |  1239|
|1    |   0.62    |  0.54   |   0.58    |   449|
|accuracy    |        |     |   0.79     | 1688|
|macro avg    | 0.73|0.71    |  0.72     | 1688|
|weighted avg|0.78    |0.79    |0.79     | 1688|
***


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline |0.734 | |
|Random Forest | 0.581225 |  |  
|Logistic Regression |0.59 | |  


- Logistic Regression model performed the best


## Testing the Model
 Logistic Regression
- Model Testing Results
0.60
***

## <a name="conclusion"></a>Conclusion:
There is a lot of ways this could have been done using other variables I chose variable based on the articles I read and information that made since 
to me. If I had to do this again information that would be useful includes. Data on reasoning for purchasing, if customer made complaints, and if tech support was utilized. 

[[Back to top](#top)]
