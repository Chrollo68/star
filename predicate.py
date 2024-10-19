import spacy

nlp = spacy.load('en_core_web_sm')

def extract_predicates(sentence): 
    doc = nlp(sentence)
    predicates = [] 
    for token in doc:
        if token.dep_ in ['attr', 'acomp']:
            predicates.append(token.text)
      
        if token.pos_ == 'VERB' and token.dep_ != 'aux':
            predicates.append(token.lemma_)
    return sorted(set(predicates))

sentences = [
    "Kalpaj is a Rider.",
   ]

# Extract and print predicates for each sentence
for sentence in sentences:
    predicates = extract_predicates(sentence)
    print(f"Predicates in the sentence '{sentence}': {predicates}")
