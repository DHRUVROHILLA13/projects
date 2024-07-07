let profiles = [];
let currentIndex = 0;

async function fetchCatImages() {
    const apiKey = 'your API key';
    try {
        const response = await fetch('https://api.thecatapi.com/v1/images/search?limit=10', {
            headers: {
                'x-api-key': apiKey
            }
        });
        const data = await response.json();
        data.forEach((cat, index) => {
            profiles.push({ name: `Cat ${profiles.length + 1}`, image: cat.url });
        });
        updateProfile();
    } catch (error) {
        console.error("Error fetching cat images:", error);
    }
}

function updateProfile() {
    if (profiles.length === 0) {
        fetchCatImages();
        return;
    }
    const profile = profiles[currentIndex];
    document.getElementById("profile-image").src = profile.image;
    document.getElementById("profile-name").textContent = profile.name;
}

function showMessage(message) {
    const floatingMessage = document.getElementById("floating-message");
    floatingMessage.textContent = message;
    floatingMessage.style.opacity = 1;
    setTimeout(() => {
        floatingMessage.style.opacity = 0;
    }, 2000);
}

function pass() {
    showMessage("Meh..." );
    currentIndex = (currentIndex + 1) % profiles.length;
    updateProfile();
}

function smash() {
    showMessage("Nice cat!" );
    currentIndex = (currentIndex + 1) % profiles.length;
    updateProfile();
}

window.onload = fetchCatImages;
