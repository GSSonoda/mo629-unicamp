import os
from populate.populate import populate
from populate.query import plot_temp_data

if os.getenv("POPULATE", "false").lower() == "true":
    populate()

plot_temp_data()