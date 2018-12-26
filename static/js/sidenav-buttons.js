// Self invoking function, that includes a bootstrap class to an element,
// after changing templates with jinja2

(() => {
    var header = document.getElementById("sidenav-buttons");
    var btns = header.getElementsByClassName("nav-li");
    var pathname = window.location.pathname;
    for (var i = 0; i < btns.length; i++) {
        if (pathname.includes(String(i+1))) {
            btns[i].className += " active";
        }
    }
})();
