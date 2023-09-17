$(document).ready(function(){
  $('.increment-btn').click(function(e){
    e.preventDefault()
    var inc_value = $(this).closest('.product_data').find('.qty-input').val()
    var value = parseInt(inc_value,10)
    value = isNaN(value) ? 0 : value;
    if(value < 10000)
    {
      value++;
      $(this).closest('.product_data').find('.qty-input').val(value)
    }
  });

  $('.decrement-btn').click(function(e){
    e.preventDefault()
    var dec_value = $(this).closest('.product_data').find('.qty-input').val()
    var value = parseInt(dec_value,10)
    value = isNaN(value) ? 0 : value;
    if(value > 1)
    {
      value--;
      $(this).closest('.product_data').find('.qty-input').val(value)
    }
  });

  $('.addToCartBtn').click(function(e){
    e.preventDefault();
    console.log('click cart');
    var product_id = $(this).closest('.product_data').find('.prod_id').val()
    var product_qty = $(this).closest('.product_data').find('.qty-input').val()
    var token = $('input[name=csrfmiddlewaretoken]').val()
    
    $.ajax({
      method: "POST",
      url: "/add-to-cart",
      data: {
        "product_id":product_id,
        "product_qty":product_qty,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        console.log(response)
        alertify.success(response.status)
      }
    })
  })

  $('.getRemarkBtn').click(function(e){
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.prod_id').val()
    var product_qty = $(this).closest('.product_data').find('.qty-input').val()
    var remark = $(this).closest('.product_data').find('.remark-input').val()
    var token = $('input[name=csrfmiddlewaretoken]').val()
    console.log(product_qty)
    console.log('1111')
    
    console.log(remark)
    
    $.ajax({
      method: "POST",
      url: "/update-remark",
      data: {
        "product_id":product_id,
        "product_qty":product_qty,
        "remark":remark,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        console.log(response)
        alertify.success(response.status)
      }
    })
    
  })




  $('.addToWishlist').click(function(e){
    e.preventDefault();
    console.log('click wishlist');
    var product_id = $(this).closest('.product_data').find('.prod_id').val()
    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
      method: "POST",
      url: "/add-to-wishlist",
      data: {
        "product_id":product_id,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        alertify.success(response.status)
      }
    })
  })

  $('.updateCart').click(function(e){
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.prod_id').val()
    var product_qty = $(this).closest('.product_data').find('.qty-input').val()
    var remark = $(this).closest('.product_data').find('.remark-input').val()
    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
      method: "POST",
      url: "/update-cart",
      data: {
        "product_id":product_id,
        "product_qty":product_qty,
        "remark":remark,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        console.log(response)
        alertify.success(response.status)
      }
    })
  })

  $('.delete-cart-item').click(function(e){
    e.preventDefault();
    console.log('delete-cart-item')
    var product_id = $(this).closest('.product_data').find('.prod_id').val()
    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
      method: "POST",
      url: "delete-cart-item",
      data: {
        "product_id":product_id,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        alertify.success(response.status)
        // 後面要空一格才可以，" .cartdata"
        $('.cartdata').load(location.href + " .cartdata")
      }
    })
  })

  $(document).on('click','.delete-wishlist-item',function(e){
    e.preventDefault();
    console.log('delete-cart-item')
    var product_id = $(this).closest('.product_data').find('.prod_id').val()
    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
      method: "POST",
      url: "delete-wishlist-item",
      data: {
        "product_id":product_id,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        alertify.success(response.status)
        // 後面要空一格才可以，" .wishdata"
        $('.wishdata').load(location.href + " .wishdata")
      }
    })
  })
})

