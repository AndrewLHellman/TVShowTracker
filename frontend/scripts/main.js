// Code not generated by ChatGPT but functions and methods were searched for using ChatGPT. Sadly all the code was painstakingly handwritten (I need to learn frameworks)
const mainContainer = document.querySelector("main");

let containerNum = 6;
let arrestedDevelopmentDesc = "Arrested Development is an American television sitcom created by Mitchell Hurwitz. It aired on Fox for three seasons from November 2, 2003, to February 10, 2006, followed by two seasons on Netflix, season four being released in 2013 and season five being released in 2018 and 2019."
let arrestedDevelopmentGenre = "Comedy"
let arrestedDevelopmentRecs = ["Tessa", "Andrew", "LeeAnn", "Jenaya"]

function createShowRec () {
    let showContainer = document.createElement("div");
    showContainer.className = "showContainer";
    showContainer.id = `show-${containerNum}`;

    let showImage = document.createElement("img");
    showImage.className = "showImage";
    showImage.id = `showImg-${containerNum}`;
    showImage.src = "images/ArrestedDevelopment.jpg"
    showContainer.appendChild(showImage);

    let showText = document.createElement("div");
    showText.className = "showText";
    showText.id = `showText-${containerNum}`;

    let showDesc = document.createElement("p");
    showDesc.className = "showDesc";
    showDesc.textContent = arrestedDevelopmentDesc;
    showText.appendChild(showDesc);

    let showGenre = document.createElement("p");
    showGenre.className = "showGenre";
    showGenre.textContent = `Genre: ${arrestedDevelopmentGenre}`;
    showText.appendChild(showGenre);

    let recommenders = document.createElement("p");
    recommenders.className = "recommenders";
    recommenders.textContent = "Recommenders: ";
    
    for (let i = 0; i < arrestedDevelopmentRecs.length; i++) {
        let recommender = document.createElement("span");
        recommender.textContent = arrestedDevelopmentRecs[i];
        recommenders.appendChild(recommender);
    }
    
    showText.appendChild(recommenders);

    showContainer.appendChild(showText);
    containerNum++;
    mainContainer.appendChild(showContainer);
}

myButton.onclick = () => {
    createShowRec();
};