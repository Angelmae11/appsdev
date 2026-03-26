const promise2 = new Promise ((resolve, reject) => {
    let arrived  = true;
    if (driver) {
        resolve("Has arrived");
    } else {
        reject("Driver Declined");
    }
    });
    promise2
    .then(result => console.log(result))
    .catch(error => console.log(erro));