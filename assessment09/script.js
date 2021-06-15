var tds = document.querySelectorAll("td");
for (t of tds) {
  t.addEventListener("click", function() {
    if (this.textContent.length === 0) this.textContent = 'X';
    else if (this.textContent === 'X') this.textContent = 'O';
    else if (this.textContent === 'O') this.textContent = '';
  })
}

var button = document.querySelector("button");
button.addEventListener("click", function() {
  for (t of tds) {
    t.textContent = '';
  }
})
