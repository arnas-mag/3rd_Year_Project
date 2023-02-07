// Displaying the date dynamically in the html
function displayDate() {
    var date = new Date();
    document.getElementById("demo").innerHTML = date.toLocaleDateString() + " " + date.toLocaleTimeString();
  }
  setInterval(displayDate, 1000);