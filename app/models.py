from . import db


class PropertyProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    bedrooms = db.Column(db.INTEGER)
    bathrooms = db.Column(db.INTEGER)
    location = db.Column(db.String(200))
    price = db.Column(db.String(80))
    proptype = db.Column(db.String(80))
    pic_name = db.Column(db.String(255))


    def __init__(self, title, description, bedrooms, bathrooms, location, price, proptype, pic_name):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.proptype = proptype
        self.pic_name = pic_name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
