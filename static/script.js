document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#qrForm');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const data = document.querySelector('input[name="data"]').value;

        fetch('/generate_qr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `data=${encodeURIComponent(data)}`,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(responseText => {
            if (responseText !== '') {
                const qrImage = document.createElement('img');
                qrImage.src = `/static/${responseText}`;
                qrImage.alt = 'QR Code';
                document.getElementById('qrImageContainer').appendChild(qrImage);

                const downloadLink = document.createElement('a');
                downloadLink.href = `/download_qr/${responseText}`;
                downloadLink.innerHTML = 'Download QR Code';
                document.getElementById('qrImageContainer').appendChild(downloadLink);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
