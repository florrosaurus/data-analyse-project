import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df, column, plot_type="histogram"):
    """
    Creëert visualisaties zoals histogrammen of lijndiagrammen.
    
    Parameters:
        df (pd.DataFrame): Dataset.
        column (str): Te visualiseren kolom.
        plot_type (str): Type visualisatie: "histogram", "lijn", of "staaf".
    """
    if column not in df:
        print(f"Kolom {column} niet gevonden in dataset.")
        return
    
    plt.figure(figsize=(10, 6))
    
    if plot_type == "histogram":
        sns.histplot(df[column], kde=True)
        plt.title(f"Histogram van {column}")
    elif plot_type == "lijn":
        plt.plot(df[column])
        plt.title(f"Lijndiagram van {column}")
    elif plot_type == "staaf":
        sns.barplot(x=df.index, y=df[column])
        plt.title(f"Staafdiagram van {column}")
    
    plt.xlabel(column)
    plt.ylabel("Frequentie")
    plt.show()
create_visualizations(data, "temperatuur", "histogram")
import tkinter as tk
from tkinter import filedialog

def start_gui():
    """
    Een GUI voor het filteren van data en het kiezen van visualisaties.
    """
    def apply_filter():
        filter_value = filter_entry.get()
        column_name = column_entry.get()
        
        if column_name in data:
            filtered_data = data[data[column_name] == filter_value]
            create_visualizations(filtered_data, column_name)
        else:
            print("Ongeldige kolomnaam.")
    
    root = tk.Tk()
    root.title("Data Visualisatie")
    
    tk.Label(root, text="Kolomnaam:").pack()
    column_entry = tk.Entry(root)
    column_entry.pack()
    
    tk.Label(root, text="Filterwaarde:").pack()
    filter_entry = tk.Entry(root)
    filter_entry.pack()
    
    tk.Button(root, text="Toepassen", command=apply_filter).pack()
    root.mainloop()

# GUI starten
start_gui()
