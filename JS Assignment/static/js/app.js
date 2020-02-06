// from data.js
var tableData = data;

var tbody = d3.select("tbody");

function buildTable(data) {

  tbody.html("");

  data.forEach((dRow) => {

    var tr = tbody.append("tr");

    Object.values(dRow).forEach((val) => {
      var td = tr.append("td");
        td.text(val);
      }
    );
  });
}

function handleClick() {

  d3.event.preventDefault();

  var dateTime = d3.select("#datetime").property("value");
  let filteredData = tableData;

  if (dateTime) {

    filteredData = filteredData.filter(tr => tr.datetime === dateTime);
  }

  buildTable(filteredData);
}

