const search_icon = $("#search-icon")
const endpoint = "/products/"
const delay_in_ms = 700
let scheduled_function = false

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
      products_div.html(response["html_from_view"])
      // fade in the div with new content
      products_div.fadeTo('slow', 1)
      // stop animating search icon
      search_icon.removeClass('blink');
      // $('#exampleModal').modal({show: true});
    })
  })
}