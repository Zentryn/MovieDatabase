window.onload = () => {
    var url = new URL(window.location.href);
    var next = url.searchParams.get("next");
    if (next !== null && next !== undefined) {
        document.getElementById('unauthorized-error').innerHTML = "Insufficient rights to view page.";
    }
}