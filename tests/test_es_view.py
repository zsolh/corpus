from src.corpus.es_view import root, ping, health, create_index

def test_root():
    assert root() == {"Hello": "World"}

def test_ping():
    assert ping() == "[true]"

def test_health():
    assert health() == {"status":"success","message":"Connected to Elasticsearch","cluster_status":"yellow","number_of_nodes":1,"active_shards":27}

def test_create_index(index_name):
    assert create_index(index_name) == {"status":"success","message":"Index created"}