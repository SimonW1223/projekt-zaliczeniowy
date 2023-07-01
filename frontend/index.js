fetch("https://reqres.in/api/users", {
    method: "POST",
    body: JSON.stringify({
        name: "Customer 1"
    })
}).then(res => {
    return res.json()
})
.then(data => console.log(data))
.catch(error => console.log("ERROR"))