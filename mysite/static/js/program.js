$( document ).ready(function() {
  var list_date  = [
    "Sunday November 18th",
    "Monday November 19th",
    "Tuesday November 20th",
    "Wednesday November 21st",
    "Thursday November 22nd"
   ]
  var list_event =  [
    [
      "12:00–18:00","Registration",
    ],
    [
      "8:00–8:30","Registration (cont.)",
      "8:30–9:00","Welcoming address",
      "9:00–10:00","Plenary 1 – Robert J. Raven",
      "10:00–10:30","Coffee break",
      "10:30–12:30","Oral session",
      "12:30–14:00","Lunch",
      "14:00–16:00","Oral session",
      "16:00–16:30","Coffee break",
      "16:30–17:30","Poster session",
      "18:30","Welcoming banquet in meeting hall floor 20"
    ],
    [
      "8:00–9:00","Registration (cont.)",
      "9:00–10:00","Plenary 2 – Deborah R. R. Smith",
      "10:00–10:30","Coffee break",
      "10:30–12:30","Oral session",
      "12:30–14:00","Lunch",
      "14:00–16:00","Oral session",
      "16:00–16:30","Coffee break",
      "16:30–17:30","Oral session",
      "17:30–18:30","Poster session"
    ],
    [
      "7:00–9:00","Bus to KMUTT, Ratchaburi campus",
      "9:00–17:00","Excursion",
      "17:00–19:00","Bus to CU"
    ],
    [
      "9:00–10:00","Oral session",
      "10:00–10:30","Coffee break",
      "10:30–12:30","Oral session",
      "12:30–14:00","Lunch",
      "14:00–16:00","Oral session",
      "16:00–16:30","Coffee break",
      "16:30–18:30","Poster award and closing session",

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
