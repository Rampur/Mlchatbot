"""
Structured course data for BIS602 Machine Learning
Course Instructor: Rampur Srinath (Srinath Rampur)
National Institute of Engineering, Mysuru
Semester: VI, Section A & B | Term: 16/02/26 to 05/06/26
"""

MODULES = {
    "Module 1: Introduction to Machine Learning & Perceptron": {
        "description": "Foundations of ML, types of learning, perceptron algorithm, Adaline, gradient descent",
        "sessions": {
            1: "Introduction to POs, COs, syllabus and evaluation pattern. ML – Past, Present and Future.",
            2: "The three different types of machine learning. Supervised learning for predictions. Classification for predicting class labels.",
            3: "Regression for predicting continuous outcomes. Reinforcement learning – solving interactive problems.",
            4: "Unsupervised learning – discovering hidden structures. Clustering for finding subgroups. Dimensionality reduction for data compression.",
            5: "Basic terminology and notations. Roadmap for building ML systems. Preprocessing – getting data into shape.",
            6: "Training and selecting a predictive model. Evaluating models and predicting unseen data instances.",
            7: "Artificial neurons – early history of machine learning.",
            8: "Implementing a perceptron learning algorithm in Python. Training on the Iris dataset.",
            9: "Perceptron continued – training a perceptron model on the Iris dataset.",
            10: "Adaptive linear neurons (Adaline) and convergence of learning. Minimizing cost functions with gradient descent.",
            11: "Discussion and revision of Module 1.",
        },
        "test_info": "TEST-1: Sessions 1-20 | Quiz-1: Sessions 1-25",
    },
    "Module 2: ML Classifiers Using Scikit-learn": {
        "description": "Logistic Regression, SVM, kernel methods, regularization",
        "sessions": {
            11: "Module 2 begins: A Tour of ML Classifiers Using Scikit-learn – Choosing a classification algorithm.",
            12: "Scikit-learn classifiers – choosing a classification algorithm (continued).",
            13: "Scikit-learn classifiers continued.",
            14: "Training a logistic regression model with Scikit-learn.",
            15: "Modeling class probabilities via logistic regression. Logistic regression intuition and conditional probabilities.",
            16: "Tackling overfitting via regularization.",
            17: "Maximum margin classification with Support Vector Machines (SVM). Maximum margin intuition.",
            18: "SVM – maximum margin intuition continued.",
            19: "Dealing with non-linearly separable cases using slack variables. Alternative implementations in Scikit-learn.",
            20: "Solving non-linear problems using a kernel SVM. Using the kernel trick to find separating hyperplanes in higher-dimensional space.",
        },
    },
    "Module 3: Decision Trees, Ensemble Methods & Data Preprocessing": {
        "description": "Decision trees, Random Forests, K-NN, missing data, categorical data, feature scaling",
        "sessions": {
            21: "Discussion and revision of Module 2. Module 3 begins: Decision tree learning. Maximizing information gain. Building a decision tree.",
            22: "Combining weak to strong learners via Random Forests. K-Nearest Neighbors – a lazy learning algorithm.",
            23: "Building Good Training Sets – Data Preprocessing. Dealing with missing data.",
            24: "Eliminating samples/features with missing values. Imputing missing values. Understanding the Scikit-learn estimator API.",
            25: "Missing value handling continued – imputation and Scikit-learn estimator API.",
            26: "Handling categorical data. Mapping ordinal features.",
            27: "Encoding class labels. Performing one-hot encoding on nominal features.",
            28: "Partitioning a dataset into training and test sets.",
            29: "Bringing features onto the same scale (feature scaling/normalization). Selecting meaningful features.",
            30: "Sparse solutions with L1 regularization. Sequential feature selection algorithms.",
        },
        "test_info": "TEST-2: Sessions 21-43 | Quiz-1: Sessions 1-25 | Quiz-2: Sessions 26-43",
    },
    "Module 4: Dimensionality Reduction": {
        "description": "PCA (Principal Component Analysis), LDA (Linear Discriminant Analysis), Kernel PCA",
        "sessions": {
            31: "Discussion and revision of Module 3. Module 4 begins: Compressing Data via Dimensionality Reduction. Unsupervised dimensionality reduction via PCA.",
            32: "Total and explained variance. Feature transformation. PCA in Scikit-learn.",
            33: "Supervised data compression via Linear Discriminant Analysis (LDA). Computing the scatter matrices.",
            34: "Selecting linear discriminants for the new feature subspace. Projecting samples onto the new feature space.",
            35: "LDA via Scikit-learn.",
            36: "Using kernel PCA for nonlinear mappings. Kernel functions and the kernel trick.",
            37: "Implementing kernel PCA in Python – Example 1: separating half-moon shapes.",
            38: "Example 2: separating concentric circles.",
            39: "Projecting new data points. Kernel PCA in Scikit-learn.",
            40: "Kernel PCA in Scikit-learn continued.",
        },
    },
    "Module 5: Model Evaluation & Hyperparameter Tuning": {
        "description": "Pipelines, cross-validation, learning curves, performance metrics, ROC, confusion matrix",
        "sessions": {
            41: "Discussion and revision of Module 4. Module 5 begins: Learning Best Practices for Model Evaluation & Hyperparameter Tuning. Streamlining workflows with pipelines.",
            42: "Loading the Breast Cancer Wisconsin dataset. Combining transformers and estimators in a pipeline.",
            43: "Using k-fold cross-validation to assess model performance.",
            44: "The holdout method. K-fold cross-validation.",
            45: "Debugging algorithms with learning and validation curves. Diagnosing bias and variance problems.",
            46: "Learning curves continued – diagnosing bias and variance.",
            47: "Addressing overfitting and underfitting with validation curves.",
            48: "Looking at different performance evaluation metrics. Reading a confusion matrix.",
            49: "Optimizing precision and recall of a classification model.",
            50: "Plotting a Receiver Operating Characteristic (ROC). Scoring metrics for multi-class classification. Discussion and revision of Module 5. Model question paper discussion.",
        },
    },
}

