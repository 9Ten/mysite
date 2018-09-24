$( document ).ready(function() {
  var list_date  = [
    "Sunday November 19th",
    "Monday November 20th",
    "Tuesday November 21st",
    "Wednesday November 22nd"
   ]
  var list_event =  [
    [
      "xx:xx-xx:xx","Waiting For Data",
    ],
    [
      "xx:xx-xx:xx","Waiting For Data",
    ],
    [
      "xx:xx-xx:xx","Waiting For Data",
    ],
    [
      "xx:xx-xx:xx","Waiting For Data",
    ]
  ]
  var table = document.createElement('table');
  var tbody = document.createElement('tbody');
  for (var i = 0; i < list_date.length; i++) {
    var th = document.createElement('th');
    th.appendChild(document.createTextNode(list_date[i]));
    th.colSpan  = 2;
    var tr = document.createElement('tr');
    var td = document.createElement('td');
    td.appendChild(document.createTextNode("TIME"));
    tr.appendChild(td);
    var td = document.createElement('td');
    td.appendChild(document.createTextNode("ACTIVITIES"));
    tr.appendChild(td);
    tbody.appendChild(th);
    tbody.appendChild(tr);
    var currentdate_events = list_event[i];
    var tr = document.createElement('tr');
    for (var j = 0; j < currentdate_events.length; j++) {
      var td = document.createElement('td');
      if (j%2!=0) {
        td.appendChild(document.createTextNode(currentdate_events[j]));
        tr.appendChild(td);
        tbody.appendChild(tr);
        var tr = document.createElement('tr');
      }
      else {
        td.appendChild(document.createTextNode(currentdate_events[j]));
        tr.appendChild(td);
      }
    }
  }
  table.appendChild(tbody);
  table.classList.add('schedule');
  var div = document.getElementById("table_programs");
  div.appendChild(table);
});
