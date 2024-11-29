def calculate_statistics(df, columns):
    """
    Berekent eenvoudige statistieken voor gegeven kolommen.
    
    Parameters:
        df (pd.DataFrame): Dataset.
        columns (list): Lijst van kolomnamen.
        
    Returns:
        dict: Statistieken per kolom.
    """
    stats = {}
    for col in columns:
        if col in df:
            stats[col] = {
                "Gemiddelde": df[col].mean(),
                "Mediaan": df[col].median(),
                "Standaarddeviatie": df[col].std()
            }
        else:
            stats[col] = "Kolom niet gevonden"
    return stats
columns_to_analyze = ["temperatuur", "neerslag"]  # Specifieke kolommen
stats = calculate_statistics(data, columns_to_analyze)
for col, stat in stats.items():
    print(f"Statistieken voor {col}: {stat}")
