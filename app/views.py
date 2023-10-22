from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Seller

@app.route('/seller/<int:seller_id>/', methods=['GET', 'POST'])
def seller(seller_id=None):
    seller = Seller.query.get_or_404(seller_id) if seller_id else None
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        address = request.form['address']
        if seller:
            seller.name = name
            seller.contact = contact
            seller.address = address
        else:
            seller = Seller(name=name, contact=contact, address=address)
            db.session.add(seller)
        db.session.commit()
        return redirect(url_for('seller', seller_id=seller.id))
    return render_template('seller.html', seller=seller)

@app.route('/')
def home():
    return redirect('/add_seller')
# ... (other endpoints and code)
