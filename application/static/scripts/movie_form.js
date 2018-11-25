var movie_preview_item = null;

window.onload = () => {
    var title_input = document.getElementById('input-title');
    var poster_input = document.getElementById('input-poster');
    var genres_input = document.getElementById('input-genres');
    var preview_item_cover = document.getElementById('movie-preview-item-cover');
    var preview_item_title = document.getElementById('movie-preview-item-title');
    var preview_item_genres = document.getElementById('movie-preview-item-genres');
    movie_preview_item = document.getElementById('movie-preview-item');

    title_input.onkeyup = () => {
        preview_item_title.innerHTML = getValue(title_input);
    }

    poster_input.onkeyup = () => {
        preview_item_cover.style.backgroundImage = "url('" + getValue(poster_input) + "')";
    }

    genres_input.onkeyup = () => {
        var genres = getValue(genres_input).split(",");
        var genres_text = "";
        for (var i = 0; i < genres.length; i++) {
            genres_text += genres[i].trim();
            if (i < genres.length - 1) genres_text += ", "
        }
        preview_item_genres.innerHTML = genres_text;
    }

    resizeCovers();
    rePositionPreviewItem();
}

/**
 * Get value of an element
 * @param {any} el Element whose value is wanted
 */
function getValue(el) {
    return el.value;
}

/**
 * Set value of an element
 * @param {any} el Element whose value should be set
 * @param {string} val New value for the element
 */
function setValue(el, val) {
    el.value = val;
}

// Moves movie preview item if the window shrinks to a small size so it doesn't overlap with other elements
window.onresize = () => {
    rePositionPreviewItem();
}

function rePositionPreviewItem() {
    if (window.innerWidth < 1250) {
        movie_preview_item.style.position = "relative";
        movie_preview_item.classList.add('movie-preview-item-left');
    }
    else {
        movie_preview_item.style.position = "absolute";
        movie_preview_item.classList.remove('movie-preview-item-left');
    }
}