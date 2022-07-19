from app import db
from models import Pet

db.drop_all()
db.create_all()

p1 = Pet(name="Woofly", species="Dog", photo_url="https://www.akc.org/wp-content/uploads/2021/01/Beagle-puppy-standing-in-the-grass-1.jpeg", age=1, notes="Cute dog", available=True)
p2 = Pet(name="Spikey", species="Porcupine", photo_url="https://i.natgeofe.com/n/d0c2bc16-95be-4d1f-a1e4-322a0669a7f2/porcupines_thumb.JPG", age=3, notes="Very pointy, be careful", available=True)
p3 = Pet(name="Ashe", species="Cat", photo_url="https://cdn.britannica.com/25/7125-050-67ACEC3C/Abyssinian-sorrel.jpg", age=6, notes="Older cat, great with kids and families", available=True)

db.session.add_all([p1, p2, p3])
db.session.commit()