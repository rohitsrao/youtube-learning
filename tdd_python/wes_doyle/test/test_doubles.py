class NerModelTestDouble:
    '''
    Test double for spaCy NLP model
    '''
    def __init__(self, model):
        self.model = model

    def return_doc_ents(self, ents):
        self.ents = ents
    
    def __call__(self, sentence):
        return DocTestDouble(sentence, self.ents)

class DocTestDouble:
    '''
    Test double for spaCy doc
    '''

    def __init__(self, sentence, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]

class SpanTestDouble:
    '''
    Test double for spaCy span
    '''
    
    def __init__(self, text, label):
        self.text = text
        self.label_ = label
