from src.corpus import es_view

app = es_view.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)