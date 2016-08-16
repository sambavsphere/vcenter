function tabulate(data, columns) {
    var table = d3.select(".data_table").append("table")
    				.attr('class','table-bordered')
    				.attr('id','table_data')
        thead = table.append("thead"),
        tbody = table.append("tbody");

    // append the header row
    thead.append("tr")
        .selectAll("th")
        .data(columns)
        .enter()
        .append("th")
            .text(function(column) { return column; });

    // create a row for each object in the data
    var rows = tbody.selectAll("tr")
        .data(data)
        .enter()
        .append("tr");

    // create a cell in each row for each column
    var cells = rows.selectAll("td")
        .data(function(row) {
            return columns.map(function(column) {
                return {column: column, value: row[column]};
            });
        })
        .enter()
        .append("td")
            .html(function(d) { return d.value; });
    
    return table;
}



$(function(){

	var data = JSON.parse($('.data').val())
	var header = JSON.parse($('.header').val())
	var am = $('.am').val()

	// active menu
	$("#"+am).addClass("active")
	var table = $('.data_table')
	d3.select('.data_table').selectAll("table").remove()
	tabulate(data,header)
	$('#table_data').DataTable();


})