from app import db

class Sellers(db.Model):
    __tablename__ = 'Sellers'
    SellerID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(100))
    Phone = db.Column(db.String(15))

class Products(db.Model):
    __tablename__ = 'Products'
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SellerID = db.Column(db.Integer, db.ForeignKey('Sellers.SellerID'))
    ProductName = db.Column(db.String(100))
    Description = db.Column(db.String(255))
    Price = db.Column(db.Float)
    Quantity = db.Column(db.Integer)
    QRCode = db.Column(db.String(255))

class Transactions(db.Model):
    __tablename__ = 'Transactions'
    TransactionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Products.ProductID'))
    SellerID = db.Column(db.Integer, db.ForeignKey('Sellers.SellerID'))
    Date = db.Column(db.DateTime)
    QuantitySold = db.Column(db.Integer)

class Invoices(db.Model):
    __tablename__ = 'Invoices'
    InvoiceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SellerID = db.Column(db.Integer, db.ForeignKey('Sellers.SellerID'))
    Date = db.Column(db.DateTime)
    TotalAmount = db.Column(db.Float)
    Fees = db.Column(db.Float)
    NetAmount = db.Column(db.Float)

class Payments(db.Model):
    __tablename__ = 'Payments'
    PaymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    InvoiceID = db.Column(db.Integer, db.ForeignKey('Invoices.InvoiceID'))
    PaymentDate = db.Column(db.DateTime)
    PaymentAmount = db.Column(db.Float)
    PaymentMethod = db.Column(db.String(50))

class Users(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(50))
    PasswordHash = db.Column(db.String(255))
    Role = db.Column(db.String(50))

class Audit(db.Model):
    __tablename__ = 'Audit'
    AuditID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    Action = db.Column(db.String(255))
    Date = db.Column(db.DateTime)
