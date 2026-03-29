const mojDivVJs = document.getElementById("mojDivVJs")

fetch("students.json")
    .then((odpoved_raw) => odpoved_raw.json())
    .then((students) => {
        console.log("Načítané dáta:", students)

        students.forEach((student) => {
            const img = document.createElement("img")
            img.src = student.image
            img.width = 200
            img.alt = student.name

            mojDivVJs.appendChild(img)
        })
    })
    .catch((chyba) => {
        console.error("Nastala chyba pri fetch:", chyba)
    })