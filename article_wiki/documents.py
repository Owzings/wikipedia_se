from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Titre

@registry.register_document
class TitreDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'titres'
        # See Elasticsearch Indices API reference for available settings
        settings = {'titre': 1,
                    }

    class Django:
        model = Titre # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'titre',
        ]