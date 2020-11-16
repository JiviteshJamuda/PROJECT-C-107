# Importing some modules ---

# module for drawing graphs 
import plotly.express as px
# module used for reading data and finding mean from the csv file
import pandas as pd
# This is not intended but I used it for creating a custom dataframe for this specific project
from pandas import DataFrame

# Reading the data of the csv file and storing it in a variable
data = pd.read_csv("data.csv")

# Sorting out all of the students individualy by their id's 
student_1 = data.loc[data["student_id"]=="TRL_xsl"]
student_2 = data.loc[data["student_id"]=="TRL_abc"]
student_3 = data.loc[data["student_id"]=="TRL_xyz"]
student_4 = data.loc[data["student_id"]=="TRL_zet"]
student_5 = data.loc[data["student_id"]=="TRL_123"]
student_6 = data.loc[data["student_id"]=="TRL_imb"]
student_7 = data.loc[data["student_id"]=="TRL_rst"]
student_8 = data.loc[data["student_id"]=="TRL_mno"]
student_9 = data.loc[data["student_id"]=="TRL_987"]
student_10 = data.loc[data["student_id"]=="TRL_mda"]
student_11 = data.loc[data["student_id"]=="TRL_zny"]

# Finding the mean for attempts of the student's in his/her individual levels
mean_1 = student_1.groupby("level")["attempt"].mean()
mean_2 = student_2.groupby("level")["attempt"].mean()
mean_3 = student_3.groupby("level")["attempt"].mean()
mean_4 = student_4.groupby("level")["attempt"].mean()
mean_5 = student_5.groupby("level")["attempt"].mean()
mean_6 = student_6.groupby("level")["attempt"].mean()
mean_7 = student_7.groupby("level")["attempt"].mean()
mean_8 = student_8.groupby("level")["attempt"].mean()
mean_9 = student_9.groupby("level")["attempt"].mean()
mean_10 = student_10.groupby("level")["attempt"].mean()
mean_11 = student_11.groupby("level")["attempt"].mean()

# Collecting all the data from what we just wrote the code for (line:27-37)
# This data_2 variable contains the student_id, level number and the mean of all the attempts
data_2 = [
    ["TRL_xsl", "Level 1", mean_1[0]],
    ["TRL_xsl", "Level 2", mean_1[1]],
    ["TRL_xsl", "Level 3", mean_1[2]],
    ["TRL_xsl", "Level 4", mean_1[3]],
    ["TRL_abc", "Level 1", mean_2[0]],
    ["TRL_abc", "Level 2", mean_2[1]],
    ["TRL_abc", "Level 3", mean_2[2]],
    ["TRL_abc", "Level 4", mean_2[3]],
    ["TRL_xyz", "Level 1", mean_3[0]],
    ["TRL_xyz", "Level 2", mean_3[1]],
    ["TRL_xyz", "Level 3", mean_3[2]],
    ["TRL_xyz", "Level 4", mean_3[3]],
    ["TRL_zet", "Level 1", mean_4[0]],
    ["TRL_zet", "Level 2", mean_4[1]],
    ["TRL_zet", "Level 3", mean_4[2]],
    ["TRL_zet", "Level 4", mean_4[3]],
    ["TRL_123", "Level 1", mean_5[0]],
    ["TRL_123", "Level 4", mean_5[1]],
    ["TRL_imb", "Level 1", mean_6[0]],
    ["TRL_imb", "Level 2", mean_6[1]],
    ["TRL_imb", "Level 3", mean_6[2]],
    ["TRL_imb", "Level 4", mean_6[3]],
    ["TRL_rst", "Level 1", mean_7[0]],
    ["TRL_rst", "Level 2", mean_7[1]],
    ["TRL_rst", "Level 3", mean_7[2]],
    ["TRL_rst", "Level 4", mean_7[3]],
    ["TRL_mno", "Level 1", mean_8[0]],
    ["TRL_mno", "Level 2", mean_8[1]],
    ["TRL_mno", "Level 3", mean_8[2]],
    ["TRL_mno", "Level 4", mean_8[3]],
    ["TRL_987", "Level 1", mean_9[0]],
    ["TRL_987", "Level 2", mean_9[1]],
    ["TRL_987", "Level 3", mean_9[2]],
    ["TRL_987", "Level 4", mean_9[3]],
    ["TRL_mda", "Level 1", mean_10[0]],
    ["TRL_mda", "Level 2", mean_10[1]],
    ["TRL_mda", "Level 3", mean_10[2]],
    ["TRL_mda", "Level 4", mean_10[3]],
    ["TRL_zny", "Level 1", mean_11[0]],
    ["TRL_zny", "Level 2", mean_11[1]],
    ["TRL_zny", "Level 3", mean_11[2]],
    ["TRL_zny", "Level 4", mean_11[3]],
]

# Converting the data_2 variable into a dataframe stored in variavble df
# This variable inludes the columns : Student ID, Level and Attempt (taken from the variable data_2)
df = DataFrame(data_2, columns=["Student ID", "Level", "Attempt"])
# print(df)

# Creating the graph using the plotly.express module
# Drawing a scatter graph with values from the Dataframe of variable df (line:88)
graph = px.scatter(df, x="Student ID", y="Level", color="Attempt", size="Attempt")
# Displaying the graph
graph.show()