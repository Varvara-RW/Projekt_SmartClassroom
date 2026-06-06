const fs = require('fs').promises;

const files = [
    'hellig.txt',
    'druck.txt',
    'temper.txt'
];
files.forEach(file => {
    fs.readFile(`/home/pi01/Sensortest/Kombitest/${file}`, 'utf8')
        .then((data) => {
            console.log(`${file}: ${data}`);
        })

        .catch((err) => {
            console.error(`Error reading ${file}:`, err);
        });
});