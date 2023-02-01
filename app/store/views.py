from . import store_bp
from flask import render_template, request, url_for

@store_bp.route('/')
def show_index():
    if request.method == 'GET':
        title = 'Store'
        return render_template('under-construction.html', title=title)
        # item1 = {
        #     'imgSrc': url_for('static', filename='img/cell.svg'),
        #     'title': 'Adult Basic Hat',
        #     'cost': '25',
        #     'description': 'Adult Basic Hat'
        # }
        # item2 = {
        #     'imgSrc': url_for('static', filename='img/cell.svg'),
        #     'title': 'Adult Trucker Hat',
        #     'cost': '29',
        #     'description': 'Adult Trucker Hat'
        # }
        # item3 = {
        #     'imgSrc': url_for('static', filename='img/cell.svg'),
        #     'title': 'Adult Trucker Hat',
        #     'cost': '28',
        #     'description': 'Adult Trucker Hat'
        # }
        # items = [item1, item2, item3]
        # return render_template('store/catalog.html', title=title, items=items)

@store_bp.route('/details/<product>')
def show_product_details(product):
    # return render_template('store/detail.html', product=product, inStock=True)
    return render_template('under-construction.html', title='Under Construction')

@store_bp.route('/tickets')
def show_tickets():
    title = 'Purchase Tickets'
    return render_template('store/tickets.html', title=title)
    # return render_template('under-construction.html', title=title)

@store_bp.route('/support')
def show_support():
    title = 'Support'
    # return render_template('store/support.html', title=title)
    return render_template('under-construction.html', title=title)

@store_bp.route('/terms-conditions')
def show_terms():
    title = 'Terms and Conditions'
    # return render_template('store/terms-conditions.html', title=title)
    return render_template('under-construction.html', title=title)

@store_bp.route('/privacy-policy')
def show_pp():
    title = 'Privacy Policy'
    # return render_template('store/privacy-policy.html', title=title)
    return render_template('under-construction.html', title=title)