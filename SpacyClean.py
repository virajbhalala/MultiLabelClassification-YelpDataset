import sys
import spacy 
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def textPreprocessing(doc):



    nlp = spacy.load('en')
    doc = nlp(doc) # phrase to tokenize
    return(doc)
    clean = []
    for token in doc:
        return(token)
        #Remove stopwords, punctuations (keep only alphanumeric), remove any unneccessary space. 
        #Tokenization will also remove any new lines character
        if  not (token.is_stop() | token.is_punct() | token.is_space() ):
            #process each token to lemmatisationa and convert to lowercase
            clean.append(token.lemma_.lower())    
    #Remove Pronouns
    clean = [i for i in clean if i not in ["-pron-"]]
    clean = ' '.join(clean)
    return clean