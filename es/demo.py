import elasticsearch
from elasticsearch.helpers import bulk


class ElasticsearchClient:

    @staticmethod
    def connection():
        es_servers = [{"host": "localhost", "port": 9200}]
        es_client = elasticsearch.Elasticsearch(hosts=es_servers)
        return es_client


class DemoDoc:

    def __init__(self):
        self.index = "demo"
        self.doc_type = "demo_doc"
        self.es_client = ElasticsearchClient.connection

    def set_mapping():
        pass
