const fs = require('fs').promises;

async function readFileExample() {
  try {
    const hellig = await fs.readFile('/home/pi01/Sensortest/Kombitest/hellig.txt', 'utf8');
    console.log('File content:', hellig);
    const druck = await fs.readFile('/home/pi01/Sensortest/Kombitest/druck.txt', 'utf8');
    console.log('File content:', druck);
    const temper = await fs.readFile('/home/pi01/Sensortest/Kombitest/temper.txt', 'utf8');
    console.log('File content:', temper);
  } catch (err) {
    console.error('Error reading file:', err);
  }
}

readFileExample();