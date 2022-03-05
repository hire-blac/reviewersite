const search_icon = $("#search-icon")
const endpoint = "/product/"
const delay_in_ms = 700
let scheduled_function = false
const product_input_div = $('#form-input-replacable-content')

// hide all input fields for new product
$('.many-attributes input').hide();

const category = $('#id_category')
category.change(function(){
  const cat = $(this).val()
  $('.many-attributes input').hide();

  switch (cat) {
    case '1':
      console.log($(this).val());
      $('.many-attributes .music').show();
      break;
    case '2':
      $('.many-attributes .car').show();
      break;
    case '34':
      $('.many-attributes .book').show();
      break;
    case '35':
      $('.many-attributes .others').show();
      break;
  }
})

// search for product
function search(element) {
  const search_input = element.id
  const display_div = search_input + "-replacable-content"
  const user_input = $('#' + search_input)
  products_div = $("#" + display_div)
  
  user_input.on('keyup', function(){
    const request_parameters = {
      q: $(this).val() // value of user input for html element with id user-input
    }
  
    // start snimating the search icon
    search_icon.addClass('blink')
    
    // cancel execution of function if scheduled_function is NOT false
    if (scheduled_function) {
      clearTimeout(scheduled_function)
    }
  
    // setTimeout returns the id of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_in_ms, endpoint, request_parameters)
  })
}

let ajax_call = function (endpoint, request_parameters) {
  $.getJSON(endpoint, request_parameters)
  .done(response => {
    // fade out the products_div
    products_div.fadeTo('slow', 0).promise().then(()=>{
      // replace the html content
      products_div.html(response["html_from_view"]);
      product_input_div.html(response["html_for_input"]);
      // fade in the div with new content
      products_div.fadeTo('slow', 1)
      // stop animating search icon
      search_icon.removeClass('blink');
      // $('#exampleModal').modal({show: true});
    })
  })
}

// hide every comment box
$('.comment-box').hide()

// event handler for comment button to toggle comment form
$('.comment-button').on('click', function () {
  // find parent div of (this)element with class review
  var $vn = $(this.closest('.review'))

  // find child element with class comment-box
  var comment = $vn.find('.comment-box')

  // toggle comment-box with callback to hide other comment-boxes
  comment.toggle(function(){
    $(this).find('textarea').focus()
    $('.comment-box').not($(this)).hide()
  })
})