import nltk
from docx import Document
from pdfminer.high_level import extract_text
import bs4 as bs
import urllib.request
import wikipedia
from gensim.summarization import keywords
import RAKE
import operator

stopwords = nltk.corpus.stopwords.words('english')

text = '''

Machine Learning (ML) is essentially extracting knowledge 
from data sets. It is a topic at the intersection of statistics, 
artificial intelligence, and computer science and covers the 
topic of predictive analytics and statistical learning. The 
application of machine learning methods has in recent years 
become common in our lives. Over the past decade, machine 
learning has produced self-driving cars, practical speech 
recognition, effective web search, and a understanding of the 
human genome. Additionally, Artificial Intelligence (AI) is a 
branch of computer science which studies building machines 
capable of intelligent behavior, while Stanford University 
defines machine learning as  the science of getting computers 
to act without being explicitly programmed .  1  Clearly 
Machine Learning is a subset of Artificial Intelligence topic. 
Also, Deep Learning (DL) is a subfield of machine learning 
concerned with algorithms inspired by the structure and 
function of the brain called artificial neural networks. Deep 
learning in terms of the algorithms ability to discover and 
learn good representations using feature learning. This paper 
will discuss some aspects of deep learning as well. 
 Machine Learning extracts value from big and 
disparate data sources with far less reliance on human 
direction. It is data driven and runs at machine scale. It is well 
suited to the complexity of dealing with disparate data 
sources and the huge variety of variables and amounts of data 
involved. And unlike traditional analysis, machine learning 
thrives on growing datasets. The more data fed into a machine 
learning system, the more it can learn and apply the results to 
insights. 
The goal and usage of Machine Learning is to build new and 
leverage existing algorithms to learn from datasets, in order 
to build generalizable models that give accurate predictions, 
or to find patterns, particularly with new and unseen similar 
data. Traditionally, the insights were gathered from data sets 
by manually developing decision rules. This is feasible for 
some applications, particularly those in which humans have 
a good understanding of the process to model. However, 
using hand coded rules to make decisions has disadvantages. 
First, process logic requires a decision specific to a single 
task. Changing the task even slightly might require rewrite of 
the whole rule system. Second, designing rules requires a 
deep understanding of how a decision should be made by a 
human expert. Using machine learning, however, simply 
presenting a program with a dataset is enough for an 
algorithm to determine the insights. 2 
In a typical Machine Learning dataset, the rows can be 
thought observations or data points and the columns for each 
data point represents the features of that observation and their 
values. Each entity or row is called a sample (or data point), 
the columns, which describe these entities as features. 
In a machine learning process, a dataset is usually split into 
multiple subsets. The minimum subsets are the training and 
test datasets, and often an optional third validation dataset is 
created as well. Once these data subsets are created from the 
primary dataset, a predictive model or classifier is trained 
using the training data, and then the model’s predictive 
accuracy is determined using the test data. 
As discussed, machine learning leverages algorithms to 
automatically model and find patterns in data, usually with 
the intention of predicting some target output. ML algorithms 
are heavily based on statistics and mathematical 
optimization. In a summary, machine learning automatically 
learns a highly accurate predictive or classifier model, or 
finding unknown patterns in data, by leveraging learning 
algorithms and optimization techniques. 
Machine learning algorithms can be categorized in following 
major areas, including, supervised, unsupervised, and semi
supervised learning. We will focus on the first two set of 
algorithms in this paper. 
In supervised learning, the data contains a label which is the 
response variable that is being modeled, and with the goal 
being that algorithm predicts the value or class of the unseen 
data. Machine learning algorithms that learn from 
input/output pairs are called supervised learning algorithms 
because a  supervisor  provides guidance to the algorithms 
in the form of the desired outputs for each dataset they learn 
from. Supervised learning algorithms are well understood 
and their performance is easy to measure. Supervised 
machine learning will likely solve the problem, if the 
application can be modelled as a supervised learning 
problem, and the dataset that includes the desired outcome. 
There are many examples of supervised machines learning 
algorithms. For example, predicting the equipment health and 
failure based on historical data of equipment data, Image 
analysis of an astronomical phenomenon based on a large 
collection of images, prediction of sport team performance 
based on historical datasets and many more. Again, the key 
here is to collect a dataset and run it through a machine 
learning algorithm and seek desired outcomes. 
Unsupervised learning involves learning from a dataset that 
has no label or response variable, and is therefore more about 
finding patterns than prediction. In an unsupervised learning, 
only the input data is known, and output data is not given to 
the algorithm. Unsupervised learning can be harder to 
understand and evaluate. There are several examples of 
unsupervised learning. Tagging people with their photos 
from a collection of pictures, tagging drugs based on the 
molecules structure and many more. 
Hence, considering the above machine learning types, the 
alternative is to write explicit code program to seek through 
the data, and that understands the stats, thresholds to take into 
account for each stat, and so forth. It would take a substantial 
amount of time to write the code, and different programs 
would need to be written for every problem needing an 
answer. 
3. SUPERVISED LEARNING ALGORITHMS 
There are two major types of supervised machine learning 
algorithms, namely classification and regression. All the 
supervised machine learning algorithm can be seen as either 
classification or regression. 
In classification, the goal is to predict a class label, which is 
a choice from a predefined list of possibilities. For example, 
identifying a set of people from photos. Classification is 
sometimes separated into binary classification, which is the 
special case of identifying two classes, and multiclass 
classification, which is classification between more than two 
classes. Binary classification is answering a yes/no question. 
Classifying emails as either spam or not spam is an example 
of a binary classification problem. 
In regression, the objective is to predict a continuous number 
with a value. Predicting a person’s annual income from their 
education, their age, and where they live is an example of a 
regression task.  2  When predicting income, the predicted 
value is an amount, and can be any number in a given range. 
An easy way to differentiate between classification and 
regression tasks is to look for continuity in the possible 
outcomes, if it is, then the problem is a regression problem. 
In supervised learning, if a model is able to make accurate 
predictions on data, it is said to generalize from the training 
set to the test data set. The goal is to build a model that is able 
to generalize as accurately as possible. Usually the models 
are built in such a way that it can make accurate predictions 
on the training set. If the training and test sets have enough in 
common, one would expect the model to also be accurate on 
the test set. However, there are some cases where this can go 
wrong. If we allow ourselves to build very complex models, 
we can always be as accurate as we like on the training set. 
Hence the objective is to find the simplest model. Building a 
model that is too complex for the dataset is called overfitting. 
Overfitting occurs when the model is too close to the nature 
of the training set and a model that works well on the training 
set but is not able to generalize to new datasets. Now, if model 
is too simple, then you are unable to capture all the aspects of 
and variability in the data, and your model will do badly even 
on the training set. Choosing too simple of a model is called 
under fitting. The more complex the model, the better we will 
be able to predict on the training data. However, if model 3 
becomes too complex, then it becomes too individualized for 
the given data point in the training set, and the model will not 
generalize well to new data. Hence, the key is to find the 
sweet spot that will yield the best generalization performance. 

The k-NN algorithm is simple machine learning algorithm. 
The algorithm makes a prediction for a new data point, by 
finding the closest data points in the training dataset, hence 
its nearest neighbor. In its simplest version, the k-NN 
algorithm only considers exactly one nearest neighbor, which 
is the closest training data point to the point for prediction. 
The prediction is then simply the known output for this 
training point. In addition to considering only the closest 
neighbors, we can also consider an arbitrary number of, k 
neighbors, hence the naming, k-nearest neighbor’s algorithm. 
When considering more than one neighbor, voting can be 
used to to assign a label. In other words, for each test point, 
count many neighbors belong to class 0 and class 1. Finally, 
assigning the class that is most frequent, the majority class 
among the k-nearest neighbors. There is also a regression 
variant of the k-nearest neighbors algorithm. Here also, one 
can use more than the single closest neighbor for regression. 
When using multiple nearest neighbors, the prediction is the 
average, or mean, of the relevant neighbors. 
One of the strengths of k-NN model is that, it is very easy to 
understand, and often gives good performance. Developing 
the nearest neighbors model is also very agile, however when 
training set is very large (either in number of features or in 
number of samples) prediction can be slow. Hence, when 
using the k-NN algorithm, it’s important to preprocess data, 
which may serve many purposes including not allowing one 
feature to dominate. This approach often does not perform 
well on datasets with large features. So, while the nearest k
neighbors algorithm is easy to understand, it is not often used 
in practice, due to prediction being slow and its inability to 
handle many features.  2  
Linear Models 
Linear models make a prediction using a linear function of 
the input features 
In this model w 0  is the slope and b is the y-axis offset. For 
more features, w contains the slopes along each feature axis. 
Lets look at 2 forms of Linear Regression models. 
Ordinary least squares 
Linear regression, or ordinary least squares (OLS), is the 
simplest linear method for regression, which calculates the 
parameters w and b that minimize the mean squared error 
between predictions and the true regression targets, y, on the 
training set. The mean squared error is the sum of the squared 
differences between the predictions and the true values, 
divided by the number of samples. There are five OLS 
assumptions that are extremely important. If the OLS 
assumptions hold, then according to Gauss-Markov 
Theorem, OLS estimator is Best Linear Unbiased Estimator. 
The assumptions can be summarized into the following. First, 
linear regression model is linear in parameters. Second, there 
should be a random sampling of observations. Third, 
conditional mean should be zero. Fourth, there is no multi
collinearity (or perfect collinearity). Fifth, There is no auto 
correlation. 
Ridge Regression 
Ridge regression is also a linear model for regression, and 
leverages the same model as ordinary least squares. In ridge 
regression, the coefficients (w) fit an additional constraints 
and to predict well. Additionally, w should be close to zero. 
This implies that feature should have as little effect on the 
outcome as possible. This constraint is called regularization, 
which restricts a model to avoid overfitting. 
Linear models for classification 
Classification also utilizes Linear models. In this case, a 
prediction is made using the following formula: 
 
The formula is very similar to linear regression, the only 
difference being, instead of returning the weighted sum of the 
features, the threshold prediction values at zero. If the 
function is smaller than zero, the prediction is class –1; if it 
is larger than zero, prediction is class +1. In linear models for 
classification, the decision boundary is a linear function of 
the input. Hence, linear classifier is a classifier that separates 
two classes using a line, a plane, or a hyperplane. 
There are a variety of learning algorithms for linear models. 
These algorithms have several uniqueness. For example, the 
approach to measure a particular combination of coefficients 
and intercept fits the training data. Different algorithms 
choose their own approaches to measure fitting the training 
set. The two most common linear classification algorithms 
are logistic regression, and linear support vector machines 
(linear SVMs). 
Linear models for multiclass classification 
Typically, linear classification models are utilized for binary 
classification only. A common technique to extend a binary 
classification algorithm to a multiclass classification 
algorithm is the one-vs.-rest approach. In this approach, a 
binary model is learned for each class, resulting in as many 
binary models as there are classes. To make a prediction, all 
binary classifiers are run on a test point. The classifier with 
the highest score in its single class is selected and its class 
label is returned as the prediction. In a single binary classifier 
per class results in one vector of coefficients (w) and one 
intercept (b) for each class. The class for which the result of 
the classification confidence formula given here is highest is 
the assigned class label: 
w 0  * x 0  + w 1  * x 1  + ... + w p  * x p  + b 
The approach in multiclass logistic regression differ 
somewhat from the one-vs.-rest approach, but they also result 
in one coefficient vector and intercept per class, and the same 
method of making a prediction is applied. 
Naive Bayes Classifiers 
Naive Bayes classifiers are a family of classifiers that are 
similar to the linear models, however is more efficient and 
faster in performance. Bayes models are efficient because 
they learn parameters by looking at each feature individually 
and collect simple per-class statistics from each feature. The 
naive Bayes models share many of the strengths and 
weaknesses of the linear models. They are very fast to train 
and to predict, and the training procedure is easy to 
understand. The models implement well with high
dimensional sparse data and are relatively robust to the 
parameters. Naive Bayes models are great baseline models 
and are often used on very large datasets, where training even 
a linear model might take too long. 
Decision Trees 
Decision trees are common models for classification and 
regression learning. Decision Trees learn a hierarchy of 
if/else questions, hence deriving a decision. 
Decision trees Construction 
Building a decision tree requires to partition the data sets in 
sections and applying if/then else questions to the datasets. In 
the machine learning, these questions are called tests. A leaf 
of the tree that contains data points that all share the same 
target value is called pure. Typically, data does not come in 
the form of binary yes/no, hence the tests that are used on 
continuous data are of the form feature x larger than value y. 

A prediction on a new data point is made by testing which 
region of the partition of the feature space the point lies in. 
The region can be found by traversing the tree from the root 
and going left or right, depending on whether the test is 
fulfilled or not. Trees can also be utilized for regression tasks, 
using exactly the same technique. To make a prediction, the 
tree is traversed based on the tests in each node to find the 
leaf the new data point falls into. The output for this data 
point is the mean target of the training points in this leaf. 
Decision trees have two advantages as compared to other 
algorithms. First, the ease of model visualization, and second, 
the algorithms are completely invariant to scaling of the data. 
As each feature is processed separately, and the possible 
splits of the data don’t depend on scaling, no preprocessing 
like normalization or standardization of features is required 
for decision tree algorithms. In particular, decision trees work 
well when you have features that are on completely different 
scales, or a mix of binary and continuous features. The main 
disadvantage of decision trees is that even with the use of pre
pruning, they tend to overfit and provide poor generalization 
performance. Therefore, in most applications, the ensemble 
methods we discuss next are usually used in place of a single 
decision tree. 
Ensembles of Decision Trees 
Ensembles are methods that combine multiple machine 
learning models to create more powerful models. The two 5 
ensemble models that get deployed on a wide range of 
datasets for classification and regression, that also use 
decision trees are random forests and gradient boosted 
decision trees. 
Random forests 
Random forest address the overfitting the training data, which 
is a short coming of decision trees. A random forest is 
essentially a collection of decision trees, where each tree is 
slightly different from the others. The approach behind 
random forests is that each tree individually will predict well, 
but will likely overfit on part of the data. Hence, one can 
average the overfitting results of all the decision trees. This 
approach is called random forest because it injects 
randomness into the tree building hence ensuring each tree is 
different. There are other ways to randomize: by selecting the 
data points used to build a tree and by selecting the features 
in each split test. 
Gradient Boosted Trees 
The gradient boosted tree is also an ensemble method that 
combines multiple decision trees to create a more powerful 
model. These models can be used for regression and 
classification. Gradient boosting algorithm works by building 
trees in a serial manner, where each tree corrects the mistakes 
of the previous one. There is no randomization in gradient 
boosted trees and are utilized for shallow trees, of depth one 
to five, which makes the model smaller in terms of memory 
and makes predictions faster. Gradient boosting iteratively 
improve performance by combining many simple models, 
where each tree can only provide good predictions on it part. 
Gradient Boosted Trees are typically sensitive to parameter 
settings than random forests, but can provide better accuracy 
if the parameters are set correctly. 
Kernelized Support Vector Machines 
Another type of supervised learning is kernelized support 
vector machines. Kernelized support vector machines (just 
referred to as SVMs) are an extension that allows for more 
complex models that are not defined simply by hyperplanes 
in the input space. 
During training, the SVM learns the data points 
representation of the decision boundary between the two 
classes. Typically only a subset of the training points matter 
for defining the decision boundary: the ones that lie on the 
border between the classes. These are called support vectors 
and give the support vector machine its name. To make a 
prediction for a new point, the distance to each of the support 
vectors is measured and a classification decision is made 
based on the distances to the support vector. The distance 
between data points is measured by the Gaussian kernel: 

4. UNSUPERVISED LEARNING ALGORITHMS 
In unsupervised learning there is no known output, no 
training data set to instruct the learning algorithm. In 
unsupervised learning, the learning algorithm is just given the 
input data to extract knowledge from this data. 
Transformation and Clustering 
Unsupervised transformations of a dataset are algorithms that 
create a new formation of the data which could easier for 
humans or other machine learning algorithms to understand 
compared to the original representation of the data.  3  
Dimension reduction, where high-dimensional representation 
of the data, consisting of many features, and summarizes the 
essential characteristics with fewer features, is a common 
application of transformation. This is useful for visualization 
purposes. There are other applications for unsupervised 
transformations, which entail finding the components that of 
the data. An example of this is topic extraction on collections 
of text documents. The transformational algorithm finds 
topics that are discussed in each document. 
Clustering algorithms, partitions data into separate groups of 
similar items. Consider the example of selecting species of 
certain animal kingdom based on photos. Here is the 
approach would be to extract all the phots and divide them 
into groups of groups of species that look similar. 
Transforming data applications can be visualization, 
compressing the data, and finding a representation that is 
more useful for other applications. Principal Component 
Analysis (PCA) approach is most commonly used for data 
transformations. There are also other algorithms like non
negative matrix factorization (NMF), Singular Value 
Decomposition (SVD), Linear discriminant analysis 
(LDA) and t-SNE. 
Principal Component Analysis (PCA) 
Principal component analysis is a method that rotates the 
dataset in a way such that the rotated features are statistically 
uncorrelated.  4  This rotation is often followed by selecting 
only a subset of the new features, according to how important 
they are for explaining the data. 
PCA is an unsupervised method, and does not use any class 
information when finding the rotation, it only considers the 
correlations in the data. 
Non-Negative Matrix Factorization (NMF) 
Non-negative matrix factorization algorithm extract useful 
features from a data set. It works similarly to PCA and can 
also be used for dimensionality reduction. In NMF, want the 
components and the coefficients for manipulation have to be 
greater than or equal to zero. As a result, this approach applies 
to data where each feature is non-negative, as a non-negative 
sum of non-negative components cannot become negative. 
NMF leads to more understandable components than PCA, as 
negative components and coefficients can lead to hard-to
interpret cancellation effects. 
Learning with t-SNE 
Just like PCA, there is a class of algorithms for visualization 
allow which allow more complex mappings, and provide 
better visualizations. t-SNE algorithm is one of this class of 
algorithm. Manifold learning algorithms are usually used for 
visualization, to compute a new representation of the training 
data, but don’t allow transformations of new data. Hence, 
they can only transform the data they were trained for. 
Manifold learning is useful for exploring data, but is typically 
not used for the final goal is supervised learning. The main 
goal behind t-SNE is to find a two-dimensional 
representation of the data that preserves the distances 
between points as best as possible. t-SNE starts with a 
random two-dimensional representation for each data point, 
and then makes points that are close in the original feature 
space closer, and points that are far apart in the original 
feature space farther apart. t-SNE focus on points that are 
close by, rather than preserving distances between far-apart 
points. As a result, it preserves the information on points that 
are neighbors to each other. 
Clustering 
Similar to Classification clustering, it is the task of 
partitioning the dataset into groups. Clustering splits up the 
data points within a single cluster and predict a number to 
each data point, depicting cluster a particular point belongs 
to. 
k-Means Clustering 
k-means clustering is a commonly used clustering 
algorithms, that finds cluster centers for certain sample of the 
data. The algorithm follows two steps. First, assigning each 
data point to the closest cluster center, and second, each 
cluster center as the mean of the data points that are assigned 
to it. The algorithm is finished when the assignment of 
instances to clusters no longer changes. 
Agglomerative Clustering 
Agglomerative clustering is a collection of clustering 
algorithms that leverages traditional clustering approaches. 
Including, declaring each point its own cluster, and then 
merges the two most similar clusters until some stopping 
criterion is met. There are several connected criteria that 
specify the most similar cluster is measured. This measure is 
always defined between two existing clusters. 
4. SAMPLE USE CASES 
Data Security 
Malware has several applications for security. The signature 
of malware are collected and ML algorithms are used to 
predict the nature of attack. In other situations, machine 
learning algorithms can look for patterns in how data in the 
cloud is accessed, and report anomalies that could predict 
security breaches. 
Financial Trading 
Humans can’t possibly do the same tasks as machines when 
it comes to consuming vast quantities of data or the speed 
with which they can execute a trade. Machine learning 
algorithms are getting closer to predict the stock market 
behavior. Many trading firms use ML systems to predict and 
execute trades at high speeds and high volume and, can turn 
huge profits for the firms. 
Healthcare 
Machine learning algorithms can process more information 
and spot more patterns than their human medical doctors. 
One study used computer assisted diagnose (CAD) when to 
review the early mammography scans of women who later 7 
developed breast cancer, and the computer spotted 52% of the 
cancers as much as a year before the women were officially 
diagnosed.  6  Additionally, machine learning can be used to 
understand risk factors for disease in large populations. Also 
another example of ML in Health care is image analysis of 
radiology images, ML algorithms can do this easily and 
enhance patient care and diagnosis. 
Aerospace 
There are many use cases in aerospace industry, including 
image analysis and prediction of celestial objects behavior 
and attributes. Also predictive maintenance of aerospace 
equipment as the components age and are use. Aerospace was 
an early adopter of AI/ML. In fact, many pilots have been 
flying with very primitive forms of ML for years, autopilots 
systems all use computer power to make intelligent decisions. 
Additionally, applying real AI to an autopilot, instead of just 
programming it to fly certain pre-planned profiles, machine 
learning makes it a more resilient autopilot that can adapt to 
changing conditions.  5  
Computer Network 
Machines Learning is quickly being applied to Network in 
form of Network Analytics. Telemetry from network 
elements is being gather and machine learning algorithms are 
applied to provide application mapping, security anomalies 
detection, security forensics and networking configuration 
recommendations. 


'''


