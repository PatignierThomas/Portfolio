const form = document.querySelector('form');

form.addEventListener("submit", (event) => {

    fetch(form.action, {
        method: form.method,
        body: new FormData(form),
    })
    .then(response =>
    response.json()
    )
    .then(json => {
        let inputfield = document.getElementById("endPassword")
        inputfield.value = json.condition
    })


    event.preventDefault()
    })

