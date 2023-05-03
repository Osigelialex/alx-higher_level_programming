$(document).ready(function() {
  const url = "https://fourtonfish.com/hellosalut/?lang=fr";
  $.get(url, function(data) {
    $("#hello").text(data.hello);
  });
});
