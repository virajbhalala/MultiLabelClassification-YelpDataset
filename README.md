# Predicting Business Categories From Business Reviews Using Yelp Dataset

CS 410: Text Information System  UIUC

Team members and responsibilities
* **Viraj Bhalala**, Lead (Primarily resonsible for extracting different features from the text data, researching and applying different natural language processing and machine learning techniques, and preparing documents)
* **Dev Patel** (Primarily responsible for obtaining and cleaning data, performing exploratory analysis on the text data, and preparing analytical dataset for this project)

The goal of this project is to predict business categories from business reviews. We have particularly used Yelp dataset for this project. Moreover, this techniques can also be leveraged to many other multi label predicting applications such as categorizing products from reviews, categorizing documents such as emails, etc.


#### In this project we have used following libraries
* [SkLearn](http://scikit-learn.org/stable/) for training model
* [NLTK](http://www.nltk.org/) for NLP
* [Spacy](https://spacy.io) for NLP
* [Pandas](https://pandas.pydata.org/) for processing data
* [Numpy](http://www.numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [wordcloud](https://github.com/amueller/word_cloud) for creating word cloud

#### Requirements
* Python 3.6

All of the notebooks can be viewed here on github or can be tested locally by using [Jupyter](http://jupyter.org/)

#### Steps/Processes
1) DataPrep.ipynb - Preprcess and prepare data
2) ExploratoryAnalysis.ipynb - Data Exploratory Analysis
3) OneVsRestClassifier.ipynb - OneVsRestClassifier - MultiLabel Classifier
4) OneVsRestClassifierV2.ipynb - OneVsRestClassifier with more parameters
5) ResultTracker.csv - Result tracker for different tests

#### Other Tech Exploration
1) SpacyTextProcessing.ipynb
2) NLTKTest.ipynb
3) SpacyTextProcessing.ipynb


#### About OneVsRest Classifer and MultiLabel Classifiers
* [OneVsRest Classifer](http://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
* [MultiLabel Classifiers](https://en.wikipedia.org/wiki/Multiclass_classification)
