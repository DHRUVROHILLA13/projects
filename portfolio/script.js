document.addEventListener("DOMContentLoaded", function() {
    // Highlight the active link
    var currentPage = window.location.pathname.split("/").pop(); // Get the current page filename
    var links = document.querySelectorAll("nav ul li a");
    links.forEach(function(link) {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    });

    // Smooth scroll animation for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
