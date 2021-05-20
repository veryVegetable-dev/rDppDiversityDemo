data_path = "data_path"
out_path = "out_path"

invoice_items = dict()
with open(data_path, "r") as data_file:
    for line in data_file.readlines()[1:]:
        fields = line.strip().split("\t")
        if len(fields) < 2:
            continue
        invoice_no = fields[0]
        stock_code = fields[1]
        invoice_items.setdefault(invoice_no, [])
        invoice_items[invoice_no].append(stock_code)

out_file = open(out_path, "w")
for k, v in invoice_items.items():
    out_file.write(",".join(v) + "\n")
    print(k, v)
out_file.flush()
out_file.close()
