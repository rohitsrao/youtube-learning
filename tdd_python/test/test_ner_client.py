import unittest
from ner_client import NamedEntityClient

class TestNerClient(unittest.TestCase):

    #For now we are imagining a structure that looks like this
    #A python dictionary with two keys ents and html
    #{
    #    ents: [{...}],
    #    html: "<span>..."
    #}

    def test_get_ents_returns_dictionary_given_empty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
