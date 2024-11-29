import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk

# Functie om data te importeren uit een CSV bestand
def import_data(file_path):
    """
    Importeer de dataset uit een CSV-bestand.
    
    Parameters:
    file_path (str): Het pad naar het CSV-bestand.
    
    Returns:
    pd.DataFrame: De ingelezen dataset.
    """
    df = pd.read_csv(file_path)
    return df

# Functie om data schoon te maken (bijv. lege waarden verwijderen)
def clean_data(df):
    """
    Schoonmaak van de dataset, zoals het verwijderen van lege waarden.
    
    Parameters:
    df (pd.DataFrame): De te verwerken dataset.
    
    Returns:
    pd.DataFrame: De schoongemaakte dataset.
    """
    df = df.dropna()  # Verwijder rijen met lege waarden
    # Voeg hier andere schoonmaakstappen toe, bijvoorbeeld omzetten van datatypes:
    # df['date'] = pd.to_datetime(df['date'])  # Als er een datumkolom is
    return df

# Functie om statistieken te berekenen
def calculate_statistics(df, column_name):
    """
    Bereken statistieken zoals gemiddelde, mediaan en standaarddeviatie.
    
    Parameters:
    df (pd.DataFrame): De dataset.
    column_name (str): De naam van de kolom om de statistieken van te berekenen.
    
    Returns:
    dict: Statistische gegevens zoals gemiddelde, mediaan en standaarddeviatie.
    """
    mean = df[column_name].mean()
    median = df[column_name].median()
    std_dev = df[column_name].std()
    print(f"Gemiddelde: {mean}, Mediaan: {median}, Standaarddeviatie: {std_dev}")
    return {"mean": mean, "median": median, "std_dev": std_dev}

# Functie om een histogram te genereren
def create_histogram(df, column_name):
    """
    Genereer een histogram voor de opgegeven kolom.
    
    Parameters:
    df (pd.DataFrame): De dataset.
    column_name (str): De naam van de kolom om het histogram van te maken.
    """
    sns.histplot(df[column_name])
    plt.title(f"Histogram van {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequentie")
    plt.savefig(f"visualizations/{column_name}_histogram.png")
    plt.show()

# Functie om een staafdiagram te genereren
def create_bar_chart(df, column_name):
    """
    Genereer een staafdiagram voor de opgegeven kolom.
    
    Parameters:
    df (pd.DataFrame): De dataset.
    column_name (str): De naam van de kolom om het staafdiagram van te maken.
    """
    df[column_name].value_counts().plot(kind='bar')
    plt.title(f"Staafdiagram van {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequentie")
    plt.savefig(f"visualizations/{column_name}_bar_chart.png")
    plt.show()

# Functie voor de GUI waarmee gebruikers filters kunnen toepassen
def create_gui(df):
    """
    Maak een Tkinter GUI waarmee gebruikers gegevens kunnen filteren.
    
    Parameters:
    df (pd.DataFrame): De dataset waarop gefilterd kan worden.
    """
    window = tk.Tk()
    window.title("Data Filtering")

    label = tk.Label(window, text="Filter op waarde:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    def apply_filter():
        # Filter de data op basis van de invoerwaarde
        value = entry.get()
        filtered_data = df[df['column_name'] == value]  # Pas filter aan naar behoefte
        print(f"Gefilterde data:\n{filtered_data}")

    button = tk.Button(window, text="Toepassen", command=apply_filter)
    button.pack()

    window.mainloop()
