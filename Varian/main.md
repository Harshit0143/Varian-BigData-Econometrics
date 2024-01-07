# [Big Data: New Tricks for Econometrics](https://www.aeaweb.org/articles?id=10.1257/jep.28.2.3)

## Some terms:
* $x$ is also called $predictor$ or  $feature$
* $Overfitting / \text{ }  High \text{ } Variance$: The model picks up noise in the data, performs well on the Traning Data for poor generalisation.

* $Underfitting / \text{ }  High \text{ }  Bias$: The model is too simple unable to capture patters in the data. 
* $Hyperparametrs$: They specify details of the learning process. They are chosen for traning and not $learnt$, in contrast to $parameters$. For example the $learning  \text{ } rate$ in Gradient Descent, the $C$ in Soft Margin SVM's etc.

## General Considerations for Prediction
* Our goal is to get good $out-of-sample$ predictions i.e. the model $generalises$ well or simply, it makes $good$ predictions on unseen examples.  
* $n$ linearly independent regressors will fit $n$ observations perfectly but but will usually have poor $out-of-sample$ performance. 
### Solving Overfitting
1) $Regularization$: Penalize models for excessive complexity as $simpler$ models tend to work better for $out-of-sample$ forecasts.
2) Splitting the dataset into $Training$, $Validation$ and $Testing$ 
3) An $explicit$  numeric  measure  of  model  complexity: Hyperparametrs. For example, the degree of the polynomial you want to fit your data into. 

### Tuning the model: $k-fold-cross-validation$
***
#### Algorithm:
1) Divide  the  data  into  $k$  roughly  equal  subsets  (folds)  and  label  them  by  
$s = 1, ... , k$. Start with subset $s = 1$.
2) Pick a value for the tuning parameter.
3) Fit your model using the $k − 1$ subsets other than subset $s$.
4) Predict for subset $s$ and measure the associated loss.
5) Stop if $s = k$, otherwise increment $s$ by $1$ and go to step $2$
***


* Notice: We test on the fold, we didn't use for training so it'll give us an idea of $out-of-sample$ performance. Even if there is no $tuning \text{ } parameter$, it is prudent to use cross-validation to report $goodness-of-fit$.
* Common choices for $k$ are $10$, $5$, and $SampleSize - 1$ or $“leave \text{ } one \text{ } out”$.
* Another usecase: When dataset is small and you don't want to split it into  $Training$, $Validation$ and $Testing$ and $waste$ it. 
* For  many  years,  economists  have  reported  $in-sample$  $goodness-of-fit$  measures  using  the  excuse  that  we  had  $small$  datasets. But now now larger datasets have become available so it'sgood to split the dataset. 




## Classification and Regression Trees
