@ -1,3 +1,60 @@
I'll try my best to explain and understand the paper: "Big Data: New Tricks for Econometrics"


* `Conventional statistical and econometric techniques`: regression often work well, but there are issues unique to big datasets that may require different tools. We need tools for:
Problems:
1) powerful data manipulation tools
2) Large data mena more features. We need to see which ones are "relevant" else noise causes "overfitting" and poor "generalisation"
3) Third,large datasets may allow for more for more flexible relationships than simple linear models. 

### Data manipulation tools
- MySQL. Relational databases offer a flexible way to store, manipulate, and retrieve
data using a Structured Query Language (SQL): medium-sized datasets.
- several gigabytes: more primitive than SQL: can handle larger amounts of data
- A number of these tools are proprietary to Google, but have been described in
academic publications in sufficient detail that open-source implementations have been developed: need Amazon, Google, pplications use large clusters of computerssuch asthose provided byAmazon, Google,
Microsoft, and other cloud-computing providers.
- The outcome of the big-data processing described above is often a “small” table of data that may be directly human readable or can be loaded into an SQL database, a statistics package, or a spreadsheet
- For even larger data: At Google, for example, I have found that random samples on the order of 0.1 percent work fine for analysis of business data. Next: EDA, consistency and data-cleaning tasks.
- Exploratory Data Analysis (EDA) is an approach to analyzing and visualizing data sets to summarize their main characteristics, often with the help of statistical graphics and other data visualization methods.

- OpenRefine and DataWrangler can be used to assist in data cleansing.
- Data analysis in statistics and econometrics can be broken down into four categories: 1) prediction, 2) summarization, 3) estimation, and 4) hypothesis testing.
- ML: prediction , Data Mining:  summarization finding interesting patterns
- Econometricians, statisticians, and data mining specialists are generally looking for insights. Econometricians need to think about how will this policy affect the society

- Words: knowledge extraction, information discovery, information harvesting, 
data archaeology, data pattern processing, and exploratory data analysis

- econometrics is concerned with detecting and summarizing relationships in the data

the conditional distribution of some variable nterested in understanding the conditional distribution of some variable y given
some other variables ome other variables x = (x 1 , … ,x P ). If we want a point prediction, we can use the . If we want a point prediction, we can use the
mean or median of the conditional distribution. That actually the the thing behind Linear Regression. What we predict is the mean of a Normally Distributed RV

- x: predictors / features 
- fat: lots of predictors relative to the number of observatiuons
- “tall”:  lots of observations relative to the number of predictors.

- “good” means it minimizes Usually “good” means it minimizes some loss function such as the sum of squared residuals,
- When confronted with a prediction problem of this sort an economist would think immediately of a linear or logistic regression
- other methids: 
 1) classification and regression trees (CART);
 2) random forests; 
 3) penalized regression such as LASSO, LARS, and elastic nets.
- good out-of-sample predictions needed. In sample is just too easy you cna just remember the answer
- n linearly independent regressors will fit n observations perfectly but will usually observations perfectly but will usually have poor out-of-sample performance

* regularization: penalize models for excessive complexity: simpler models tend to work better for out-of-sample forecasts, 
* training data to estimate a mode the validation data to choose your model, and the testing data to evaluate
* k-fold cross-validation: Common choices for k are 10, 5 and leave one out
* this is actually different from what we did though
* Even if there is no tuning parameter, it is prudent to use cross-validation to report goodness-of-fit measures since it measures out-of-sample performance
* now that larger datasets have become available,datasets  there is no reason not to use
separate training and testing sets. It's an out-of-sample measure 


### Classification and Regression Trees
x: explanatory variables or predictors (by economists)
* Economists would typically use a generalized linear model like a logit or probit for a classification problem.
* 
