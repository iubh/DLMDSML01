# DLMDSML01 - Machine Learning

## Q & A - Sessions

### Introduction to Machine-Learning

<details>
           <summary>Hands-On Regression & Classification</summary>
           <p> `01_intro_to_ml.ipynb` (last update: xx-xx-xx) </p>
         </details>

### Clustering

#### Part 1

#### Part 2

We analyze clustering algorithms from a theoretical perspective, starting with developing a concept of similarity measures, discussing metrics to measure the quality of clustering methods, until going into detail on different clustering techniques. Finally we discuss hierarchical clustering in detail.

### Regression and Classification

<details>
           <summary>Hands-On Regression</summary>
           <p> `regression.ipynb` (last update: xx-xx-xx)</p>
         </details>

<details>
           <summary>Hands-On Classification</summary>
           <p> not yet prepared </p>
         </details>

<details>
           <summary>Theory and Concepts of Regression</summary>
           <p> hand-written document on *Tutorial Documents* </p>
         </details> 

<details>
           <summary>Multiclass Classification</summary>
           <p> `multiclass_classification.ipynb` (last update: 2021-02-09): We discuss how to generalize a classification problem to a multiclass classification problem. First of all, we show how to transform a logistic regression model into a multinomial logistic regression model. Then we show, with the use of the Iris dataset, how to generalize the sklearn classification algorithms to multiclass problems. After an outlook into multiclass performance metrics, like a multiclass confusion matrix, we discuss so-called meta-estimators available in *sklearn.multiclass* which help to increase accuracy and runtime performance of the classifiers .    </p>
         </details>

### Support Vector Machines

### Decision Trees and Ensemble Methods

#### Part 2

We deepen our understanding of random forest algorithms, namely how boosting trees work. After discussing an analytical example we go over to the scikit learn's implementation of boosted trees as well as most recent algorithms, like XGBoost, LightGBM and CatBoost.

### Genetic Algorithms (GAs)

#### Part 1 - Theory and Concepts

Based on *Haupt & Haupt, Practical Genetic Algorithms (2004)* we discuss how to approach GAs both for binary as well as continuous problems. We try to understand how to encode variables, find the initial population, perform the natural selection process as well as mating/crossover and mutations until convergence is reached. 

*    `Q_A_genetic_algorithms_theory.ipynb` (last update: 2021-01-19): Jupyter notebook exploring
how to approach GAs for binary and continuous problems. 

#### Part 2 - Applications

### Performance Metrics

We discuss how to evaluate the performance of a machine-learning algorithm, both for
supervised and unsupervised tasks.

Sources:

*    `11_performance_measures.ipynb` (last update: 2020-12-22): Jupyter notebook exploring
the individual performance measures from the *sklearn.metrics* functions.   

### Recommendation Systems

We discuss the basic principles of how to implement recommendation systems. For the MovieLens dataset we build up a first, simple user-based collaborative filtering movie recommendation system.

*    `12_recommendation_systems.ipynb` (last update: 2021-01-05): Jupyter notebook implementing a user-based collaborative filtering movie recommendation system.


