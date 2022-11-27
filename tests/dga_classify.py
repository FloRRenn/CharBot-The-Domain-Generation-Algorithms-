import argparse
from src.model import QueryModel

if __name__ == "__main__":
    model_path = "models/trained.model"
    query_model = QueryModel(model_path, "legit")

    ap = argparse.ArgumentParser()
    ap.add_argument("domain", nargs = '*', help="Domain(s) to be test. Either single domain or comma separated")
    args = vars(ap.parse_args())
    
    domain = args["domain"]
    prediction = query_model.predict(domain)
    print(prediction)
