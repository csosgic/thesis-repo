le = LabelEncoder()
cleaned_data['Label']= le.fit_transform(cleaned_data['Label'])
cleaned_data['Label'].unique()