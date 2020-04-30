import pandas as pd
import json


#state- cities dict
with open('state_cities.json', 'r') as fp:
    state_cities_dict = json.load(fp)

final_df = pd.read_csv('demo_data.csv')


pages = ['/contact','/','/pricing','/aboutus','/products']

dates = final_df.date.unique()
date_cnt = [list(final_df.date).count(dates[i]) for i in range(len(dates))]

states = final_df.state.unique()
states_cnt = [list(final_df.state).count(states[i]) for i in range(len(states))]


pg_cnt = []
contact_cnt = 0
home_cnt = 0
price_cnt  =0
about_cnt = 0
product_cnt = 0

for i in final_df.pages:
    contact_cnt += (i.count(pages[0]))
    home_cnt+= (i.count(pages[1]))
    price_cnt += (i.count(pages[2]))
    about_cnt+= (i.count(pages[3]))
    product_cnt+= (i.count(pages[4]))

pg_cnt = [contact_cnt,home_cnt,price_cnt,about_cnt,product_cnt]




#dropdown state menu
state_dropdown_options = []
for i in states:
    tmp = {}
    label = i
    #value = i.lower().replace(' ','_')
    value  = i
    tmp['label'] = label
    tmp['value'] =value
    state_dropdown_options.append(tmp)


def get_cities_count(state):
        cities = state_cities_dict[state]
        cities_cnt = []
        for i in cities:
            cities_cnt.append(list(final_df.city).count(i))
        return {'cities': cities, 'cities_cnt' : cities_cnt }
    

