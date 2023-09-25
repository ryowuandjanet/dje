$(document).ready(function(){

  $('.payWithRazorpay').click(function (e){
    e.preventDefault()

    var fname = $("[name='fname']").val()
    var email = $("[name='email']").val()
    var phone = $("[name='phone']").val()
    var address = $("[name='address']").val()
    var city = $("[name='city']").val()
    var pincode = $("[name='pincode']").val()
    var token = $("[name='csrfmiddlewaretoken']").val()

    if(fname == "" || email == "" || phone == "" || address == "" || city == "" || pincode == "")
    {
      Swal.fire("Alert!","All fields are mandatory !","error")
      return false
    }
    else{
      $.ajax({
        method: "GET",
        url: "/proceed-to-pay",
        success: function (response){
          var options = {
            "key": "rzp_test_Hn11IJH2YVC3ZJ", // Enter the Key ID generated from the Dashboard
            "amount": 1 * 100,
            "currency": "INR",
            "description": "Acme Corp",
            "name":"ryowu",
            "image": "https://s3.amazonaws.com/rzp-mobile/images/rzp.jpg",
            "handler": function (responseb) {
              alert(responseb.razorpay_payment_id);
              data = {
                "fname": fname,
                "email": email,
                "phone": phone,
                "address": address,
                "city": city,
                "pincode": pincode,
                "payment_mode": "Paid by Razorpay",
                "payment_id": responseb.razorpay_payment_id,
                csrfmiddlewaretoken: token
              }
              $.ajax({
                method: "POST",
                url: "/place-order",
                data: data,
                success: function(responsec){
                  Swal.fire("Congratulations!",responsec.status,"success").then((value) => {
                    window.location.href = 'my-orders'
                  })
                }
              })
            },
            "prefill": {
              "name": fname,
              "email": email,
              "contact": phone,
            },
            "theme": {
              "color": "#3399cc"
            }
          };
          var rzp1 = new Razorpay(options);
          rzp1.open();
        }
      })
      
    }
    
  })
})