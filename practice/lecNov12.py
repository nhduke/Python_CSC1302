import pandas as pd

df1 = pd.DataFrame([
    [1,'A','a@gmail.com'],
    [2, 'B', 'b@gmail.com'],
    [3, 'C', 'c@gmail.com']
], columns = ['member_id', 'name', 'email'])
df2 = pd.DataFrame([
    [1000,'Laptop',800,2],
    [1001, 'Phone', 700,1],
    [1002, 'Backpack',50,4],
    [1003, 'Chair',50,3],
    [1004, 'Guitar',200,5]
], columns = ['order_id', 'product', 'price', 'member'])


result = pd.merge(df1, df2, how = "right", left_on = 'member_id', right_on = 'member')


print(result)