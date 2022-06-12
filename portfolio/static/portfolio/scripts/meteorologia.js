
    const sunny = [0,1]
    const cloudy = [2, 3, 4, 5, 17, 24, 25, 26, 27, ]
    const rain = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 23]
    const snow = [18, 21, 22, 28, 29, 30]

    window.onload = function(){
        weather()
    };

    function weather(){

        var maxTemp = document.querySelector('.maxTemp')
        var minTemp = document.querySelector('.minTemp')



        fetch('//api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                maxTemp.innerHTML = "Max: " + data['data'][0]['tMax'] + "Cº";
                minTemp.innerHTML = "Min: " + data['data'][0]['tMin'] + "Cº";

                var weatherId = data['data'][0]['idWeatherType'];
                var weatherIcon = "";

                if (sunny.includes(weatherId)){
                    weatherIcon = "sun.png"
                }else if(cloudy.includes(weatherId)){
                    weatherIcon = "cloud.png"
                }else if(rain.includes(weatherId)){
                    weatherIcon = "rain.png"
                }else if(snow.includes(weatherId)){
                    weatherIcon = "cloud.png"
                }

                document.getElementById("weatherImage").src = "portfolio/static/portfolio/images/" + weatherIcon;
            })
    }
