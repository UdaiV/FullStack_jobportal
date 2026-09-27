/* Skillhunt Interactive Logic Engine */
document.addEventListener("DOMContentLoaded", function () {
    console.log("Skillhunt web framework components loaded successfully.");
    
    // Smooth navbar shadow transitions on page scroll down
    window.addEventListener("scroll", function () {
        const nav = document.querySelector(".custom-nav");
        if (nav) {
            if (window.scrollY > 40) {
                nav.classList.add("shadow-lg");
            } else {
                nav.classList.remove("shadow-lg");
            }
        }
    });
});
