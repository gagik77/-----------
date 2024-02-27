import datetime
goods ={
     'Пельмени':[
         {'amount': 1, 'expiration_date':datetime.date(2023, 9, 30)},
         {'amount': 2, 'expiration_date': datetime.date(2023, 10, 28)}
     ]
} 

def add(items, title, amount, expiration_date=None):
    key=items.keys()
    if expiration_date != None:
        f_date_str=datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
        f_date=f_date_str.date()
        if title in items:
            goods[title].append({'amount': amount, 'expiration_date':f_date})
        else:
            items[title] = [{'amount':amount,'expiration_date':f_date}]
    else:
      if title in items:
            goods[title].append({'amount': amount, 'expiration_date':f_date})
      else:
            items[title] = [{'amount':amount,'expiration_date':f_date}]
            


add(goods, 'Яйца', 10, '2023-9-30')
print(goods)