import pandas as pd

def import_and_clean_data(file_path):
    """
    Importeert een CSV-bestand en voert dataverwerking uit.
    
    Parameters:
        file_path (str): Pad naar het CSV-bestand.
        
    Returns:
        pd.DataFrame: Schoongemaakte DataFrame.
    """
    try:
        # CSV inlezen
        data = pd.read_csv(file_path)
        
        # Verwijderen van lege waarden
        data = data.dropna()
        
        # Automatisch datatypes converteren
        data = data.convert_dtypes()
        
        print("Data succesvol geïmporteerd en schoongemaakt.")
        return data
    
    except Exception as e:
        print(f"Fout bij het verwerken van data: {e}")
        return None
# Testbestand (bijv. "data.csv")
data = import_and_clean_data("data.csv")
print(data.head())
