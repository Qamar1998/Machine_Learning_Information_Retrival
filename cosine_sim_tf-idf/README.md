<h1>Documents-Search-Engine</h1>
<h6>Documents-Search-Engine is an Information Retrieval System that use Term frecuency-inverse Document Frecuency and cosine similarity to retreive the most relevants documents given a query</h6>

<h3>Calculate TFIDF and Cosine Similarity</h3>

<h6>We will find the similarity between documents and specific queries using cosine similarity and term-document matrix with TF-IDF weighting.</h6>
<h4>Overview</h4>
<h5>1. Reading the documents</h5>
<h5>2. Generating tf-idf vectors using Tfidfvectorizer from (SklearnCosineSimilarity library) you compute the word counts, idf and tf-idf values all at once</h5>
<h6>TfidfVectorizer will convert a collection of raw documents to a matrix of TF-IDF features.</h6>
<h5>Parameters that TfidfVectorizer func use :</h5>

<ul>
    <li><h6> lowercase, default=True :
    Convert all characters to lowercase before tokenizing.</h6>
   </li>
    <li><h6> tokenizer, default=None :
    Override the string tokenization step while preserving the preprocessing and n-grams generation steps.
    Only applies if analyzer == 'word'.</h6>
   </li>
    <li> <h6>stop_words{‘english’}, list, default=None :
    all stop words will be removed from the resulting tokens. Only applies if analyzer == 'word'</h6>
   </li>
    <li> <h6>max_df, float or int, default=1.0 :
    When building the vocabulary ignore terms that have a document frequency strictly higher than the given           threshold</h6>
    </li>
    <li> <h6>min_dffloat or int, default=1 :
    It will gnore words that have very few occurrences to be considered meaningful</h6>
   </li>
    <li> <h6>max_features, limiting Vocabulary Size :
     When your feature space gets too large, you can limit its size by putting a restriction on the vocabulary          size. Say you want a max of 10,000 n-grams. it will keep the top 10,000 most frequent n-grams and      drop the rest.</h6>
   </li>  
</ul>

    
<h5>3. Calculate cosine similarity for the documents</h5>
<h6>Cosine similarity is a measure of similarity between two vectors and in information retrieval gives a useful measure of how similar two documents are likely to be in terms of their subject matter.</h6>

<h4>Source Code</h4>
<li><h5>main source file can be found /cosine_tfidf.py </h5></li>

<h4>Input information</h4>
<h5> input files were assigned and can be found ./Docs and your query by using this command</h5>
<h5> python3 cosine_tfidf.py -l ./Docs,newsletter </h5>
<h6> Which is the dir_path is ./Docs and your query is newsletter </h6>


  
    
    
 
