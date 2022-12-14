



"""
BAR GRAPH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# In[]
"""
BAR GRAPH
"""
# In[]

Pop_total = pd.read_csv("Air_pollution.csv")
print(Pop_total)

drp_Pop_column = Pop_total.drop(['Country Code', 'Indicator Name', 'Indicator Code', '1989'], axis=1)
print(drp_Pop_column)

new_Pop_total = drp_Pop_column.iloc[[13,29,35,40,55,109,81],:]
print(new_Pop_total)

drp_Pop_null = new_Pop_total.dropna()
print(drp_Pop_null)

Pop_index = drp_Pop_null.set_index('Country Name')
print(Pop_index)

Pop_sel_cols = (new_Pop_total["Country Name"])

x = np.arange(len(Pop_sel_cols))

Pop_one = (new_Pop_total["1990"])
Pop_two = (new_Pop_total["1995"])
Pop_three = (new_Pop_total["2000"])
Pop_four = (new_Pop_total["2005"])
Pop_five = (new_Pop_total["2010"])
Pop_six = (new_Pop_total["2015"])

plt.figure(figsize=(10,8))


plt.bar(x-0.3,Pop_one, width=0.1, label="1990", edgecolor="black")
plt.bar(x-0.2,Pop_two, width=0.1, label="1995", edgecolor="black")
plt.bar(x-0.1,Pop_three, width=0.1, label="2000", edgecolor="black")
plt.bar(x+0.1,Pop_four, width=0.1, label="2005", edgecolor="black")
plt.bar(x+0.2,Pop_five, width=0.1, label="2010", edgecolor="black")
plt.bar(x+0.3,Pop_six, width=0.1, label="2015", edgecolor="black")

plt.xticks(x, Pop_sel_cols, rotation = 45)
plt.xlabel("Countries")
plt.ylabel('Air Pollution(micrograms per cubic meter)')
plt.legend()
plt.show()



# In[]
"""
BAR GRAPH (2)
"""
# In[]

ghg_total = pd.read_csv("ghg-emissions.csv")
print(ghg_total)

drp_ghg_column = ghg_total.drop(['unit'], axis=1)
print(drp_ghg_column)

new_ghg_total = drp_ghg_column.iloc[[14,5,8,10,2,20],:]
print(new_ghg_total)

drp_ghg_null = new_ghg_total.dropna()
print(drp_ghg_null)

ghg_index = drp_ghg_null.set_index('Country Name')
print(ghg_index)

ghg_sel_cols = (new_ghg_total["Country Name"])

x = np.arange(len(ghg_sel_cols))

ghg_one = (new_ghg_total["1995"])
ghg_two = (new_ghg_total["2000"])
ghg_three = (new_ghg_total["2005"])
ghg_four = (new_ghg_total["2010"])
ghg_five = (new_ghg_total["2015"])
ghg_six = (new_ghg_total["2019"])

plt.figure(figsize=(10,8))


plt.bar(x-0.3,ghg_one, width=0.1, label="1995", edgecolor="black")
plt.bar(x-0.2,ghg_two, width=0.1, label="2000", edgecolor="black")
plt.bar(x-0.1,ghg_three, width=0.1, label="2005", edgecolor="black")
plt.bar(x+0.1,ghg_four, width=0.1, label="2010", edgecolor="black")
plt.bar(x+0.2,ghg_five, width=0.1, label="2015", edgecolor="black")
plt.bar(x+0.3,ghg_six, width=0.1, label="2019", edgecolor="black")

plt.xticks(x, ghg_sel_cols, rotation = 45)
plt.xlabel("Countries")
plt.ylabel('GHG Emission(MtCO2e)')
plt.legend()
plt.show()




# In[]


"""
LINE GRAPH
"""

# Read Excel file and have a look

agri_land = pd.read_csv("Agricultural_Land.csv")
print("\nagri_land: \n", agri_land)

agri_land = agri_land.drop(['Indicator Name', 'Indicator Code', '1990'], axis=1)
print("\ndrop agri_land: \n", agri_land)

# transpose it

# In[ ]:


agri_land = pd.DataFrame.transpose(agri_land)
print("\n transpose agri_land: \n", agri_land)

# Create the header

# In[ ]:

header_1 = agri_land.iloc[0].values.tolist()
agri_land.columns = header_1
print("\nheader agri_land",agri_land)

# Two ways to remove the first two lines

# In[ ]:

agri_land = agri_land.iloc[2:]
print("\nremove lines agri_land: \n",agri_land)
# Remove NaN entries for canada and china. 

# In[ ]:

print(len(agri_land))

agri_land = agri_land[agri_land["China"].notna()]
agri_land = agri_land[agri_land["Chile"].notna()]
agri_land = agri_land[agri_land["Brazil"].notna()]
agri_land = agri_land[agri_land["Japan"].notna()]
agri_land = agri_land[agri_land["Jordan"].notna()]
agri_land = agri_land[agri_land["Canada"].notna()]
agri_land = agri_land[agri_land["Italy"].notna()]
agri_land = agri_land[agri_land["Mexico"].notna()]


# And the plot

# In[ ]:


agri_land.index = agri_land.index.astype(int)

plt.figure(figsize=(10,8))

plt.plot(agri_land.index, agri_land["China"], label="China", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Chile"], label="Chile", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Japan"], label="Japan", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Jordan"], label="Jordan", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Canada"], label="Canada", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Italy"], label="Italy", linestyle='dashed')
plt.plot(agri_land.index, agri_land["Mexico"], label="Mexico", linestyle='dashed')

plt.xlabel("year")
plt.ylabel("GHG Emmissions")
plt.legend()
plt.show()





"""
LINE GRAPH (2)
"""

# Read Excel file and have a look

land_area = pd.read_csv("Forest_Area.csv")
print("\nland_area: \n", land_area)

land_area = land_area.drop(['Country Code','Indicator Name', 'Indicator Code'], axis=1)
print("\ndrop land_area: \n", land_area)

# transpose it

# In[ ]:


land_area = pd.DataFrame.transpose(land_area)
print("\n transpose land_area: \n", land_area)

# Create the header

# In[ ]:

header_1 = land_area.iloc[0].values.tolist()
land_area.columns = header_1
print("\nheader land_area",land_area)

# Two ways to remove the first two lines

# In[ ]:

land_area = land_area.iloc[2:]
print("\nremove lines land_area: \n",land_area)
# Remove NaN entries for canada and china. 

# In[ ]:

print(len(land_area))

land_area = land_area[land_area["India"].notna()]
land_area = land_area[land_area["Japan"].notna()]
land_area = land_area[land_area["Sri Lanka"].notna()]
land_area = land_area[land_area["Mexico"].notna()]
land_area = land_area[land_area["Australia"].notna()]
land_area = land_area[land_area["Romania"].notna()]
land_area = land_area[land_area["Vietnam"].notna()]


# And the plot

# In[ ]:


land_area.index = land_area.index.astype(int)

plt.figure(figsize=(10,8))

plt.plot(land_area.index, land_area["India"], label="India", linestyle='dashed')
plt.plot(land_area.index, land_area["Japan"], label="Japan", linestyle='dashed')
plt.plot(land_area.index, land_area["Sri Lanka"], label="Sri Lanka", linestyle='dashed')
plt.plot(land_area.index, land_area["Mexico"], label="Mexico", linestyle='dashed')
plt.plot(land_area.index, land_area["Australia"], label="Australia", linestyle='dashed')
plt.plot(land_area.index, land_area["Romania"], label="Romania", linestyle='dashed')
plt.plot(land_area.index, land_area["Vietnam"], label="Vietnam", linestyle='dashed')

plt.xlabel("year")
plt.ylabel("Land Area")
plt.legend()
plt.show()
