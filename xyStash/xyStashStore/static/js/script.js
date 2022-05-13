const navSlide = () => {
    const burger = document.querySelector('.burger')
    const nav = document.querySelector('.primary-nav')
    const navLinks = document.querySelectorAll('.primary-nav li')

    burger.addEventListener('click', () => {
        //toggle nav
        nav.classList.toggle('nav-active');

        //anim nav links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            }
            else {
            
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
        //burger anim
        burger.classList.toggle('toggle');
    });    
}

navSlide();


document.addEventListener("DOMContentLoaded", function() {
  
    var userFeed = new Instafeed({
        get: 'user',
        target: "instafeed",
        resolution: 'thumbnail',
        accessToken: 'IGQVJWcHFyZA1dBT0d3NWsxYktaRnZASTWhOZAHdGalFBWUNXZAk1qVjVad1RJNXZADNGxGT28zaXRzZAUJkV1lTeHpHMG8tLUpuMUFqVHFNbU9VLVpCY2ktVTVVNVJBQzhxVHVoQjFGb2J5M3FqZAWw1dl9hRQZDZD',
        limit: 6,
        template: '<a href="{{link}}" target="_blank"><img src="{{image}}" /></a>'
    });
    userFeed.run();
     
  });