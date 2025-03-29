// Dark Mode Toggle
document.getElementById('toggle-theme').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

function showSection(sectionId) {
        // Hide all sections
        document.getElementById("photo-gallery").classList.add("hidden");
        document.getElementById("linkedin-profile").classList.add("hidden");
        document.getElementById("github-profile").classList.add("hidden");

        // Show the selected section
        document.getElementById(sectionId).classList.remove("hidden");
    }

    document.getElementById("photos-btn").addEventListener("click", function () {
        showSection("photo-gallery");
    });

    document.getElementById("linkedin-btn").addEventListener("click", function () {
        showSection("linkedin-profile");
    });

    document.getElementById("github-btn").addEventListener("click", function () {
        showSection("github-profile");
    });