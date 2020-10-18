#!/usr/bin/env python
# coding: utf-8

# <h1>Create A Simple Search Engine Using Python</h1>

# <h3>1. Preparing the documents </h3>

# In[16]:


import pandas as pd  # data processing
import numpy as np  # linear algebra
import glob  # find files recursively


# In[17]:


def read_files(folder_name):
    corpus = [] 
    
    #Get number of files in dir
    fileCounter =  len(glob.glob(folder_name+"/*.txt"))  

    #The glob module is used to retrieve files/pathnames matching a specified pattern
    #An asterisk (*) matches zero or more characters in a segment of a name
    
    for file in glob.glob(folder_name + "/*.txt"):
        with open(file, "r") as file_txt:    
            # Append the documents to corpus
            corpus.append((file, file_txt.read()))
                    
    return corpus,fileCounter


# <h3>2. Create a Term-Document Matrix with TF-IDF weighting</h3>

# <h5>Generating tf-idf vectors using Tfidfvectorizer you compute the word counts, idf and tf-idf values all at once</h5>

# In[18]:


def tf_idf(corpus):

    # Import TfidfVectorizer
    from sklearn.feature_extraction.text import TfidfVectorizer

    # Create TfidfVectorizer object
    vectorizer = TfidfVectorizer(analyzer='word', min_df = 0, max_df = 0.85 , stop_words = 'english') 

    # Generate matrix of tf-idf vectors
    tfidf_matrix = vectorizer.fit_transform([content for file, content in corpus])

    # Create a DataFrame and set the vocabulary as the index
    tfidf_matrix = tfidf_matrix.T.toarray()
    df = pd.DataFrame(tfidf_matrix, index=vectorizer.get_feature_names())
    return df,vectorizer


# <h3>3. Get cosine Similarity</h3>
# <h6>It will defines the similarity between query and documents by measuring cosine of angle between two vectors .</h6>

# In[19]:


def get_similarity(folder_name, query):
    
    #Read the files 
    corpus,fileCounter = read_files(folder_name)  
    
    #Generate tf-idf vectors
    df,vectorizer = tf_idf(corpus)  
    
    # Convert the query to lowercase
    query.lower()
    # Convert the query become a vector
    query = [query]
    q_vec = vectorizer.transform(query).toarray().reshape(df.shape[0],)
    sim = {} 
    
    # Calculate the similarity
    for i in range(fileCounter):
        sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
        
    # Sort the values 
    sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True) 

    # Print the document and their similarity values
    for k, v in sim_sorted:
        if v != 0.0:
            print("Similaritas:", v)
            print("File path :", corpus[k][0] , '\n')


# In[20]:


# Add The Query and dir_name
dir_name = input("Enter directory name : ") 
Query = input("Enter your query : ") 
print()

#Get the similar documents
get_similarity(dir_name, Query)


# In[ ]:




