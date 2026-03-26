const promise2 = new Promise ((resolve, reject) => {
    let arrived  = true;
    if (driver) {
        setTimeout(() => {
            resolve("Has arrived");
        }, 3000);
    } else {
        reject("Driver Declined");
    }
    });
    promise2
    .then(result => console.log(result))
    .catch(error => console.log(error));