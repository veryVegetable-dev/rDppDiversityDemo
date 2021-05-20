import random

data_dir = "data_dir"

# movies info  
data_path = data_dir + "movies.txt.small"

# processed data 
items_emb_path = data_dir + "items_emb"
duration_path = data_dir + "duration"
items_info_path = data_dir + "items_info"
feautures_path = data_dir + "features"

# generate durations & item info & feautre vector
duration_file = open(duration_path, "w")
items_info_file = open(items_info_path, "w")
feature_set = set()
with open(data_path, "r") as data_file:
    for line in data_file.readlines()[1:]:
        fields = line.strip().split("\t")
        if len(fields) != 3:
            continue
        for one_feature in fields[2].split("|"):
            feature_set.add(one_feature)
        rand_duration = int(random.normalvariate(120, 30))
        duration_file.write(str(rand_duration) + "\n")
        items_info_file.write(fields[2] + "\t" + str(rand_duration) + "\n")
duration_file.flush()
duration_file.close()
items_info_file.flush()
items_info_file.close()

# save features & item emb 
feature_list = list(feature_set)
items_emb_file = open(items_emb_path, "w")
with open(data_path, "r") as data_file:
    for line in data_file.readlines()[1:]:
        fields = line.strip().split("\t")
        if len(fields) != 3:
            continue
        curr_features = set(fields[2].split("|"))
        one_hot_feature = ["1" if _ in curr_features else "0" for _ in feature_list]
        items_emb_file.write("\t".join(one_hot_feature) + "\n")
items_emb_file.flush()
items_emb_file.close()

with open(feautures_path, "w") as features_file:
    for feature in feature_list:
        features_file.write(feature + "\n")
    features_file.flush()
