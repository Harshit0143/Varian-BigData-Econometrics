 

* cost to complexity: "to avoid overfitting"


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


- fat: lots of predictors relative to the number of observatiuons
- “tall”:  lots of observations relative to the number of predictors.

- “good” means it minimizes Usually “good” means it minimizes some loss function such as the sum of squared residuals,
- When confronted with a prediction problem of this sort an economist would think immediately of a linear or logistic regression
- other methids: 
 1) classification and regression trees (CART);
 2) random forests; 
 3) penalized regression such as LASSO, LARS, and elastic nets.






* Classification problem
* Losigtic can make only Linear decision boundary! We sometimes need a non-linear lassfier   
x: explanatory variables or predictors (by economists)
* Economists would typically use a generalized linear model like a **logit** or **probit** for a classification problem.
* The goal is to construct (or “grow”) a decision tree that leads to good out-of-sample predictions
* Trees tend to work well for problems where there are important nonlinearities and interactions.
* I'll just throw ar you the decision tree first to show the mechanics and later we'll see how to grow it: 
* Why have they mentioned lived on some leaves and died in some? That's because it's the majority observations in the testing set.
* Let's see how to interpret it and make a prediction
Accuracy: 723 / 1046 = 69.12% as the paper mentiions it misclassifies abiut 30% of the training examples
* Show the tree and the "partition plot" side by side and explain the partitioning. It diivided the 2d space into rectiagular regions. Division by lines parallel to the axes
* Slight detail about regression trees: grow till THRESHOLD variamce, report the mean 
* Now it's clear that this decision tree can fit any kind of data
* Unfortunately the link to code the author refrerred is broken
* If the values of all features is same but the results of the 2 datas are different: It won't be possible to get 100% accuracy there. 
Forget what these number are, just look at "alive" or "dead"

# How to grow the tree?

* Continuous are split based on median, Catrgorial :k way split
* How you build the tree in this image is not explined but I'll  briefly explain how it's done: You try splitting over every paramater and then choose the one that's associated with tthe maximum information exchange. I'll take these 2 simple diagrams to explain this, w/o needing to use the math. Just to give the idea.

* As an example, let us continue with  the Titanic data and create a data and create a
tree that relates survival to age. In this case, the rule generated by the tree is \
simple: predict “survive” if age < 8.5 years. We can examine the same data with a 8.5 years. We can examine the same data with a
logistic regression to estimate the probability of survival as a function of age, (Not sure how this rule came. The median age is 8.5)
results reported in Table 3. 

* t values and p values?
* The tree model suggests that age is an important predictor of survival, while the logistic model says it is barely important

[5 rows x 14 columns]
Index(['pclass', 'survived', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket',
       'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'],
      dtype='object')
Median:  28.0
Mean:  29.881137667304014
min age: 0.17 val: 0.6141190737792076
max age: 80.0 val: 0.5756643510425494


* Not sure how usage of the age was rendered useless

the age example shows that they may reveal aspects of the data that are not apparent from a traditional linear modeling approach.
* Trees also handle missing data well

* Perlich, Provost, and Simonoff (2003) rees also handle missing data well. 
examined several standard datasets and found that  “logistic regression is better for smaller data sets and tree induction for larger data sets.”
* r the tree formulation made this nonlinearity immediately apparent.

## Pruning
*  Trees  - problem- overfitting - It can almost "completely" receover the training data information 
*  Solution- cost to complexity: "to avoid overfitting"
* one measure for complexity: the number of **leaves** . other: **max depth** 
* 10 - fold cross validation - 9 forlds training - excluded fold for out-of-sample trsting 
* choose C that's the best 
* Some researchers recommend being a bit more aggressive and advocate choosing the complexity parameter that is one standard deviation lower than the loss-minimizing value.
* skill, experience, and intuition and Diagnostics, exploration, and experimentation a

## Growing the tree:
* pure leaf idea 
* splitting then the lower level boxes
* now let's not discuss the splitting criuteria is chosen
### Explicitly Statistical Method: Conditional Inference tree - ctree
* ctree chooses the structure of the tree using a sequence of hypothesis tests
The resulting trees tend to need very little pruning (Hothorn, Hornik, and Zeileis 2006)
* show image on paper pg 12


* One might summarize this tree by the following principle: “women
and children first . . . particularly if they were traveling first . .  class"
* Not clearly mentioned what p < 0.001 and p  = 0.01 means 

* classification trees can be helpful in summarizing relationships in data, as well as predicting outcomes. 

* subsp: number of siblings plus spouse aboard.


# An Economic Example Using Home Mortgage Disclosure Act Data
if race played a significant role in determining who was approved for a mortgage.
* Result of logistic regression: The coeffi cient on race showed a statistically signifiically negative impact on probability of getting a mortgage for black applicants that later prompted considerable subsequent debate and discussion;

### Using a tree:
* 2,380  observations of 12  predictors , R package party.
* misclassifying 228 of the 2,380  observations : 9.579% trainig error 
* logistic: 225 of the 2,380  9.5% error
* “dmi”= “denied mortgage insurance.” This variable alone explains much of the variation in the data. 
* The race variable (“black”) shows up far down the tree
* One way to gauge whether a variable is important is to exclude it from the 
prediction and see what happens. 
* when it's done accuracy of the tree-based model doesn’t change at all: 
*  that some of the variables included are esewhere in the mortgage process, or that some of the variables included are highly correlated with race.


### Boosting Bagging Bootstrap
* but adding randomness turns out to be a helpful way of dealing 
with the overfi ith the overfi tting problem.

* Bootstrap involves choosing (with replacement) a sample of size involves choosing (with replacement) a sample of size n from a dataset from a dataset to estimate the sampling distribution of some statistic. A variation is the 
“m out of n bootstrap” which draws a sample of size bootstrap” which draws a sample of size m from a dataset of size from a dataset of size n > m.
* Bagging involves averaging across models estimated with several different boot- involves averaging across models estimated with several different bootstrap samples in order to improve the performance of an estimator
* Boosting involves repeated estimation where misclassified observations are given 
increasing weight in each repetition. The final estimate is then a vote or an average n
across the repeated estimates. 
* see image while dmo is strong 
Econometricians are well-acquainted with the bootstrap but rarely use the 
other two methods

* This method produces surprisingly good out-of-sample fits, particularly with 
highly nonlinear data.
* Howard and Bowles (2012) claim “ensembles of 
decision trees (often known as ‘Random Forests’) have been the most successful 
general-purpose algorithm in modern times.

* There are 
a number of variations and extensions of the basic “ensemble of trees” model such 
as Friedman’s “Stochastic Gradient Boosting” (Friedman 2002)

they don’t
offer simple summaries of relationships in the data


I ran the random forest method on the HMDA data and found that it misclassi- ran the random forest method on the HMDA data and found that it misclassifi ed 223 of the 2,380 cases, a small improvement over the logit and the ctree. I also ed 223 of the 2,380 cases, a small improvement over the logit and the ctree. I also
used the importance option in random forests to see how the predictors compared. sed the importance option in random forests to see how the predictors compared.
It turned out that “dmi t turned out that “dmi” was the most important predictor and race was second was the most important predictor and race was second
from the bottom, which is consistent with the ctree analysis