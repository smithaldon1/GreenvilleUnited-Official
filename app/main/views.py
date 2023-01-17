from . import main_bp
from flask import render_template, request, url_for, abort
from app import db
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *
import config
from ..models import Main, Donation
from datetime import datetime as dt

@main_bp.route('/')
def show_index():
    # Spotlight Initialization
    card1 = {
        'img_src': url_for('static', filename='img/season-standings-2022.png'),
        'img_title': '2022 Season Standings',
        'title': 'GUFC tops Coastal Standings!', 
        'text': 'Greenville United finishes the 2022 season at the top of the Coastal Standings. The team finished with 7 wins, 1 tie, and 2 losses, and a cumulative 21 points.'
    }
    card2 = {
        'img_src': url_for('static', filename='img/conference-final.png'),
        'img_title': 'Conference Final Image',
        'title': 'Conference Final Nov 19!', 
        'text': 'Check out our final game on November 19th!'
    }
    card3 = {
        'img_src': url_for('static', filename='img/gufc-vs-goldsboro.jpg'),
        'img_title': 'GUFC vs Goldsboro',
        'title': 'GUFC wins 3 - 0 against Goldsboro', 
        'text': 'Greenville United wins the season finale with a final score of 3 to nill. Fantastic work Bucks!'
    }
    spotlight_cards = [card1, card2, card3]
    
    # Sponsors Initialization
    carolina_vision = {
        'img_src': url_for('static', filename='img/carolina-vision-logo.png'),
        'name': 'Carolina Vision Care Logo',
        'href': 'https://carolinavisioncare.com/'
    }
    
    botanic_tonics = {
        'img_src': url_for('static', filename='img/botanic-tonics-logo.png'),
        'name': 'Botanic Tonics Logo',
        'href': 'https://botanictonics.com/'
    }
    
    partners = [botanic_tonics]
    sponsors = [carolina_vision]
    
    title = 'GUFC Goes National!'
    return render_template('main/index.html', title=title, cards=spotlight_cards, partners=partners, sponsors=sponsors)

@main_bp.route('/terms-and-conditions')
def show_terms():
    return render_template('main/terms-conditions.html', title='Terms and Conditions')

@main_bp.route('/db-admin', methods=['GET', 'POST', 'PUT'])
def show_db_admin():
    if request.method == 'GET':
        return render_template('main/form.html')

@main_bp.route('/donate', methods=['GET', 'POST'])
def show_donate():
    if request.method == 'GET':
        # Create select statements using SQLAlchemy() db object
        total_stmt = db.select(Main.value).where(Main.id == 1)
        goal_stmt = db.select(Main.value).where(Main.id == 2)
        
        # execute statements against db session
        d_total = db.session.scalars(total_stmt).one()
        d_goal = db.session.scalars(goal_stmt).one()
        # d_total = 1500
        # d_goal = 50000
        g_percent = (d_total/d_goal)*100
        return render_template('partners/donation.html', title='Make a Donation', total=f"${d_total}.00", percent_of_goal=g_percent, goal=f"${d_goal}.00")
    elif request.method == 'POST':
        # Define form input/card vars
        amount = request.form['donations']
        f_name = request.form['fName']
        l_name = request.form['lName']
        email = request.form['email']
        phone = request.form['phone']
        card_name = request.form['name']
        
        cc = apicontractsv1.creditCardType()
        cc.cardNumber = request.form['cardNum']
        expM = request.form['expm']
        expY = request.form['expy']
        cc.expirationDate = f"{expY}-{expM}"
        cc.cardCode = request.form['cvv']
        b_zip = request.form['zip']
        
        # Charge the card
        charge_card_donation(f_name, l_name, email, phone, amount, cc, b_zip, "Greenville United Football Club Donation", "00004")
        
        # Select existing total value
        stmt = db.select(Main.value).where(Main.id == 1)
        total = db.session.scalars(stmt).one()
        # Create new updated total amount
        new_total = total + int(amount)
        
        # Update table with new value
        update_stmt = db.update(Main).where(Main.name == 'total').values(value=new_total).returning(Main.value)
        # print(update_stmt)
        db.session.scalars(update_stmt).one()
        # Commit changes
        db.session.commit()
        
        # Assign template vars
        htag = "Thank you for supporting us!"
        ptag = f"Thank you for donating to the Greenville United Football Club. Your donation of ${amount}.00 will help us in so many ways and it means a lot to our team, fans, club, and community."
        
        # Return 'Thank You' template with share donation enabled, and assigned template vars
        return render_template('main/thank-you.html', title='Thank you for your Donation', donated=True, htag=htag, ptag=ptag)


@main_bp.route('/site-map', methods=['GET'])
def show_site_map():
    about = { 'headerHref': url_for('about.show_index'), 'name': 'About', 'links': [ {'href': url_for('about.show_vmc'), 'name': 'Vision, Mission, Core'}, {'href': url_for('about.show_league'), 'name': 'League'}, {'href': url_for('about.show_club'), 'name': 'Club'}, {'href': url_for('about.show_team'), 'name': 'Team'},] }
    community = { 'headerHref': url_for('community.show_index'), 'name': 'Community', 'links': [ {'href': url_for('community.show_youth'), 'name': 'Youth'}, {'href': url_for('community.show_news'), 'name': 'Local News'}, {'href': url_for('community.show_schedule'), 'name': 'Schedule'},] }
    
    sections=[about, community]
    
    return render_template('main/site-map.html', title='Site Map', sections=sections)

