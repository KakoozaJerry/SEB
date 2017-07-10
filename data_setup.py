from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Daily import Base, Daily, Shop

engine = create_engine('sqlite:///shop.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

## 'adding various shops'
# myShop = Shop(name = "shop 3")
# session.add(myShop)
# session.commit()

##'adding sales'
# myFirstSale = Shop(name = "shop 1")
# Sale = Daily(name = "Mark", item ="LJP", price ="500", shop = myFirstSale )
# session.add(Sale)
# session.commit()

##'Printing a shop from the daily table
# spinach = session.query(Daily).filter_by(item = 'LJP').one()
# print(spinach.shop.name)



