document.querySelector('form').onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/predict', {
        method: 'POST',
        body: formData,
    });
    const data = await response.json();
    document.getElementById('output').innerText = JSON.stringify(data, null, 2);
};