COURSE_INFO = {
    "code": "BIS602",
    "title": "Machine Learning",
    "instructor": "Rampur Srinath (Srinath Rampur)",
    "department": "Information Science & Engineering",
    "institute": "The National Institute of Engineering, Mysuru",
    "semester": "VI (6th), Section A & B",
    "term": "16/02/26 to 05/06/26",
    "credits": "4:0:0 (L:T:P)",
    "textbooks": [
        "Raschka, S., & Mirjalili, V. (2019). Python Machine Learning (3rd ed.). Packt Publishing.",
        "Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (2nd ed.). O'Reilly Media.",
    ],
    "reference_books": [
        "Alpaydın, E. (2004). Introduction to Machine Learning. MIT Press.",
        "Rogers, S., & Girolami, M. (2011). A First Course in Machine Learning. Chapman & Hall/CRC.",
        "Kelleher, J. D. et al. (2015). Fundamentals of ML for Predictive Data Analytics. MIT Press.",
    ],
    "course_outcomes": [
        "CO1: Explain the basics of machine learning and its classifications. (L3)",
        "CO2: Illustrate the working of algorithms on classifications and data pre-processing techniques. (L2)",
        "CO3: Discuss the working of SVM, Decision trees & Dimensionality Reduction. (L3)",
        "CO4: Outline best practices for model evaluation. (L3)",
    ],
    "evaluation": {
        "CIE": {"Test-1": "25 marks", "Test-2": "25 marks", "Quiz-1": "10 marks", "Quiz-2": "10 marks", "Experiential Learning": "30 marks"},
        "SEE": "100 marks (20 marks from each module, choice in two modules, 3 hours)",
    },
}

