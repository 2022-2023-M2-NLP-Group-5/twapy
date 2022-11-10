"""Example script
"""

import twapy

model_dir = './models'
collection = twapy.ModelCollection(model_dir)
analogy = twapy.Analogy('reagan', '2001', '2013', collection=collection)
print(analogy)
# This prints the following:?

