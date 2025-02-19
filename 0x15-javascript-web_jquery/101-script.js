$(document).ready(function () {
  $("DIV#add_item").click(function () {
    $("<li>Item</li>").appendTo("ul.my_list");
  });

  $("DIV#remove_item").click(function () {
    $("ul.my_list li:last-child").remove();
  });

  $("DIV#clear_list").click(function () {
    $("ul.my_list").empty();
  });
});
