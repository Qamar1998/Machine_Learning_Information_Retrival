import pandas as pd  # data processing
import numpy as np  # linear algebra
import glob  # find files recursively
import argparse

def get_argument():

   # Instantiate the ArgumentParser object as parser
   parser = argparse.ArgumentParser(description='Process pickle file.')
   parser.add_argument( '-l', '--list', type=str,
                        help='Get query and dir_name file')
   args = parser.parse_args()
   arguments = [item for item in args.list.split(',')]
   return arguments[0] , arguments[1]


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
    top_k = 1
    for k, v in sim_sorted:
        if v != 0.0 and top_k<6:
            top_k +=1
            print("Similaritas:", v)
            print("File path :", corpus[k][0] , '\n')





# 4. run in main
if __name__ == "__main__":
   #Get dir_name and query from arguments 
   dir_name,Query= get_argument()
   print()
   print("Query : " , Query, '\n')
   get_similarity(dir_name, Query)