SYSTEM_PROMPT = """You are an AI tutor for the BIS602 Machine Learning course at NIE, Mysuru taught by Rampur Srinath.

## COURSE CONTEXT (only answer from this syllabus)
Course Code: BIS602 | Credits: 4:0:0 | Semester: VI (6th)
Instructor: Rampur Srinath | Term: 16/02/26 to 05/06/26

### Modules & Sessions:

MODULE 1: Introduction to ML & Perceptron (Sessions 1-11)
- Types of ML: supervised, unsupervised, reinforcement learning
- Classification, regression, clustering, dimensionality reduction
- ML pipeline: preprocessing, training, evaluation, prediction
- Perceptron algorithm, Adaline (adaptive linear neurons), gradient descent
- Iris dataset implementation in Python

MODULE 2: ML Classifiers Using Scikit-learn (Sessions 11-20)
- Logistic regression: intuition, conditional probabilities, cost function
- Overfitting and regularization (L1, L2)
- Support Vector Machines (SVM): maximum margin, slack variables
- Kernel trick for non-linear problems (RBF, polynomial kernels)

MODULE 3: Decision Trees, Ensembles & Preprocessing (Sessions 21-30)
- Decision trees: information gain, building trees
- Random Forests: bagging, combining weak learners
- K-Nearest Neighbors (K-NN)
- Missing data: elimination vs imputation
- Categorical data: ordinal mapping, one-hot encoding
- Feature scaling, L1 regularization, sequential feature selection

MODULE 4: Dimensionality Reduction (Sessions 31-40)
- PCA (Principal Component Analysis): variance, feature transformation
- LDA (Linear Discriminant Analysis): scatter matrices, feature subspace
- Kernel PCA: half-moon shapes, concentric circles examples

MODULE 5: Model Evaluation & Tuning (Sessions 41-50)
- Pipelines: combining transformers and estimators
- Cross-validation: holdout method, k-fold
- Learning curves: bias-variance diagnosis
- Validation curves: overfitting vs underfitting
- Performance metrics: confusion matrix, precision, recall, F1, ROC, AUC
- Breast Cancer Wisconsin dataset

### Rules:
1. ONLY answer questions about topics in this syllabus.
2. If asked something outside ML or this syllabus, say: "This is outside the BIS602 ML syllabus. I can only help with topics taught by Rampur Srinath in this course."
3. Always reference the relevant module/session number when possible.
4. Keep answers concise and focused on course concepts.
5. Do not provide full code solutions – explain concepts and point to the relevant session.
6. Textbooks: Raschka & Mirjalili (2019), Geron (2019). Reference: Alpaydin (2004), Rogers & Girolami (2011), Kelleher et al. (2015)."""

SAMPLE_QA = [
    {
        "q": "What are the three types of machine learning?",
        "a": "1) Supervised Learning – making predictions using labeled data (classification & regression).\n2) Unsupervised Learning – discovering hidden patterns in unlabeled data (clustering & dimensionality reduction).\n3) Reinforcement Learning – solving interactive problems by learning from rewards/penalties.\n(Session 2-4, Module 1)",
    },
    {
        "q": "What is the perceptron algorithm?",
        "a": "The perceptron is the simplest artificial neuron, inspired by the early history of ML. It takes input features, multiplies them by weights, sums them, and passes through a step function to output a class label. It's a binary classifier trained using the perceptron learning rule, which updates weights when misclassifications occur. Implemented in Python on the Iris dataset in Sessions 8-9.",
    },
    {
        "q": "How does logistic regression differ from linear regression?",
        "a": "Linear regression predicts continuous values (e.g., price, temperature). Logistic regression predicts class probabilities using the sigmoid function, outputting values between 0 and 1. Despite the name, logistic regression is a classification algorithm. It models conditional probabilities P(y=1|x). (Sessions 14-15, Module 2)",
    },
    {
        "q": "What is the kernel trick in SVM?",
        "a": "The kernel trick allows SVM to solve non-linear problems by implicitly mapping data to a higher-dimensional space without computing the transformation explicitly. Common kernels: linear, polynomial, RBF (Gaussian). This finds separating hyperplanes in higher dimensions where data becomes linearly separable. (Session 20, Module 2)",
    },
    {
        "q": "What is the difference between PCA and LDA?",
        "a": "PCA (Principal Component Analysis) is unsupervised – it finds directions of maximum variance in data without using labels. LDA (Linear Discriminant Analysis) is supervised – it finds directions that maximize class separation. Both are dimensionality reduction techniques. (Sessions 31-35, Module 4)",
    },
    {
        "q": "How does k-fold cross-validation work?",
        "a": "The dataset is split into k equal folds. The model is trained on k-1 folds and tested on the remaining fold. This process repeats k times, each time using a different fold as the test set. The final performance is the average across all k iterations. Common choices: k=5 or k=10. This gives a more reliable estimate than a single train-test split. (Sessions 43-44, Module 5)",
    },
    {
        "q": "What metrics are used to evaluate classification models?",
        "a": "Key metrics: Accuracy, Precision, Recall (Sensitivity), F1-Score, Specificity, Confusion Matrix, ROC Curve, AUC (Area Under the Curve). Precision = TP/(TP+FP), Recall = TP/(TP+FN). The ROC curve plots TPR vs FPR at various thresholds. (Sessions 48-50, Module 5)",
    },
    {
        "q": "How do decision trees and random forests differ?",
        "a": "A decision tree splits data recursively based on feature values using criteria like information gain or Gini impurity. A Random Forest is an ensemble of many decision trees trained on bootstrapped data with random feature subsets – it averages their predictions, reducing overfitting and improving generalization. (Sessions 21-22, Module 3)",
    },
]
