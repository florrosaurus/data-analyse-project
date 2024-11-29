import pytest
import pandas as pd
from data_processing import import_data, clean_data, calculate_statistics

def test_import_data():
    df = import_data("data/data.csv")
    assert not df.empty, "Data is leeg na importeren"

def test_clean_data():
    df = import_data("data/data.csv")
    cleaned_df = clean_data(df)
    assert cleaned_df.isnull().sum().sum() == 0, "Er zijn nog lege waarden na het schoonmaken"

def test_calculate_statistics():
    df = import_data("data/data.csv")
    stats = calculate_statistics(df, "temperature")
    assert "mean" in stats, "De statistieken bevatten geen gemiddelde"
    assert "median" in stats, "De statistieken bevatten geen mediaan"
    assert "std_dev" in stats, "De statistieken bevatten geen standaarddeviatie"
