var title = $( ".product-heading" );
var prodId = $( "#prod-id" );
var size = $( "#size" );
var sBtn = $( "#sBtn" );
var mBtn = $( "#mBtn" );
var lBtn = $( "#lBtn" );
var xlBtn = $( "#xlBtn" );
var xxlBtn = $( "#2xlBtn" );

sBtn.on( "click", function(e) {
    size.html("S");
});

mBtn.on( "click", function(e) {
    size.html("M");
});

lBtn.on( "click", function(e) {
    size.html("L");
});

xlBtn.on( "click", function(e) {
    size.html("XL");
});

xxlBtn.on( "click", function(e) {
    size.html("2XL");
});
