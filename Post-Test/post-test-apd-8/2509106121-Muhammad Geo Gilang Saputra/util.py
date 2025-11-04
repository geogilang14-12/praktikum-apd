import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(teks):
    print("=" * 50)
    print(teks.center(50))
    print("=" * 50)
