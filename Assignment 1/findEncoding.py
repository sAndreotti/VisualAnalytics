import chardet
import pandas as pd

with open("./datasets/us_accidents.csv", "rb") as f:
    result = chardet.detect(f.read(10000))  # Read a portion of the file
    print(result["encoding"])  # Print detected encoding

df = pd.read_csv("./datasets/us_accidents.csv", encoding=result["encoding"])
