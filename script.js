const mojDivVJs = document.getElementById("mojDivVJs")

fetch("students.json")
    .then((odpoved_raw) => odpoved_raw.json())
    .then((students) => {

        students.forEach((student) => {

            
            const card = document.createElement("div")
            card.style.display = "inline-block"
            card.style.margin = "10px"
            card.style.textAlign = "center"
            card.style.fontFamily = "Arial"
            
           
            const img = document.createElement("img")
            img.src = student.image
            img.width = 200
            img.alt = student.name
            img.style.borderRadius = "10px"
            img.style.boxShadow = "0 2px 6px rgba(0,0,0,0.2)"

            
            const name = document.createElement("p")
            name.textContent = student.name
            name.style.marginTop = "8px"
            name.style.fontWeight = "bold"

          
            card.appendChild(img)
            card.appendChild(name)

        
            mojDivVJs.appendChild(card)
        })
    })
    .catch((chyba) => {
        console.error("Nastala chyba pri fetch:", chyba)
    })
