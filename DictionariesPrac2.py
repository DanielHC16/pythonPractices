# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
            'fantasy land': { 'capital':'nowhere', 'population':6.666} }
manila = { 'tondo': {'tourist spot':'binondo', 'rating':10}, 
            'sta.mesa': {'tourist spot': 'denlens', 'rating': 10},
            'intramuros': {'tourist spot:': 'plm', 'rating': 10}}

# Print out the capital of France
print(europe['france']['population'])

# Create sub-dictionary data
data = {'capital':'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)