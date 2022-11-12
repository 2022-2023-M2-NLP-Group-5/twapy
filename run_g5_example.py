"""Example script. NOTE: The DUKweb csvs appear to be malformed. Before running this, use the script g5/dukweb.py.

This will normalize/sanitize the number of columns in a CSV file. Use it on the
YEAR.csv files extracted from the DUKweb dataset files (YEAR.csv.zip).

Example usage invocations:
$ python3 run_g5_example.py
$ python3 run_g5_example.py 'dog'
$ python3 run_g5_example.py ['dog','cat','bush','cheney','reagan','computer','internet','food'] # query multiple terms in one go

"""
import fire
import twapy

def run_example(word1_list:list[str]=['cheney'],
                model1='2000',
                model2='2001',
                model_dir = './models'):
    collection = twapy.ModelCollection(model_dir)
    alignment = twapy.Alignment(model1, model2, collection=collection)

    if type(word1_list) == str:
        word1_list = [word1_list]

    for word1 in word1_list:
        analogy = twapy.Analogy(str(word1), str(model1), str(model2), alignment=alignment)
        print(analogy)

if __name__ == '__main__':
    fire.Fire(run_example)
