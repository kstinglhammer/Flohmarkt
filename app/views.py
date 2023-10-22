from flask import render_template, request, jsonify, redirect
from app import app, db
from app.models import Sellers

@app.route('/add_seller', methods=['GET', 'POST'])
def add_seller():
    if request.method == 'POST':
        data = request.get_json()
        new_seller = Sellers(
            FirstName=data['first_name'],
            LastName=data['last_name'],
            Email=data['email'],
            Phone=data['phone']
        )
        db.session.add(new_seller)
        db.session.commit()
        return jsonify({'message': 'Seller added successfully!'}), 201
    return render_template('add_seller.html')

@app.route('/')
def home():
    return redirect('/add_seller')
# ... (other endpoints and code)
