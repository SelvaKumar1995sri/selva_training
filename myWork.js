
function myFunction() {
    axios
      .get("https://jsonplaceholder.typicode.com/users")
      .then(response => {
        console.log((JSON.stringify(response.data)));
        let data_value = JSON.stringify(response.data);
      document.getElementById("data").innerHTML = JSON.stringify(response.data[0]['name']);


      })
      .catch(error => console.error(error));
}