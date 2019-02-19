from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Innovation", email="Innovation@udacity.com",
             picture='https://pbs.twimg.com\
             /profile_images/2671170543/18debd694829\
             ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#  for UrbanBurger
catalog1 = Catalog(user_id=1, name="Zerg")

session.add(catalog1)
session.commit()

Item2 = Item(user_id=1, name="zergling", description="The \
    Zergling is a small and fast melee attacker and the backbone\
     of the Zerg army. ",
                     catalog=catalog1)

session.add(Item2)
session.commit()


Item1 = Item(user_id=1, name="Drone", description="The Drone \
    is the basic worker unit for Zerg.",
                     catalog=catalog1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Queen", description="The Queen \
    is an essential unit for the Zerg base, capable of being spawned fr\
       om any Hatchery after a Spawning Pool has been built",                     catalog=catalog1)

session.add(Item2)
session.commit()

catalog1 = Catalog(user_id=1, name="Terren")

session.add(catalog1)
session.commit()

Item2 = Item(user_id=1, name="Marine", description="Marines\
 are the all-purpose infantry unit produced from a Barracks. ",
                     catalog=catalog1)

session.add(Item2)
session.commit()


Item1 = Item(user_id=1, name="Ghost", description="The Ghost\
 is a specialized infantry unit built from a Barracks with an attached \
    Tech Lab once a Ghost Academy has been constructed.",
                     catalog=catalog1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Battlecruiser", description="The\
 Battlecruiser is the Terran's capital ship. In LotV the Battlecruiser has \
    been granted the Tactical Jump ability, allowing it to telepo\
    rt anywhere on the map (regardless of fog of war).",
                     catalog=catalog1)

session.add(Item2)
session.commit()

print "added  items!"
