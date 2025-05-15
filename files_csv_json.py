import json

with open("./media/logs_unique_ips.json") as f:
    data = json.load(f)

d = {}
for row in data:
    if row["ip"] not in d:
        d[row["ip"]] = 1
    else:
        d[row["ip"]] += 1   
         
values_list = list(d.values())
res = sorted(values_list, reverse=True)
print(sum(res[:3]))

