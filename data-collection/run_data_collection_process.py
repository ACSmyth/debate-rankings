import os

start = '2020-08-01'
end = '2021-08-01'
sleep_time = 4

# Scrape tournament ids
os.system(f'npx cypress run --spec "cypress/integration/scrape_tournament_ids.js" --env start="{start}",end="{end}"')

# Scrape entries from each tournament
os.system(f'npx cypress run --spec "cypress/integration/scrape_bid_tournaments.js" --env start="{start}",end="{end}"')

# Get round pages for each entry
os.system(f'python get_round_pages.py start="{start}" end="{end}" sleep={sleep_time}')

# Process round pages for each entry
os.system(f'python process_round_pages.py start="{start}" end="{end}"')
