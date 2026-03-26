async function getData() {
    URL = "https: //jsonplaceholder.typicode.com/users";
    try {
const response = await fetch (URL);
const data = await response.jason();
console.log(data);
    }
    catch(error) {
        console.log(error);
    }
}
getData();