from src.model import QueryModel

if __name__ == "__main__":
    model_path = "./h5_files/trained.h5"
    query_model = QueryModel(model_path, "legit")
    
    domain = "microsoft.com"
    prediction = query_model.predict(domain)
    print(prediction)
