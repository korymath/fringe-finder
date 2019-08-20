import pandas as pd

# Read the csv file in
df = pd.read_csv('data/fringe_shows_updated.csv')

for i, row in df.iterrows():
    df.at[i, 'image_url'] = '<img class="show_thumb" style="width: 100px;" src="{}"/>'.format(row['image_url'])
    df.at[i, 'perf_link'] = '<a class="buy_tickets_link" href="{}">Buy tickets</a>'.format(row['perf_link'])

df = df.drop(columns=['website'])
df = df.drop(columns=['event'])

df = df.rename(
    columns={
        'image_url':'Poster',
        'title':'Title',
        'perf_date':'Date',
        'perf_time':'Time',
        'day_of_week':'Day',
        'venue':'Venue',
        'perf_link':'Tickets',
        'duration':'Duration',
        'category':'Category',
        'rating':'Rating'})

# Save to file
df.to_html(
    'data/fringe_shows_updated.html',
    escape=False,
    table_id='table-container-table',
    classes='responsive',
    index=False)