const apiKey = 'f5a4f965000b48118e5160713232410';
var locationName = 'Kollam'; 

const weatherInfoElement = document.getElementById('weather-info');
const inputField = document.getElementById('inputField');
const backgroundChange = document.getElementById('body2');


function changeBackgroundImage(imageURL) {
    backgroundChange.style.backgroundImage = 'url(' + imageURL + ')';
}

document.getElementById("search").addEventListener("click", function() {
    console.log(inputField.value)
    locationName=inputField.value;
    fetch('https://api.weatherapi.com/v1/current.json?key=' + apiKey + '&q=' + locationName)
   .then(response => response.json())
   .then(data => {
       console.log(data);
       weatherInfoElement.innerHTML = `
           <p>Location: ${data.location.name}, ${data.location.country}</p>
           <p>Temperature: ${data.current.temp_c}°C</p>
           <p text-align: 'center'> ${data.current.condition.text}</p>
       `;
       if(data.current.condition.text.includes('Sunny')){
        changeBackgroundImage('assets/cloudy.jpg');
       }
       else{
        changeBackgroundImage('assets/rainy.jpg');
       }
   })
   .catch(error => {
       console.error('Error:', error);
       weatherInfoElement.textContent = 'Error: city not found';
   });
   inputField.value = '';
});




