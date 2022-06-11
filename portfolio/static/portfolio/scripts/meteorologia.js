    var weatherSubmit = document.querySelector('.weatherSubmitCity')
    var maxTemp = document.querySelector('.maxTemp')
    var minTemp = document.querySelector('.minTemp')
    var dataTemp = document.querySelector('.data')

    window.onload = function(){
     fetch('//api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            maxTemp.innerHTML = data['data'][0]['tMax'];
            minTemp.innerHTML = data['data'][0]['tMin'];
            dataTemp.innerHTML = data['data'][0]['forecastDate'];
        })
    }
