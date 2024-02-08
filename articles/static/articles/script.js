/*function darkMode() {
    var darkMode_button = document.getElementById('darkMode_button');
    
    if (darkMode_button.innerText === 'Dark Mode') {
        darkMode_button.innerText = 'Light Mode';
        document.body.classList.add("dark");
        document.body.classList.remove("light");
    } else {
        darkMode_button.innerText = 'Dark Mode';
        document.body.classList.add("light");
        document.body.classList.remove("dark");
    }
}*/

function showHide(input_id) {
    var element = document.getElementById(input_id)
    element.classList.toggle("invisible")
}

function changeSource(source_link) {
    var img = document.getElementById("varying_image")
    img.src = source_link
}