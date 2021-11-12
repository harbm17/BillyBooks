import pandas as pd

#in here you need to provide the number spilts
number_of_splits=7
for i in range(0,number_of_splits+1):
    word =i+1
    print(word)

    json_file =f"goodreads_book_works{word}.json"
    csv_file =f"goodreads_book_works{word}.csv"
    df = pd.read_json (fr'C:\Users\bsder\Desktop\New folder\{json_file}')
    df.to_csv (fr'C:\Users\bsder\Desktop\New folder\{csv_file}', index = None)