import json

# with open("./media/logs_unique_ips.json") as f:
#     data = json.load(f)

# d = {}
# for row in data:
#     if row["ip"] not in d:
#         d[row["ip"]] = 1
#     else:
#         d[row["ip"]] += 1   
         
# values_list = list(d.values())
# res = sorted(values_list, reverse=True)
# print(sum(res[:3]))
import csv

# with open("./media/crups.csv") as f:
#     data = csv.reader(f, delimiter=";")
#     next(data)
#     semolina_price = None
#     all_price = 0
#     counter = 0
#     for row in data:
#         price = float(row[1].replace('"', ''))
#         if semolina_price is None or price < semolina_price:  
#             semolina_price = price
#         all_price += price
#         counter += 1

# print(semolina_price, round(all_price / counter, 2))
# with open("./media/crups.csv") as f:
#     data = csv.reader(f, delimiter=";")
#     next(data)
#     lst = []
#     for row in data:
#         lst.append(float(row[1].replace('"', '')))
#     print(sum(lst) / len(lst))

with open('./media/logs_unique_ips.json', encoding='utf-8') as f:
    data = json.load(f)

with open('./media/logs_unique_ips.csv', 'w', encoding='utf-8') as csv_f:
    # headers = data[0].keys()
    headers = ['timestamp', 'ip', 'user-agent']
    writer = csv.DictWriter(csv_f, fieldnames=headers, delimiter=',')
    writer.writeheader()
    writer.writerows(data)