def text_file(file):
    rf = file[::-1].index('.')
    extension = file[-1 * rf:]
    print(extension)
    if extension == 'txt':

        f = open(file, 'r')
        try:
            text = f.read()
            # print(text)
        except UnicodeDecodeError:
            pass

    elif extension == 'docx':

        text = ''
        f = Document(file)
        for i in f.paragraphs:
            text += i.text

    elif extension == 'pdf':

        text = extract_text(file)

    else:
        print("Please upload correct file !!!")
        return 0

    return text


def get_text_from_link(urllink):
    if urllink.find('wikipedia.org') != -1:
        result = urllink.find('wikipedia.org/wiki/')
        wiki = wikipedia.page(urllink[result + 19:])
        text = wiki.content
        text = text.replace('==', '')
        print(text)
        return text

    scraped_data = urllib.request.urlopen(urllink)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article, 'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    # article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    # article_text = re.sub(r'\s+', ' ', article_text)
    # formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    # formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    print(article_text)
    return article_text


def get_keywords(text):
    return (keywords(text).split('\n'))


def sort_tup(tup):
    tup.sort(key=lambda x: x[1])
    return tup


def get_keyphrases(text):
    stop_dir = "C:\\Users\\bhaskar\\Desktop\\FYP\\smartstoplist.txt"
    rakeobj = RAKE.Rake(stop_dir)

    lst = []
    keywords = sort_tup(rakeobj.run(text))
    for i in range(len(keywords)):
        if keywords[i][1] > 0 and len(keywords[i][0].split(' ')) > 1:
            lst.append(keywords[i][0])

    return lst[::-1]



