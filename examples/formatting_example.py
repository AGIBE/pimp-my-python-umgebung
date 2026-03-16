import sys, os
import json, re, time

# Korrigiere Formatierung: ruff format examples\formatting_example.py
# Korrigiere Code: ruff check --fix examples\formatting_example.py
# Automatischer fix bei speichern ist nicht praktisch, da es zu ungewollten Änderungen führen kann.
# Es ist besser, die Änderungen manuell zu überprüfen und zu bestätigen.


# Uneinheitliche Anführungszeichen und Leerzeichen
def greet_user( name,age):
    greeting='Hello, '+name+"!"
    return greeting

# Lange Zeilen und fehlende Kommas am Ende von Funktionsargumenten
def process_data(data, timeout=60, retry_count=3, ignore_errors=False, log_level="INFO", dry_run=False, output_format="json"):
    pass

def dict_to_json():
    # Schlechte Datenstrukturformatierung (seltsame Abstände, fehlende abschließende Kommas)
    my_dict = {
    'name':"Alice", 'age' : 30 ,
    "location":"Wonderland","skills": ['Python' , 'Data Science','Machine Learning']}
    return json.dumps(my_dict)

# Nicht verwendete Importe und Variablen 
def calculate_total(prices):
    import math # Lokaler Import, der nicht benötigt wird (ruff check --fix)
    unused_variable = 42
    total=0
    for p in prices:
            total += p # Uneinheitliche Einrückungen
    return total

# Zu viele Leerzeilen


class UserProfile:
    def __init__( self,username ):
        self.username=username

    def display(self ):
        print(  f"User: {self.username}"  )