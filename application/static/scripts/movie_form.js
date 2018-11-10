window.onload = () => {
    var title_input = document.getElementById('input-title');
    var poster_input = document.getElementById('input-poster');
    var preview_item_cover = document.getElementById('movie-preview-item-cover');
    var preview_item_title = document.getElementById('movie-preview-item-title');

    title_input.onkeyup = () => {
        preview_item_title.innerHTML = getValue(title_input);
    }

    poster_input.onkeyup = () => {
        preview_item_cover.style.backgroundImage = "url('" + getValue(poster_input) + "')";
    }

    resizeCovers();
}

/**
 * Get value of an element
 * @param {any} el Element whose value is wanted
 */
function getValue(el) {
    return el.value;
}