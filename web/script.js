var light = false;

function switchmode() {
    var body = document.body;
    var card = document.getElementsByClassName('CardMe')[0];
    var header = document.querySelector("body > header > button")
    var h1 = document.getElementsByTagName("h1");
    var img = document.getElementById("img")

    body.classList.toggle("light-mode-body");
    body.classList.toggle("light-mode-text");
    card.classList.toggle("light-mode-card");
    card.classList.toggle("light-mode-text");
    header.classList.toggle("light-mode-card");
    header.classList.toggle("light-mode-text");

    light = !light

    if (light) {
        document.getElementById("mode").textContent = "Light Mode"
        img.src = "https://images.pexels.com/photos/2817430/pexels-photo-2817430.jpeg?cs=srgb&dl=pexels-d%C6%B0%C6%A1ng-nh%C3%A2n-2817430.jpg&fm=jpg"
    } else {
        document.getElementById("mode").textContent = "Dark Mode"
        img.src = "https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/397881539_122104202516093412_1216137457645425803_n.jpg?stp=cp6_dst-jpg&_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEWPPZ6qmDfTaC8acwoY0Vkg3QhPB0oBTODdCE8HSgFM4yCLdz1vP_B1OoCS6iZrEXSesRE03YklryOKUgjVwUW&_nc_ohc=kyjnNJbinRMAX8QLUTB&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfB8IwQGPpxBV1I9PwlmoLmhwcm8_etqlZeW7d45n1Uw2g&oe=654E9B7D"
    }

    for (var i = 0; i < h1.length; i++) {
        h1[i].classList.toggle("light-mode-text");
    }
}