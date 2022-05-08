import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_stop

nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def clean(text):
    # standalone sequences of specials, matches &# but not #cool
    text = re.sub(r'(?:^|\s)[&#<>{}\[\]+|\\:-]{1,}(?:\s|$)', ' ', text)
    # standalone sequences of hyphens like --- or ==”
    text = re.sub(r'(?:^|\s)[\-=\+]{2,}(?:\s|$)', ' ', text)
    # Remove punctuation and numbers
    text = re.sub('[^\w\s]', '', text)
    text = re.sub('\d+', '', text)
    # sequences of white spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip().lower()


def clean_df(df):
    df = df.copy()
    df["article"] = df["article"].map(decontracted).map(clean)
    return df


def lemmatize(df, nlp=nlp):
    
    def create_lemmas(text):
        doc = nlp(text)
        lemmatized = [
            token.lemma_
            for token in doc
            if token.text not in en_stop
                and len(token.text) >  1
            ]
        # remove new stopwords created by lemmatization
        lemmatized = [
            token
            for token in lemmatized
            if token not in en_stop
                and len(token) > 1
            ]
        return lemmatized
    
    df = df.copy()
    df["article"] = df["article"].map(create_lemmas)
    
    return df
