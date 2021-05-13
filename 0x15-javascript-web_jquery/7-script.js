$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => $('character').text(data.name));
