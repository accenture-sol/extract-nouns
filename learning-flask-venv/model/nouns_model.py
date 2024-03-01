from textblob import TextBlob

def extract_noun_phrases(text):
    extract_noun_phrases = TextBlob(text).noun_phrases
    output_string = ""
    for noun_phrase in extract_noun_phrases:
        output_string += f"{noun_phrase} "
    output = {'noun_phrases': output_string}
    return output
        
    
    