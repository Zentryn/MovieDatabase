// Resizes all movie covers to their appropriate heights
function resizeCovers() {
    var covers = document.getElementsByClassName('movie-item-cover');

    for (var i = 0; i < covers.length; i++) {
        setHeight(covers[i], String(covers[i].clientWidth * 1.482) + "px");
    }
}

window.onload = resizeCovers;

window.onresize = () => {
    resizeCovers();
}

/**
 * Sets the height for an element
 * @param {any} el The element whose style should be changed
 * @param {String} value The height wanted
 */
function setHeight(el, value) {
    el.style.height = value;
}

setTimeout(() => {
    resizeCovers();
});