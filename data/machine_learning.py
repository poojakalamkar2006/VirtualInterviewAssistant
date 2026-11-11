questions = {

    "Easy": [

        {
            "question": "What is Machine Learning?",
            "expected_answer": "Machine Learning is a field of AI where computers learn patterns from data and use those patterns to make predictions or decisions without being explicitly programmed for every case."
        },

        {
            "question": "What is the difference between AI and Machine Learning?",
            "expected_answer": "AI is the broader field of creating systems that perform tasks requiring intelligence. Machine Learning is a subset of AI that learns patterns from data."
        },

        {
            "question": "What are the main types of Machine Learning?",
            "expected_answer": "The main types are supervised learning, unsupervised learning, and reinforcement learning."
        },

        {
            "question": "What is supervised learning?",
            "expected_answer": "Supervised learning trains a model using labeled data, where the input and the expected output are known."
        },

        {
            "question": "What is unsupervised learning?",
            "expected_answer": "Unsupervised learning finds patterns or structures in data without using labeled target outputs."
        },

        {
            "question": "What is reinforcement learning?",
            "expected_answer": "Reinforcement learning trains an agent to make decisions by interacting with an environment and receiving rewards or penalties."
        },

        {
            "question": "What is a dataset in Machine Learning?",
            "expected_answer": "A dataset is a collection of data used to train, validate, or test a Machine Learning model."
        },

        {
            "question": "What are features in Machine Learning?",
            "expected_answer": "Features are input variables or measurable properties used by a Machine Learning model to make predictions."
        },

        {
            "question": "What is a target variable?",
            "expected_answer": "The target variable is the output a supervised Machine Learning model is trained to predict."
        },

        {
            "question": "What is a label in Machine Learning?",
            "expected_answer": "A label is the known target value associated with a training example in supervised learning."
        },

        {
            "question": "What is training data?",
            "expected_answer": "Training data is the portion of a dataset used by a model to learn patterns and relationships."
        },

        {
            "question": "What is testing data?",
            "expected_answer": "Testing data is a separate dataset used to evaluate how well a trained model performs on unseen data."
        },

        {
            "question": "What is validation data?",
            "expected_answer": "Validation data is used during model development to compare models, tune settings, and select a suitable model before final testing."
        },

        {
            "question": "Why do we split data into training and testing sets?",
            "expected_answer": "The split helps evaluate whether a model can generalize to unseen data rather than simply memorizing the training examples."
        },

        {
            "question": "What is classification?",
            "expected_answer": "Classification is a supervised learning task where a model predicts a category or class, such as spam or not spam."
        },

        {
            "question": "What is regression?",
            "expected_answer": "Regression is a supervised learning task where a model predicts a continuous numerical value, such as house price."
        },

        {
            "question": "What is clustering?",
            "expected_answer": "Clustering is an unsupervised learning technique that groups similar data points together."
        },

        {
            "question": "What is linear regression?",
            "expected_answer": "Linear regression models the relationship between input variables and a continuous target using a linear equation."
        },

        {
            "question": "What is logistic regression?",
            "expected_answer": "Logistic regression is a classification algorithm that estimates the probability of a class, commonly using the sigmoid function for binary classification."
        },

        {
            "question": "What is a decision tree?",
            "expected_answer": "A decision tree makes predictions by repeatedly splitting data based on feature conditions and following branches to a final prediction."
        },

        {
            "question": "What is a random forest?",
            "expected_answer": "Random Forest is an ensemble algorithm that combines predictions from many decision trees to improve generalization and reduce overfitting."
        },

        {
            "question": "What is K-Nearest Neighbors?",
            "expected_answer": "K-Nearest Neighbors predicts a value or class based on the closest training examples according to a distance measure."
        },

        {
            "question": "What is Naive Bayes?",
            "expected_answer": "Naive Bayes is a probabilistic classification algorithm based on Bayes' theorem and assumes conditional independence between features."
        },

        {
            "question": "What is Support Vector Machine?",
            "expected_answer": "Support Vector Machine is an algorithm that finds a decision boundary that separates classes while maximizing the margin between them."
        },

        {
            "question": "What is K-Means clustering?",
            "expected_answer": "K-Means is an unsupervised algorithm that divides data into a chosen number of clusters by assigning points to nearby centroids and updating those centroids."
        },

        {
            "question": "What is an algorithm in Machine Learning?",
            "expected_answer": "A Machine Learning algorithm is a method used to learn patterns from data and produce predictions or decisions."
        },

        {
            "question": "What is a Machine Learning model?",
            "expected_answer": "A Machine Learning model is the learned representation or function produced by training an algorithm on data."
        },

        {
            "question": "What is model training?",
            "expected_answer": "Model training is the process of learning model parameters from training data by minimizing an objective or loss function."
        },

        {
            "question": "What is prediction in Machine Learning?",
            "expected_answer": "Prediction is the process of using a trained model to produce an output for new input data."
        },

        {
            "question": "What is overfitting?",
            "expected_answer": "Overfitting occurs when a model learns the training data too closely, including noise, and performs poorly on unseen data."
        },

        {
            "question": "What is underfitting?",
            "expected_answer": "Underfitting occurs when a model is too simple to capture important patterns in the data and performs poorly even on training data."
        },

        {
            "question": "What is generalization?",
            "expected_answer": "Generalization is the ability of a Machine Learning model to perform well on new, unseen data."
        },

        {
            "question": "What is bias in Machine Learning?",
            "expected_answer": "Bias is error caused by overly simple assumptions in a model, which can prevent it from capturing important relationships in the data."
        },

        {
            "question": "What is variance in Machine Learning?",
            "expected_answer": "Variance describes how sensitive a model is to changes in its training data. High variance often leads to overfitting."
        },

        {
            "question": "What is the bias-variance tradeoff?",
            "expected_answer": "The bias-variance tradeoff involves balancing errors from overly simple models against errors from overly sensitive models to achieve good generalization."
        },

        {
            "question": "What is a loss function?",
            "expected_answer": "A loss function measures how different a model's prediction is from the expected target value."
        },

        {
            "question": "What is a cost function?",
            "expected_answer": "A cost function summarizes model loss across multiple training examples and is used to measure overall training error."
        },

        {
            "question": "What is Mean Squared Error?",
            "expected_answer": "Mean Squared Error is the average of the squared differences between predicted and actual values and is commonly used for regression."
        },

        {
            "question": "What is Mean Absolute Error?",
            "expected_answer": "Mean Absolute Error is the average absolute difference between predicted and actual values."
        },

        {
            "question": "What is accuracy?",
            "expected_answer": "Accuracy is the proportion of predictions that are correct out of all predictions."
        },

        {
            "question": "What is precision?",
            "expected_answer": "Precision is the proportion of predicted positive cases that are actually positive."
        },

        {
            "question": "What is recall?",
            "expected_answer": "Recall is the proportion of actual positive cases that the model correctly identifies."
        },

        {
            "question": "What is F1-score?",
            "expected_answer": "F1-score is the harmonic mean of precision and recall and is useful when both types of errors matter."
        },

        {
            "question": "What is a confusion matrix?",
            "expected_answer": "A confusion matrix summarizes classification results using true positives, true negatives, false positives, and false negatives."
        },

        {
            "question": "What is a true positive?",
            "expected_answer": "A true positive occurs when the model correctly predicts the positive class."
        },

        {
            "question": "What is a true negative?",
            "expected_answer": "A true negative occurs when the model correctly predicts the negative class."
        },

        {
            "question": "What is a false positive?",
            "expected_answer": "A false positive occurs when the model predicts the positive class but the actual class is negative."
        },

        {
            "question": "What is a false negative?",
            "expected_answer": "A false negative occurs when the model predicts the negative class but the actual class is positive."
        },

        {
            "question": "What is feature scaling?",
            "expected_answer": "Feature scaling transforms numerical features to comparable ranges so that algorithms sensitive to feature magnitude work more effectively."
        },

        {
            "question": "What is normalization in Machine Learning?",
            "expected_answer": "Normalization commonly scales values to a bounded range, often between 0 and 1, depending on the method used."
        },

        {
            "question": "What is standardization?",
            "expected_answer": "Standardization transforms a feature so that it has approximately zero mean and unit standard deviation."
        },

        {
            "question": "Why is feature scaling important?",
            "expected_answer": "Scaling prevents features with larger numerical ranges from dominating algorithms that depend on distances or gradient-based optimization."
        },

        {
            "question": "What is missing data?",
            "expected_answer": "Missing data occurs when some values are unavailable or not recorded for one or more observations."
        },

        {
            "question": "How can missing values be handled?",
            "expected_answer": "Missing values can be removed, filled using appropriate imputation methods, or handled using algorithms that support missing values."
        },

        {
            "question": "What is data preprocessing?",
            "expected_answer": "Data preprocessing prepares raw data for Machine Learning by cleaning, transforming, encoding, scaling, and handling missing or invalid values."
        },

        {
            "question": "What is categorical data?",
            "expected_answer": "Categorical data represents values belonging to categories, such as gender, city, product type, or department."
        },

        {
            "question": "What is numerical data?",
            "expected_answer": "Numerical data represents measurable quantities expressed as numbers, such as age, salary, height, or temperature."
        },

        {
            "question": "What is one-hot encoding?",
            "expected_answer": "One-hot encoding converts categorical values into separate binary features, with each category represented by a column."
        },

        {
            "question": "What is label encoding?",
            "expected_answer": "Label encoding assigns a numerical value to each category. It should be used carefully because the assigned numbers can imply an order that may not exist."
        },

        {
            "question": "What is feature engineering?",
            "expected_answer": "Feature engineering is the process of creating, transforming, or selecting useful input features to improve model performance."
        },

        {
            "question": "What is feature selection?",
            "expected_answer": "Feature selection chooses a useful subset of available features while removing irrelevant or redundant ones."
        },

        {
            "question": "What is dimensionality reduction?",
            "expected_answer": "Dimensionality reduction reduces the number of input features while attempting to preserve important information in the data."
        },

        {
            "question": "What is PCA?",
            "expected_answer": "Principal Component Analysis is a dimensionality-reduction technique that transforms correlated features into a smaller set of components capturing major directions of variance."
        },

        {
            "question": "What is cross-validation?",
            "expected_answer": "Cross-validation repeatedly splits training data into training and validation portions to estimate how well a model is likely to generalize."
        },

        {
            "question": "What is k-fold cross-validation?",
            "expected_answer": "K-fold cross-validation divides data into k parts and trains and validates the model multiple times, using a different part for validation each time."
        },

        {
            "question": "What is a hyperparameter?",
            "expected_answer": "A hyperparameter is a setting chosen before or during model training that controls how the learning algorithm behaves."
        },

        {
            "question": "What is the difference between parameters and hyperparameters?",
            "expected_answer": "Parameters are learned from training data, while hyperparameters are settings chosen to control the training process or model structure."
        },

        {
            "question": "What is hyperparameter tuning?",
            "expected_answer": "Hyperparameter tuning searches for suitable hyperparameter values that improve model performance on validation data."
        },

        {
            "question": "What is regularization?",
            "expected_answer": "Regularization adds a penalty or constraint to discourage overly complex models and help reduce overfitting."
        },

        {
            "question": "What is L1 regularization?",
            "expected_answer": "L1 regularization adds a penalty based on the absolute values of model coefficients and can encourage some coefficients to become exactly zero."
        },

        {
            "question": "What is L2 regularization?",
            "expected_answer": "L2 regularization adds a penalty based on squared coefficient values and generally discourages large weights."
        },

        {
            "question": "What is gradient descent?",
            "expected_answer": "Gradient descent is an optimization algorithm that updates model parameters in the direction that reduces the loss function."
        },

        {
            "question": "What is a learning rate?",
            "expected_answer": "The learning rate controls how large each parameter update is during optimization."
        },

        {
            "question": "What happens if the learning rate is too high?",
            "expected_answer": "A learning rate that is too high can cause training to overshoot good solutions, become unstable, or fail to converge."
        },

        {
            "question": "What happens if the learning rate is too low?",
            "expected_answer": "A learning rate that is too low can make training extremely slow and may require many iterations to reach a good solution."
        }

    ],

    #"Medium": 

        "Medium": [
    {
        "question": "What is the typical Machine Learning workflow?",
        "expected_answer": "A typical workflow includes defining the problem, collecting data, preprocessing it, splitting the data, training models, tuning them, evaluating performance, and deploying and monitoring the selected model."
    },

    {
        "question": "How do you decide whether a problem is classification or regression?",
        "expected_answer": "If the target is a category, it is usually classification. If the target is a continuous numerical value, it is usually regression."
    },

    {
        "question": "What is the difference between binary and multiclass classification?",
        "expected_answer": "Binary classification predicts between two classes, while multiclass classification predicts one class from more than two possible classes."
    },

    {
        "question": "What is multilabel classification?",
        "expected_answer": "Multilabel classification allows each input example to belong to multiple classes simultaneously."
    },

    {
        "question": "What is the difference between parametric and non-parametric models?",
        "expected_answer": "Parametric models assume a fixed form with a limited number of parameters, while non-parametric models can have complexity that grows with the amount of training data."
    },

    {
        "question": "What is the difference between generative and discriminative models?",
        "expected_answer": "Generative models learn how data is distributed and can model how observations are generated, while discriminative models focus on predicting labels or decision boundaries."
    },

    {
        "question": "What assumptions does linear regression make?",
        "expected_answer": "Common assumptions include linearity, independent observations, appropriate error behavior, constant error variance, and limited problematic multicollinearity."
    },

    {
        "question": "What is multicollinearity?",
        "expected_answer": "Multicollinearity occurs when input features are strongly correlated with each other, making coefficient estimates unstable and harder to interpret."
    },

    {
        "question": "How can multicollinearity be detected?",
        "expected_answer": "It can be investigated using correlation analysis, variance inflation factor, model diagnostics, or inspection of unstable coefficients."
    },

    {
        "question": "How can multicollinearity be handled?",
        "expected_answer": "Possible approaches include removing redundant features, combining features, using dimensionality reduction, or applying regularization."
    },

    {
        "question": "What is polynomial regression?",
        "expected_answer": "Polynomial regression extends linear regression by using polynomial transformations of features to model nonlinear relationships."
    },

    {
        "question": "What is the difference between linear and logistic regression?",
        "expected_answer": "Linear regression predicts continuous values, while logistic regression models class probabilities and is commonly used for classification."
    },

    {
        "question": "Why is logistic regression called regression even though it is used for classification?",
        "expected_answer": "It estimates a continuous probability using a regression model, which is then converted into a class decision using a threshold."
    },

    {
        "question": "What is the sigmoid function?",
        "expected_answer": "The sigmoid function maps any real-valued input to a value between 0 and 1 and is commonly used to represent binary-class probabilities."
    },

    {
        "question": "What is the decision boundary in classification?",
        "expected_answer": "The decision boundary is the region or surface that separates different predicted classes in the feature space."
    },

    {
        "question": "What is entropy in a decision tree?",
        "expected_answer": "Entropy measures the impurity or uncertainty of a set of examples. A lower entropy indicates that the examples are more concentrated in particular classes."
    },

    {
        "question": "What is Gini impurity?",
        "expected_answer": "Gini impurity measures the probability of incorrectly classifying a randomly chosen sample if its class were assigned according to the class distribution."
    },

    {
        "question": "What is information gain?",
        "expected_answer": "Information gain measures how much a split reduces uncertainty or entropy in a decision tree."
    },

    {
        "question": "Why can decision trees overfit?",
        "expected_answer": "A deep tree can create very specific splits that memorize training examples and noise instead of learning general patterns."
    },

    {
        "question": "How can a decision tree be prevented from overfitting?",
        "expected_answer": "Use techniques such as limiting tree depth, requiring minimum samples for splits or leaves, pruning, or using ensemble methods."
    },

    {
        "question": "What is bagging?",
        "expected_answer": "Bagging trains multiple models on different bootstrap samples of the training data and combines their predictions to reduce variance."
    },

    {
        "question": "What is boosting?",
        "expected_answer": "Boosting builds models sequentially, with later models focusing more on correcting errors made by earlier models."
    },

    {
        "question": "What is the difference between bagging and boosting?",
        "expected_answer": "Bagging mainly reduces variance by training models independently on sampled data, while boosting builds models sequentially to improve previous errors."
    },

    {
        "question": "Why is Random Forest usually more robust than a single decision tree?",
        "expected_answer": "Random Forest averages many diverse decision trees, which generally reduces variance and makes the model less sensitive to individual training samples."
    },

    {
        "question": "What is gradient boosting?",
        "expected_answer": "Gradient boosting builds an ensemble sequentially, with each new model attempting to reduce the remaining loss or error of the current ensemble."
    },

    {
        "question": "What is XGBoost?",
        "expected_answer": "XGBoost is an optimized gradient boosting algorithm that uses decision trees and includes regularization and engineering improvements for speed and performance."
    },

    {
        "question": "What is the difference between Random Forest and XGBoost?",
        "expected_answer": "Random Forest uses bagging with independently trained trees, while XGBoost uses sequential boosting where later trees correct errors from earlier trees."
    },

    {
        "question": "How does K-Nearest Neighbors work?",
        "expected_answer": "KNN finds the nearest training examples to a new point and uses their labels or values to make the prediction."
    },

    {
        "question": "Why is feature scaling important for KNN?",
        "expected_answer": "KNN relies on distances, so features with larger numerical scales can dominate the distance calculation if features are not scaled."
    },

    {
        "question": "What happens when K is too small in KNN?",
        "expected_answer": "A very small K makes the model sensitive to noise and individual training points, increasing variance and the risk of overfitting."
    },

    {
        "question": "What happens when K is too large in KNN?",
        "expected_answer": "A very large K can make the model too influenced by distant points and oversimplify the decision boundary, causing underfitting."
    },

    {
        "question": "What is the kernel trick in SVM?",
        "expected_answer": "The kernel trick allows SVMs to model nonlinear decision boundaries by computing similarities in a higher-dimensional feature space without explicitly constructing that space."
    },

    {
        "question": "What is the margin in SVM?",
        "expected_answer": "The margin is the distance between the decision boundary and the closest training examples from the classes."
    },

    {
        "question": "What are support vectors?",
        "expected_answer": "Support vectors are training examples that are most influential in defining the SVM decision boundary, typically those closest to it."
    },

    {
        "question": "What is the purpose of the C parameter in SVM?",
        "expected_answer": "C controls the tradeoff between allowing classification errors and keeping a wider margin. Higher C penalizes training errors more strongly."
    },

    {
        "question": "What is the purpose of gamma in an RBF-kernel SVM?",
        "expected_answer": "Gamma controls how strongly individual training points influence the decision boundary. High gamma can create more complex boundaries."
    },

    {
        "question": "What is Naive Bayes based on?",
        "expected_answer": "Naive Bayes is based on Bayes' theorem and a simplifying assumption that features are conditionally independent given the class."
    },

    {
        "question": "Why can Naive Bayes work well for text classification?",
        "expected_answer": "It is computationally efficient, works well with high-dimensional sparse features, and can perform effectively even with relatively limited training data."
    },

    {
        "question": "What is the difference between K-Means and hierarchical clustering?",
        "expected_answer": "K-Means directly divides data into a chosen number of clusters, while hierarchical clustering builds a hierarchy of clusters that can be represented using a dendrogram."
    },

    {
        "question": "What is the elbow method?",
        "expected_answer": "The elbow method examines clustering error such as within-cluster sum of squares for different K values and looks for a point where additional clusters provide diminishing improvement."
    },

    {
        "question": "What is a centroid in K-Means?",
        "expected_answer": "A centroid is the representative center of a cluster, calculated as the mean of the points assigned to that cluster."
    },

    {
        "question": "What are common limitations of K-Means?",
        "expected_answer": "K-Means requires choosing K, is sensitive to initialization and scaling, and works best when clusters are reasonably compact and separated."
    },

    {
        "question": "What is DBSCAN?",
        "expected_answer": "DBSCAN is a density-based clustering algorithm that groups points in dense regions and can identify noise or outliers."
    },

    {
        "question": "What is PCA used for?",
        "expected_answer": "PCA is used to reduce dimensionality, remove some redundancy, visualize high-dimensional data, or create compact representations while preserving major variance."
    },

    {
        "question": "Why should features often be standardized before PCA?",
        "expected_answer": "PCA is based on variance, so features with larger scales can dominate the principal components if the features are not appropriately scaled."
    },

    {
        "question": "What is explained variance in PCA?",
        "expected_answer": "Explained variance indicates how much of the original data's variance is captured by each principal component or by a group of components."
    },

    {
        "question": "What is the difference between feature selection and feature extraction?",
        "expected_answer": "Feature selection keeps a subset of the original features, while feature extraction creates new representations from the original features."
    },

    {
        "question": "What is data leakage?",
        "expected_answer": "Data leakage occurs when information unavailable at prediction time is used during training, causing unrealistically high evaluation performance."
    },

    {
        "question": "How can data leakage happen during preprocessing?",
        "expected_answer": "It can happen when preprocessing steps such as scaling, imputation, or feature selection are fitted using the entire dataset before the train-test split."
    },

    {
        "question": "How can preprocessing leakage be prevented?",
        "expected_answer": "Split the data first and fit preprocessing transformations only on the training data. Use pipelines to keep preprocessing and modeling together."
    },

    {
        "question": "What is a Machine Learning pipeline?",
        "expected_answer": "A pipeline connects preprocessing and modeling steps into a single workflow so that transformations are applied consistently during training and prediction."
    },

    {
        "question": "Why are pipelines useful in Machine Learning?",
        "expected_answer": "Pipelines improve reproducibility, prevent preprocessing mistakes and leakage, and ensure the same transformations are applied to training and unseen data."
    },

    {
        "question": "What is stratified sampling?",
        "expected_answer": "Stratified sampling creates samples that preserve important proportions of groups, commonly preserving class proportions in classification datasets."
    },

    {
        "question": "Why is stratified train-test splitting useful for classification?",
        "expected_answer": "It helps maintain similar class proportions in the training and testing sets, especially when classes are imbalanced."
    },

    {
        "question": "What is an imbalanced dataset?",
        "expected_answer": "An imbalanced dataset has significantly different numbers of examples across classes."
    },

    {
        "question": "Why can accuracy be misleading for imbalanced classification?",
        "expected_answer": "A model can achieve high accuracy by mostly predicting the majority class while performing poorly on the minority class."
    },

    {
        "question": "How can imbalanced classification be handled?",
        "expected_answer": "Possible approaches include class weighting, appropriate resampling, threshold adjustment, and evaluation using metrics such as precision, recall, and PR-AUC."
    },

    {
        "question": "What is ROC-AUC?",
        "expected_answer": "ROC-AUC measures how well a classifier ranks positive examples above negative examples across different classification thresholds."
    },

    {
        "question": "What is the precision-recall curve?",
        "expected_answer": "A precision-recall curve shows the tradeoff between precision and recall at different classification thresholds."
    },

    {
        "question": "When is PR-AUC more informative than ROC-AUC?",
        "expected_answer": "PR-AUC can be more informative when the positive class is rare because it focuses on precision and recall for the positive class."
    },

    {
        "question": "How do you choose an evaluation metric for a Machine Learning model?",
        "expected_answer": "Choose metrics based on the business objective, type of prediction, class balance, and relative cost of different errors."
    },

    {
        "question": "What is cross-validation mainly used for?",
        "expected_answer": "Cross-validation estimates generalization performance and helps compare models or tune hyperparameters using repeated training and validation splits."
    },

    {
        "question": "What is stratified k-fold cross-validation?",
        "expected_answer": "It performs k-fold cross-validation while attempting to preserve class proportions in each fold."
    },

    {
        "question": "What is grid search?",
        "expected_answer": "Grid search evaluates predefined combinations of hyperparameter values to identify a combination that performs well according to a chosen validation metric."
    },

    {
        "question": "What is random search?",
        "expected_answer": "Random search samples hyperparameter combinations from specified distributions and can explore large search spaces more efficiently than exhaustive grid search."
    },


    ],

    #"Hard":
    #  
        "Hard": [

    {
        "question": "Explain the bias-variance tradeoff in detail.",
        "expected_answer": "High bias usually means the model is too simple and underfits, while high variance means it is too sensitive to training data and overfits. Good model design balances both to achieve strong generalization."
    },

    {
        "question": "How would you diagnose whether a model is underfitting or overfitting?",
        "expected_answer": "Compare training and validation performance. Poor performance on both suggests underfitting, while very good training performance combined with much worse validation performance suggests overfitting."
    },

    {
        "question": "What is irreducible error?",
        "expected_answer": "Irreducible error is error caused by noise or uncertainty inherent in the data that cannot be eliminated completely by choosing a different model."
    },

    {
        "question": "What is the difference between model capacity and model complexity?",
        "expected_answer": "Model capacity describes how complex a function a model can represent. Higher capacity allows more complex patterns but can increase the risk of overfitting."
    },

    {
        "question": "Why does adding more features sometimes reduce model performance?",
        "expected_answer": "Irrelevant or noisy features can increase variance, make learning harder, and introduce the curse of dimensionality."
    },

    {
        "question": "What is the curse of dimensionality?",
        "expected_answer": "As the number of features increases, data becomes sparse in the feature space, distances become less informative, and more data may be required to learn reliable patterns."
    },

    {
        "question": "How can the curse of dimensionality be reduced?",
        "expected_answer": "Use feature selection, dimensionality reduction, domain knowledge, regularization, or collect more representative training data."
    },

    {
        "question": "What is the difference between L1 and L2 regularization mathematically?",
        "expected_answer": "L1 adds a penalty proportional to the sum of absolute parameter values, while L2 adds a penalty proportional to the sum of squared parameter values."
    },

    {
        "question": "Why can L1 regularization perform feature selection?",
        "expected_answer": "The absolute-value penalty can drive some coefficients exactly to zero, effectively removing the corresponding features from the model."
    },

    {
        "question": "Why does L2 regularization usually not produce exactly zero coefficients?",
        "expected_answer": "The squared penalty smoothly shrinks coefficients toward zero but normally does not force them exactly to zero."
    },

    {
        "question": "What is Elastic Net regularization?",
        "expected_answer": "Elastic Net combines L1 and L2 regularization, providing both feature-selection behavior and coefficient shrinkage."
    },

    {
        "question": "What is maximum likelihood estimation?",
        "expected_answer": "Maximum likelihood estimation chooses model parameters that make the observed training data most probable under the assumed statistical model."
    },

    {
        "question": "What is maximum a posteriori estimation?",
        "expected_answer": "MAP estimation combines the likelihood of the observed data with a prior distribution over parameters and chooses parameters with the highest posterior probability."
    },

    {
        "question": "What is the relationship between regularization and Bayesian priors?",
        "expected_answer": "Certain regularization penalties can be interpreted as imposing particular priors on model parameters. For example, L2 regularization corresponds to a Gaussian prior under common assumptions."
    },

    {
        "question": "What is convex optimization and why is it useful in Machine Learning?",
        "expected_answer": "In convex optimization, every local minimum is also a global minimum. This can make optimization problems easier to solve reliably."
    },

    {
        "question": "Why can neural-network optimization be more difficult than linear regression?",
        "expected_answer": "Neural networks have highly nonlinear objectives with many parameters and potentially complex optimization landscapes, making training more challenging."
    },

    {
        "question": "What is momentum in gradient descent?",
        "expected_answer": "Momentum uses previous parameter updates to influence the current update, helping optimization move consistently in useful directions and reducing oscillations."
    },

    {
        "question": "What is Adam optimizer?",
        "expected_answer": "Adam is an adaptive optimization algorithm that maintains moving estimates of gradients and squared gradients to adapt the learning rate for each parameter."
    },

    {
        "question": "What is the difference between Adam and standard gradient descent?",
        "expected_answer": "Standard gradient descent typically uses a shared learning-rate strategy, while Adam adapts updates using estimates of first and second moments of gradients."
    },

    {
        "question": "Why can a poorly chosen learning rate prevent convergence?",
        "expected_answer": "A very large learning rate can overshoot useful regions, while a very small learning rate can make optimization extremely slow or practically ineffective."
    },

    {
        "question": "What is a saddle point in optimization?",
        "expected_answer": "A saddle point is a point where the objective has directions of both increasing and decreasing values, so it is not a local minimum even though the gradient may be zero."
    },

    {
        "question": "What is ensemble learning?",
        "expected_answer": "Ensemble learning combines multiple models to produce a prediction that can be more accurate or robust than an individual model."
    },

    {
        "question": "What is stacking?",
        "expected_answer": "Stacking combines predictions from multiple base models and trains another model, called a meta-model, to make the final prediction."
    },

    {
        "question": "What is blending?",
        "expected_answer": "Blending combines predictions from multiple models using a separate validation set or another fixed dataset to train or determine the final combination."
    },

    {
        "question": "What is out-of-bag evaluation in Random Forest?",
        "expected_answer": "Each bootstrap sample leaves some training examples unused for a particular tree. These out-of-bag examples can be used to estimate model performance without a separate validation set."
    },

    {
        "question": "What is feature importance in Random Forest?",
        "expected_answer": "Feature importance estimates how much each feature contributes to reducing impurity or improving predictions across the ensemble, depending on the importance method."
    },

    {
        "question": "Why can impurity-based feature importance be misleading?",
        "expected_answer": "It can favor high-cardinality or continuous features and may give misleading importance when features are correlated."
    },

    {
        "question": "What is permutation feature importance?",
        "expected_answer": "Permutation importance measures the performance decrease caused by randomly shuffling a feature while keeping other data unchanged."
    },

    {
        "question": "What is SHAP?",
        "expected_answer": "SHAP is an explainability method based on Shapley values that estimates how individual features contribute to a particular model prediction."
    },

    {
        "question": "What is the difference between global and local model explainability?",
        "expected_answer": "Global explainability describes overall model behavior, while local explainability explains why the model produced a particular prediction for an individual example."
    },

    {
        "question": "What is partial dependence?",
        "expected_answer": "A partial dependence plot shows the average predicted response as one or more features vary while averaging over other features."
    },

    {
        "question": "What is calibration in classification?",
        "expected_answer": "Calibration describes how closely predicted probabilities correspond to actual observed frequencies. A well-calibrated model's predictions can be interpreted as probabilities."
    },

    {
        "question": "What is the difference between discrimination and calibration?",
        "expected_answer": "Discrimination measures how well a model separates classes, while calibration measures how accurately predicted probabilities correspond to observed outcomes."
    },

    {
        "question": "What is threshold tuning in classification?",
        "expected_answer": "Threshold tuning changes the probability cutoff used to convert predicted probabilities into class labels to achieve a desired tradeoff between errors."
    },

    {
        "question": "Why should the classification threshold not always be 0.5?",
        "expected_answer": "The best threshold depends on class imbalance, probability calibration, and the relative costs of false positives and false negatives."
    },

    {
        "question": "How would you handle a highly imbalanced fraud-detection problem?",
        "expected_answer": "Use appropriate metrics such as precision-recall measures, class weighting or suitable resampling, threshold tuning, and possibly anomaly-detection techniques depending on the problem."
    },

    {
        "question": "What is oversampling?",
        "expected_answer": "Oversampling increases representation of minority-class examples in the training data, either by duplicating samples or generating new synthetic examples."
    },

    {
        "question": "What is SMOTE?",
        "expected_answer": "SMOTE generates synthetic minority-class examples by interpolating between existing minority samples rather than simply duplicating them."
    },

    {
        "question": "What is a risk of applying SMOTE before train-test splitting?",
        "expected_answer": "It can cause information from the future validation or test set to influence generated training examples, resulting in data leakage."
    },

    {
        "question": "How should SMOTE be used safely?",
        "expected_answer": "Apply SMOTE only to the training portion of each cross-validation split, preferably through a pipeline that keeps preprocessing and sampling inside the training workflow."
    },

    {
        "question": "What is concept drift?",
        "expected_answer": "Concept drift occurs when the relationship between input features and the target changes over time."
    },

    {
        "question": "What is data drift?",
        "expected_answer": "Data drift occurs when the distribution of input features changes between the training environment and the production environment."
    },

    {
        "question": "What is prediction drift?",
        "expected_answer": "Prediction drift occurs when the distribution of model predictions changes over time, which may indicate changes in input data or underlying behavior."
    },

    {
        "question": "How can model drift be detected?",
        "expected_answer": "Monitor input distributions, prediction distributions, data quality, and model performance when labels become available, using statistical or business-level monitoring."
    },

    {
        "question": "What is covariate shift?",
        "expected_answer": "Covariate shift occurs when the distribution of input features changes between training and deployment while the conditional relationship with the target is assumed to remain relatively stable."
    },

    {
        "question": "What is target leakage?",
        "expected_answer": "Target leakage occurs when a feature contains information about the target that would not be available at the time the prediction is actually made."
    },

    {
        "question": "How would you identify suspiciously high model performance?",
        "expected_answer": "Check for data leakage, duplicate records, incorrect train-test splitting, target-related features, temporal leakage, and evaluation mistakes."
    },

    {
        "question": "Why is random train-test splitting dangerous for time-series data?",
        "expected_answer": "Random splitting can allow future information to appear in training while earlier observations are used for testing, producing unrealistic performance."
    },

    {
        "question": "How should time-series data usually be split?",
        "expected_answer": "Use chronological splits so training data comes from earlier periods and validation or testing data represents later periods."
    },

    {
        "question": "What is nested cross-validation?",
        "expected_answer": "Nested cross-validation uses an inner loop for model or hyperparameter selection and an outer loop for unbiased evaluation of the complete selection process."
    },

    {
        "question": "Why can tuning hyperparameters on the test set be problematic?",
        "expected_answer": "Repeatedly using the test set to make modeling decisions causes information from the test set to influence development, making the final evaluation overly optimistic."
    },

    {
        "question": "What is the difference between validation and test data in a mature ML workflow?",
        "expected_answer": "Validation data helps make modeling decisions and tune the system, while the test set should remain untouched until final evaluation."
    },

    {
        "question": "What is cross-validation leakage?",
        "expected_answer": "Cross-validation leakage occurs when information from validation folds influences training or preprocessing for those folds, producing an overly optimistic estimate."
    },

    {
        "question": "Why should preprocessing be inside a cross-validation pipeline?",
        "expected_answer": "This ensures each preprocessing step is fitted only on the training portion of each fold and prevents information from the validation fold leaking into training."
    },

    {
        "question": "How would you handle categorical features with many unique values?",
        "expected_answer": "Possible approaches include grouping rare categories, target encoding with leakage-safe cross-validation, hashing, embeddings, or suitable tree-based methods."
    },

    {
        "question": "What is target encoding?",
        "expected_answer": "Target encoding replaces a category with statistics derived from the target, such as a category's average target value. It must be performed carefully to avoid leakage."
    },

    {
        "question": "Why can target encoding cause data leakage?",
        "expected_answer": "If the target value of the current validation or training example is directly used to calculate its encoded feature, the feature contains information that would not be available at prediction time."
    },

    {
        "question": "What is the difference between normalization and standardization?",
        "expected_answer": "Normalization commonly rescales values to a bounded range, while standardization centers values around zero and scales them according to standard deviation."
    },

    {
        "question": "When is standardization especially useful?",
        "expected_answer": "It is often useful for algorithms based on distances or gradient optimization, such as KNN, SVM, logistic regression, and many neural-network models."
    },

    {
        "question": "When might tree-based models not require feature scaling?",
        "expected_answer": "Decision trees and many tree ensembles split based on feature thresholds and are generally not sensitive to differences in feature scale."
    },

    {
        "question": "What is monotonicity in Machine Learning models?",
        "expected_answer": "A monotonic relationship means predictions consistently increase or decrease as a feature changes, subject to the model's specified constraints."
    },

    {
        "question": "What is model interpretability?",
        "expected_answer": "Model interpretability describes how easily humans can understand the reasoning, structure, or important factors behind model predictions."
    },

    {
        "question": "Why can highly accurate models still be unsuitable for production?",
        "expected_answer": "A model can have high offline accuracy but fail because of latency, data drift, fairness issues, poor calibration, unavailable features, high operating cost, or unreliable data."
    },

    {
        "question": "What is the difference between offline and online model evaluation?",
        "expected_answer": "Offline evaluation uses historical or held-out data, while online evaluation measures behavior in the real production environment, often using controlled experiments."
    },

    {
        "question": "What is A/B testing for Machine Learning systems?",
        "expected_answer": "A/B testing compares different model versions by exposing different user groups to them and measuring predefined business or system metrics."
    },

    {
        "question": "What is shadow deployment?",
        "expected_answer": "Shadow deployment sends production inputs to a new model while keeping its predictions from affecting real decisions, allowing safe evaluation under realistic traffic."
    },

    {
        "question": "What is canary deployment for an ML model?",
        "expected_answer": "Canary deployment gradually exposes a new model to a small portion of production traffic before increasing its usage if performance and reliability remain acceptable."
    },

    {
        "question": "What is model versioning?",
        "expected_answer": "Model versioning tracks different trained model artifacts, their configurations, training data references, code, and evaluation results so deployments can be reproduced and rolled back."
    },

    {
        "question": "What is reproducibility in Machine Learning?",
        "expected_answer": "Reproducibility means being able to recreate the same or sufficiently equivalent results using recorded data, code, configurations, dependencies, and random seeds where appropriate."
    },


        

    ]
}