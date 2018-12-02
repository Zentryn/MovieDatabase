var title_input = null;
var poster_input = null;
var backdrop_input = null;
var background = null;
var genres_input = null;
var item_cover = null;
var item_title = null;
var item_genres = null;

$(document).ready(() => {
    title_input = document.getElementById('input-title');
    poster_input = document.getElementById('input-poster');
    backdrop_input = document.getElementById('input-backdrop');
    background = document.getElementById('background');
    genres_input = document.getElementById('input-genres');
    item_cover = document.getElementById('movie-item-cover');
    item_title = document.getElementById('movie-item-title');
    item_genres = document.getElementById('movie-item-genres');

    title_input.onkeyup = () => {
        updateInputs();
    }

    poster_input.onkeyup = () => {
        updateInputs();
    }

    backdrop_input.onkeyup = () => {
        updateInputs();
    }

    genres_input.onkeyup = () => {
        updateInputs();
    }

    updateInputs();
});

function updateInputs() {
    item_title.innerHTML = getValue(title_input);
    item_cover.style.backgroundImage = "url('" + getValue(poster_input) + "')";
    background.style.backgroundImage = "url('" + getValue(backdrop_input) + "')";

    var genres = getValue(genres_input).split(",");
        var genres_text = "";
        for (var i = 0; i < genres.length; i++) {
            genres_text += genres[i].trim();
            if (i < genres.length - 1) genres_text += ", "
        }
        item_genres.innerHTML = genres_text;
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