# initializing lists
test_list1 = [{"gfg": 1, "best": 4}, {"geeks": 10, "good": 15}, {"love": "gfg"}]
test_list2 = [{"gfg": 6}, {"better": 3, "for": 10, "geeks": 1}, {"gfg": 10}]

# create a set of all unique keys in both dictionaries
all_keys = set().union(*(d.keys() for d in test_list1 + test_list2))

# create new dictionaries with merged values for each dictionary in both lists
new_list1 = [{key: test_list1[idx][key] if key in test_list1[idx] else None for key in all_keys} for idx in range(len(test_list1))]
new_list2 = [{key: test_list2[idx][key] if key in test_list2[idx] else None for key in all_keys} for idx in range(len(test_list2))]

# combine the new dictionaries into a single list
merged_list = []
for dict1, dict2 in zip(new_list1, new_list2):
	merged_dict = {}
	for key in all_keys:
		if dict1[key] is not None:
			merged_dict[key] = dict1[key]
		elif dict2[key] is not None:
			merged_dict[key] = dict2[key]
	merged_list.append(merged_dict)

# printing result
print("The Merged Dictionary list : " + str(merged_list))
