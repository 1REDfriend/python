function switchmode() {
    var body = document.body;
    var card = document.getElementsByClassName('CardMe')[0];
    var header = document.querySelector("body > header > button")
    var h1 = document.getElementsByTagName("h1");

    body.classList.toggle("light-mode-body");
    body.classList.toggle("light-mode-text");
    card.classList.toggle("light-mode-card");
    card.classList.toggle("light-mode-text");
    header.classList.toggle("light-mode-card");
    header.classList.toggle("light-mode-text");
    for (var i = 0; i < h1.length; i++) {
        h1[i].classList.toggle("light-mode-text");
    }
}