import pandas as pd
import csv
import plotly.express as px


rag = pd.read_csv("data.csv")
mean = rag.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
hi = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
hi.show()
