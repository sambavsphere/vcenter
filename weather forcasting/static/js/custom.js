$(function(){
	var weathers=JSON.parse($('.weathers').val())
	var today = new Date().getTime() 
	var dates =[]
	var temparatures = []
	var humidities = []
	for (var i=0;i<weathers.length;i++){
		row=""
		weather = JSON.parse(weathers[i])
		console.log(weather)
		var temparature = Math.round(weather.temperature.day/32)
		var status = weather.detailed_status
		var humidity = weather.humidity
		var date = new Date(today)
		today = today + 86400000
		var sr=date.toDateString()
		var month = sr.slice(3,7)
		var dt = date.getDate()
		var display_date = month+" "+dt
		dates.push(display_date)
		temparatures.push(temparature)
		humidities.push(humidity)
		if(i==0){
			$('.numbers').text(temparature)
			$('.status').text(status)
			$('.humidity').text(humidity+"% HUMIDITY")
		}
	}
	wts=[dates,temparatures,humidities]
	for (k=0;k<3;k++){
		row="<tr>"
		for(var j=0;j<5;j++){
			if(k==1){
				row=row+"<td><b>"+wts[k][j]+"</b></td>"
			}else{
				row=row+"<td>"+wts[k][j]+"</td>"
			}
			
		}
		row=row+"</tr>"
		$('.weather').append(row)

	}

	




})