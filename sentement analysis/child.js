const { spawn } = require('child_process');
const python = spawn('python', ['sentement.py', 'product is terrible']);

python.stdout.on('data', (data) => {
  console.log('pattern: ', data.toString());
});

python.stderr.on('data', (data) => {
  console.error('err: ', data.toString());
});

python.on('error', (error) => {
  console.error('error: ', error.message);
});

python.on('close', (code) => {
  console.log('child process exited with code ', code);
});