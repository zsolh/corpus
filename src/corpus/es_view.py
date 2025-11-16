import logging

from datasets import load_dataset
from elasticsearch import Elasticsearch
from fastapi import FastAPI, HTTPException

logging.basicConfig(filename="es.log", level=logging.INFO)

app = FastAPI()

es_client = Elasticsearch('http://localhost:9200/')
@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/ping")
def ping():
    ping = es_client.ping()
    return {ping}

@app.get("/health")
def health():
    health = es_client.cluster.health()

    return {
        "status": "success",
        "message": "Connected to Elasticsearch",
        "cluster_status": health["status"],
        "number_of_nodes": health["number_of_nodes"],
        "active_shards": health["active_shards"],
    }

@app.get("/create_index/{index_name}")
def create_index(index_name):
    logging.info(f"Creating index {index_name}")
    dataset = load_dataset("SZTAKI-HLT/HunSum-2-abstractive", split='train')
    dataset.add_elasticsearch_index(column="title", index_name=index_name, es_client=es_client)
    return {"status": "success", "message": "Index created"}


