// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Show merged models when checkbox is checked
var input = document.getElementById('merged-models-checkbox')
if (input) {
  var filterMergedModels = function() {
    var table = document.getElementsByTagName('tbody')[0];
    var rows = table.getElementsByTagName('tr');
    var bgColours = ['#ffffff', 'rgb(228,228,228)'];
    var bgColour = bgColours[0];
    for (var i = 0; i < rows.length; i++) {
      if (input.checked) {
        rows[i].style.display = 'table-row';
        rows[i].style.backgroundColor = bgColour;
      } else {
        if (rows[i].classList.contains('merged-model')) {
          rows[i].style.display = 'none';
        } else {
          rows[i].style.display = 'table-row';
          rows[i].style.backgroundColor = bgColour;
        }
      }
      bgColour = bgColours[bgColours.indexOf(bgColour) ^ 1];
    }
  }
  input.addEventListener('change', filterMergedModels)
  filterMergedModels()
}
