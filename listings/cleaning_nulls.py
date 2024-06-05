# find null or missing values
network_data.isna().sum().to_numpy()

# drop null or missing columns
cleaned_data = network_data.dropna(inplace=true)