// Add slight shadow to navbar on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 10) {
        navbar.style.boxShadow = '0 10px 15px -3px rgba(13, 110, 253, 0.1)';
    } else {
        navbar.style.boxShadow = '0 4px 6px rgba(13, 110, 253, 0.05)';
    }
});
