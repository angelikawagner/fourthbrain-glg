# FourthBrain Capstone: GLG Expert Finder

The scripts in this repo are for model development. The repo for the web application can be found [here](ttps://github.com/exp-ouroborous/fourthbrain-capstone-ui).

### Contributors
- Angelika Wagner <angelika.wagner0220@gmail.com>
- Awais Shah <shah.awais77@gmail.com>
- Binit Mohanty <binit.mohanty@gmail.com>

### Skills
- Natural language processing (NLP), unsupervised learning, topic modelling, hierarchical clustering, LDA, HLDA, word embedding, named entity recognition, model deployment, REST API,  web application, experiment tracking, data engineering, cloud computing

### Tech Stack
- Gensim, Tomotopy, Top2Vec, spaCy, Dask, Weights & Biases, Streamlit, FastAPI, Docker, AWS EC2, AWS ECR, GitHub Actions, Python, pandas, scikit-learn

## Overview

We built a web application where the user can submit a question and gets matches to a subject-matter expert. The application sends the query to a REST API that parses the text and uses two machine learning algorithms to detect topics and keywords. It then displays the topic hierarchies, named entities, and subject-matter experts to the user.

## Background

How can we organize thousands of requests quickly and automatically with little human intervention? This is the challenge [GLG](https://glginsights.com), the world's largest expert network, faces every day. GLG receives hundreds of requests per day from clients looking for subject-matter experts that can help answer questions on topics ranging from the airline industry’s ability to cope with COVID-19 to the zebra mussel infestations in North America. The goal is to quickly identify the topics and keywords in free-form text to match clients with a specialist in the database.

## Project goals
- Detect hierarchical clusters of topics from client submitted requests
- Group requests into common topics to better understand and service demand
- Automatic meta-data tagging
- Identify underlying patterns in submitted requests over time
- Create web application to demo algorithm and match clients to topic specialist in database

## Approach
- [2.7 million news articles](https://components.one/datasets/all-the-news-2-news-articles-dataset/) as proxies for client request
  - Focused on healthcare and technology related topics
- [Top2Vec](https://github.com/ddangelov/Top2Vec) algorithm for hierarchical clustering, served with FastAPI, deployed on AWS EC2
- Named entity recognition with SpaCy and SciSpaCy's NER models
- Streamlit web app
  - where user can submit a request and receive topic distribution and named entities
  - shows distribution of topic hierarchies over time
  - dockerized and deployed on AWS EC2

<br/>

### Streamlit UI
![Screenshot of Streamlit app](docs/imgs/tabs3.png?raw=true)

### Query submission and named entity recognition results
![Screenshot: named entity recognition](docs/imgs/submit_query_tech_amz2.png?raw=true)

### Display of topic hierarchies and matching to experts
![Screenshot: topic hierarchies](docs/imgs/submit_query_tree.png?raw=true)

### Distribution of topics over time, hierarchy level 2
![Screenshot: topic hierarchies](docs/imgs/topic_distribution_lev2.png?raw=true)

### Distribution of topics over time, hierarchy level 3
![Screenshot: topic hierarchies](docs/imgs/topic_distribution_lev3.png?raw=true)