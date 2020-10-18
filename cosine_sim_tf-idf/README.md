<h1>Calculate TFIDF and Cosine Similarity</h1>

<h4>Find similarity between documents and specific queries using cosine similarity and term-document matrix with TF-IDF weighting.</h4>

<h5>Generating tf-idf vectors using Tfidfvectorizer you compute the word counts, idf and tf-idf values all at once</h5>
<h5>TfidfVectorizer will convert a collection of raw documents to a matrix of TF-IDF features.</h5>
<h5>Parameters that TfidfVectorizer func use </h5>

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
    
    
 
