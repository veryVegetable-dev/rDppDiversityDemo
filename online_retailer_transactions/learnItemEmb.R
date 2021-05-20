library(rDppDiversity) # devtools::load_all() for package with local source code 


data_dir = "data_dir"
data_path=paste(data_dir, "transactions_data_group_by_invoice.txt.100", sep="/")

res = learnItemEmb(train_data_path=data_path, emb_size=3, regularization=1, learning_rate=0.001, neg_sample_cnt=10, epoch=1)

item_emb = res[[1]]
names = res[[2]]
log_likelihood = res[[2]]

test_num = 100
test_item_emb = item_emb[1:test_num, ] 
n = 10
top_n = bestSubset(test_item_emb, rep(1, test_num), n)
names[top_n$id+1]
