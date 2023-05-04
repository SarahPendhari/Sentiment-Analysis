const express=require('express')
const morgan=require('morgan')
const bodyParser=require('body-parser')
const { spawn } = require('child_process');
const path=require('path')

const app=express();
app.listen(3000)  
app.use(morgan('tiny'))
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set("view engine","ejs") 
app.use(express.static(path.join(__dirname, 'public')));


app.get('/',(req,res)=>{
    res.render('index',{"rate":""});
})

app.post('/',(req,res)=>{
    console.log(req.body.Textarea)
    const python = spawn('python', ['sentement.py', req.body.Textarea]);
    python.stdout.on('data', (data) => {
        console.log('pattern: ', data.toString(),req.body.textarea);
        res.render('index',{"rate": data.toString()});
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
      
})

