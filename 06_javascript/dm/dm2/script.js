let slideIndex = 1;

function slides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let slides = document.getElementsByClassName("slides");

    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "block";
}

let timeout;
function auto() {
    document.getElementById("prev").style.display = "none";
    document.getElementById("next").style.display = "none";
    document.getElementById("auto").disabled = "disabled";
    document.getElementById("pause").disabled = "";

    showSlidesAuto();

    function showSlidesAuto() {
        let slides = document.getElementsByClassName("slides");

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        slideIndex++;

        if (slideIndex > slides.length) {slideIndex = 1}
        
        slides[slideIndex - 1].style.display = "block";

        timeout = setTimeout(showSlidesAuto, 2000);
    }
}

function pause() {
    document.getElementById("prev").style.display = "block";
    document.getElementById("next").style.display = "block";
    document.getElementById("auto").disabled = "";
    document.getElementById("pause").disabled = "disabled";

    clearTimeout(timeout);
}
