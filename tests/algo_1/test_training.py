from src.model import train_model

if __name__ == "__main__":
    domain_file = "./dataset/dga_domains.csv"
    output_file = "./h5_files/model.h5"
    
    x_columns = "domain"
    y_column = "class"
    
    train_model(domain_file, x_columns, y_column, output_path = output_file)
