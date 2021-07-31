import pandas as pd
import plotly.express as px
import codecs
import os

'''
DOCUMENTATION - https://plotly.com/python/bar-charts/
'''

base_df = pd.read_html("https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm?utm_campaign=dp_google")

# extracting olympic medal dataset
df = base_df[0]
df.to_csv("olympics.csv")

# renaming dataframe columns
df.columns = ['Rank', 'Country', 'Gold', 'Silver', 'Bronze', 'Total','RankbyTotal', 'NOCCode']

# renaming country values to list
countries = df['Country'].to_list()

csv_file = codecs.open(os.path.join("data","medals.csv"),"w",encoding="utf8")
head = "Country,medal,count\n"
csv_file.write(head)
for country in countries:
    # medal counts
    g = df[df['Country']==country]['Gold'].to_list()[0]
    s = df[df['Country']==country]['Silver'].to_list()[0]
    b = df[df['Country']==country]['Bronze'].to_list()[0]
    country = country.replace(",", "|")
    genstr = country + "," + "gold" + "," + str(g) + "\n" + country + "," + "Silver" + "," + str(s) + "\n" + country + "," + "Bronze" + "," + str(b) + "\n"
    csv_file.write(genstr)

csv_file.close()

medal_df = pd.read_csv(os.path.join("data","medals.csv"))

fig = px.bar(medal_df, x="Country", y="count", color="medal", color_discrete_sequence=['yellow','silver','rgb(173, 138, 86)'],title="All Country Tokyo Olympic 2020 Medal Visualization")
fig.update_layout(xaxis_tickangle=60)
fig.show()