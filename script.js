const mojDivVJs = document.getElementById("mojDivVJs")

fetch("https://boozeapi.com/api/v1/cocktails")
    .then((odpoved_raw) => odpoved_raw.json())
    .then((odpoved) => {
        console.log(odpoved.data)

        odpoved.data.forEach((drink) => {
            const drinkImg = document.createElement("img")
            drinkImg.src = drink.image
            drinkImg.width = 200

            mojDivVJs.appendChild(drinkImg)
        })
    })
    .catch((chyba) => {
        console.error("Nastala chyba pri fetch:", chyba)
    })
    