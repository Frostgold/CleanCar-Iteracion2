const carouselSlide = document.querySelector('#carousel-slide');
const carouselImages = document.querySelectorAll('#carousel-slide img');

const prevBtn = document.querySelector('#prevBtn');
const nextBtn = document.querySelector('#nextBtn');

let timer = setInterval(siguiente, 9000); //Timer imagenes
let counter = 1;
let size = carouselImages[0].clientWidth;
carouselSlide.style.transform = 'translateX('+ (-size * counter) + 'px)';

// Reset carousel al cambiar tamaño de la ventana
window.addEventListener("resize", cambioTamano);
function cambioTamano(){
    counter = 1;
    size = carouselImages[0].clientWidth;
    carouselSlide.style.transform = 'translateX('+ (-size * counter) + 'px)';
    clearInterval(timer);
    timer = setInterval(siguiente, 9000);
}

function siguiente() {
    if (counter >= carouselImages.length - 1) return;
    carouselSlide.style.transition = "transform 0.4s ease-out";
    counter++;
    carouselSlide.style.transform = 'translateX('+ (-size * counter) + 'px)';
    clearInterval(timer);
    timer = setInterval(siguiente, 9000);
};

nextBtn.addEventListener('click',() => {
    siguiente();
});

prevBtn.addEventListener('click',() => {
    if (counter <= 0) return;
    carouselSlide.style.transition = "transform 0.4s ease-out";
    counter--;
    carouselSlide.style.transform = 'translateX('+ (-size * counter) + 'px)';
    clearInterval(timer);
    timer = setInterval(siguiente, 9000);
});

carouselSlide.addEventListener('transitionend', () => {
    if (carouselImages[counter].id === 'lastClone') {
        carouselSlide.style.transition = 'none';
        counter = carouselImages.length -2;
        carouselSlide.style.transform = 'translateX('+ (-size * counter) + 'px)';
    }
    if (carouselImages[counter].id === 'firstClone') {
        carouselSlide.style.transition = 'none';
        counter = carouselImages.length -counter;
        carouselSlide.style.transform = 'translateX('+ (-size * counter) + 'px)';
    }
})