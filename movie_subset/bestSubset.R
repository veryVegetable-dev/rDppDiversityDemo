library(rDppDiversity) # devtools::load_all() for package with local source code 


data_dir = "data_dir"

items_emb_path = paste(data_dir, "items_emb", sep="/")
duration_path = paste(data_dir, "duration", sep="/")
items_info_path = paste(data_dir, "items_info", sep="/")
features_path = paste(data_dir, "features", sep="/")

# load data 
items_emb = read.delim(items_emb_path, header=FALSE)
items_info = read.delim(items_info_path, header=FALSE)
features = read.delim(features_path, header=FALSE)
duration = data.matrix(read.delim(duration_path, header=FALSE), rownames.force = NA)

# efficiency
efficiency = 1200.0 / duration

# origin data 
items_info$V4 = efficiency
names(items_info) = c("name", "genres", "duration", "efficiency")
names(items_emb) = as.character(features$V1)

# find best subset 
n = 10
top_n = bestSubset(data.matrix(items_emb, rownames.force = NA), efficiency, n)

# best subset analysis
best_subset = items_info[top_n$id+1,]
best_subset$V5 = top_n$gain
names(best_subset)[5] = "gain"

mean(best_subset$duration)
cnt = t(data.matrix(colSums(items_emb[top_n$id+1,])))
