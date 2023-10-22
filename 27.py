#Merge two dictionaries into one.
dict1 = {'Mahesh': 85, 'Soham': 92, 'Sham': 78}
dict2 = {'Arihant': 95, 'Ram': 88}
dict3= {**dict1, **dict2}
print("Merged Dictionary: ")
print(merged_dict)