@main_bp.route('/privacy-policy')
def show_pp():
    return render_template('store/privacy-policy.html', title='Privacy Policy')


# Helper Functions ----------------------------

def charge_card_donation(f_name, l_name, email, phone, amount, creditCard, b_zip, o_desc, o_inv_num):
    """
    Charge a credit card
    """
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    # TODO update static code below before deploying to production
    merchantAuth.name = config.DevelopmentConfig.API_LOGIN_ID
    merchantAuth.transactionKey = config.DevelopmentConfig.TRANSACTION_KEY

    # Create the payment data for a credit card
    creditCard = creditCard

    # Add the payment data to a paymentType object
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard

    # Create order information
    order = apicontractsv1.orderType()
    order.invoiceNumber = o_inv_num
    order.description = o_desc

    # Set the customer's Bill To address
    customerAddress = apicontractsv1.customerAddressType()
    customerAddress.firstName = f_name
    customerAddress.lastName = l_name
    customerAddress.zip = b_zip

    # Set the customer's identifying information
    customerData = apicontractsv1.customerDataType()
    customerData.type = "individual"
    customerData.email = email

    # Add values for transaction settings
    duplicateWindowSetting = apicontractsv1.settingType()
    duplicateWindowSetting.settingName = "duplicateWindow"
    duplicateWindowSetting.settingValue = "600"
    settings = apicontractsv1.ArrayOfSetting()
    settings.setting.append(duplicateWindowSetting)

    # setup individual line items
    line_item_1 = apicontractsv1.lineItemType()
    line_item_1.itemId = "000001"
    line_item_1.name = "GUFC Donation"
    line_item_1.description = o_desc
    line_item_1.quantity = "1"
    line_item_1.unitPrice = amount

    # build the array of line items
    line_items = apicontractsv1.ArrayOfLineItem()
    line_items.lineItem.append(line_item_1)

    # Create a transactionRequestType object and add the previous objects to it.
    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType = "authCaptureTransaction"
    transactionrequest.amount = amount
    transactionrequest.payment = payment
    transactionrequest.order = order
    transactionrequest.billTo = customerAddress
    transactionrequest.customer = customerData
    transactionrequest.transactionSettings = settings
    transactionrequest.lineItems = line_items
    
    # Assemble the complete transaction request
    createtransactionrequest = apicontractsv1.createTransactionRequest()
    createtransactionrequest.merchantAuthentication = merchantAuth
    createtransactionrequest.refId = "4445055366710"
    createtransactionrequest.transactionRequest = transactionrequest
    # Create the controller
    createtransactioncontroller = createTransactionController(
        createtransactionrequest)
    createtransactioncontroller.execute()

    response = createtransactioncontroller.getresponse()

    if response is not None:
        # Check to see if the API request was successfully received and acted upon
        if response.messages.resultCode == "Ok":
            # Since the API request was successful, look for a transaction response
            # and parse it to display the results of authorizing the card
            if hasattr(response.transactionResponse, 'messages') is True:
                print(
                    'Successfully created transaction with Transaction ID: %s'
                    % response.transactionResponse.transId)
                print('Transaction Response Code: %s' %
                      response.transactionResponse.responseCode)
                print('Message Code: %s' %
                      response.transactionResponse.messages.message[0].code)
                print('Description: %s' % response.transactionResponse.
                      messages.message[0].description)
                
                donation = Donation(amount=amount, first_name=f_name, last_name=l_name, email=email, phone=phone, zip_code=b_zip)
                db.session.add(donation)
                db.session.commit()
            else:
                print('Failed Transaction.')
                if hasattr(response.transactionResponse, 'errors') is True:
                    eC = 'Error Code:  %s' % str(response.transactionResponse.errors.error[0].errorCode)
                    eM = 'Error message: %s' % response.transactionResponse.errors.error[0].errorText
                    return render_template('400.html', errorCode=eC, errorMessage=eM)
                    
        # Or, print errors if the API request wasn't successful
        else:
            print('Failed Transaction.')
            if hasattr(response, 'transactionResponse') is True and hasattr(
                    response.transactionResponse, 'errors') is True:
                eC = 'Error Code: %s' % str(
                    response.transactionResponse.errors.error[0].errorCode)
                eM = 'Error message: %s' % response.transactionResponse.errors.error[0].errorText
                return render_template('500.html', errorCode=eC, errorMessage=eM)
            else:
                eC = 'Error Code: %s' % response.messages.message[0]['code'].text
                eM = 'Error message: %s' % response.messages.message[0]['text'].text
                return render_template('500.html', errorCode=eC, errorMessage=eM)
    else:
        print('Null Response.')
        abort(404)

    return response