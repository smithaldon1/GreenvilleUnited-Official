$(document).ready(function(){
    console.log("ready!");
});

$('#radio4').click(() => {
    $('#other-input').removeAttr('readonly').removeClass('form-control-plaintext');
});

$('.s-radio').click(() => {
    $('#other-input').attr('readonly', 'readonly').addClass('form-control-plaintext');
});

// Add checkout amount to pay button
$('#c-btn').click(() => {
    var amount = $('input[name=donations]:checked').val();
    var other = $('#other-input').val();
    if ($('#radio4:checked').length === 1) {
        $('#p-btn').text("Pay $" + other);
        var amount1 = $('#radio4').attr('value', other);
        console.log('radio4 amount: ', amount1)
    } else {
        $('#p-btn').text("Pay $" + amount);
        console.log(amount);
    }
});


function sendPaymentDataToAnet() {
    var authData = {};
    authData.clientKey = '32FUq27PnXR2fytsBqGMpZTknJ57spKJN8h5nZ9J647ZHa4d2a4kAf57mTMaBAam';
    authData.apiLoginId = '2JjBw86h';

    var cardData = {};
    cardData.fullName = $('#name').val();
    cardData.cardNumber = $('#card').val();
    cardData.month = $('#expm').val();
    cardData.year = $('#expy').val();
    cardData.cardCode = $('#cvv').val();

    var secureData = {};
    secureData.authData = authData;
    secureData.cardData = cardData;

    Accept.dispatchData(secureData, (response) => {
        if (response.messages.resultCode === "Error") {
            var i = 0;
            while (i < response.messages.length) {
                console.log(
                    response.messages.message[i].code + ": " + response.messages.message[i].text
                );
                i = i + 1;
            }
        } else {
            paymentFormUpdate(response.opaqueData);
        }
    });
    console.log('AuthData: ' + authData, 'CardData: ' + cardData);
};

function paymentFormUpdate(opaqueData) {
    // Update hidden inputs with payment nonce information
    $('#dataDescriptor').val(opaqueData.dataDescriptor);
    $('#dataValue').val(opaqueData.dataValue);

    // Clear form values
    $('#fName').val("");
    $('#lName').val("");
    $('#email').val("");
    $('#phone').val("");
    $('#name').val("");
    $('#card').val("");
    $('#expm').val("");
    $('#expy').val("");
    $('#cvv').val("");

    // Submit Data Form
    $('#paymentForm').submit();
};
