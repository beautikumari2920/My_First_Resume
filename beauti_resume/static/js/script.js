document.getElementById("toggle-theme").addEventListener("click", function() {
    let body = document.body;
    let button = document.getElementById("toggle-theme");

    if (body.classList.contains("dark-mode")) {
        body.classList.remove("dark-mode");
        body.classList.add("sepia-mode");
        button.innerHTML = '<i class="fa-solid fa-sun"></i> Switch to Light Mode';
    } else if (body.classList.contains("sepia-mode")) {
        body.classList.remove("sepia-mode");
        body.classList.add("light-mode");
        button.innerHTML = '<i class="fa-solid fa-moon"></i> Switch to Dark Mode';
    } else if (body.classList.contains("light-mode")) {
        body.classList.remove("light-mode");
        body.classList.add("dark-mode");
        button.innerHTML = '<i class="fa-solid fa-adjust"></i> Switch to Sepia Mode';
    } else {
        body.classList.add("dark-mode");
        button.innerHTML = '<i class="fa-solid fa-sun"></i> Switch to Light Mode';
    }
});

document.getElementById("photos-btn").addEventListener("click", function() {
    let section = document.getElementById("photo-gallery");

    // Toggle the "hidden" class on each click
    section.classList.toggle("hidden");
});




