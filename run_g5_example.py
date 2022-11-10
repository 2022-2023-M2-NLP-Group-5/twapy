"""Example script. NOTE: The DUKweb csvs appear to be malformed. Before running this, use the script g5/dukweb.py.

This will normalize/sanitize the number of columns in a CSV file. Use it on the
YEAR.csv files extracted from the DUKweb dataset files (YEAR.csv.zip).

"""

import twapy

model_dir = './models'
collection = twapy.ModelCollection(model_dir)
analogy = twapy.Analogy('cheney', '2001', '2013', collection=collection)
print(analogy)
# This prints the following:?

