  
function tooltip(n, d){
	return "<h4>"+n+"</h4><table>"+
		"<tr><td>% Violations</td><td>"+Math.round(d.PercentLocViolations)+"</td></tr>"+
		"<tr><td>Total Violations</td><td>"+(d.TotalViolations)+"</td></tr>"+
		"</table>";
}

    var sampleData ={};     
    d3.csv("../raw-data.csv", function(data){
    var color = d3.scale.linear()
      .range(["#ebebeb","#c40018"])
      .domain([d3.min(data, function(d) { return d.PercentLocViolations/100; }), d3.max(data, function(d) { return d.PercentLocViolations/100; }) ])
    data.forEach(function(d) {
      sampleData[d.Abbreviation] = { 
      PercentLocViolations : d.PercentLocViolations, 
      TotalViolations : d.TotalViolations, 
      color : color(d.PercentLocViolations/100)
      };
    });
    counties.draw("#", sampleData, tooltip);
    });