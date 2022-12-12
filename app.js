
const AWS = require ('aws-sdk');
var http = require('http');
var fs = require('fs');
var formidable = require('formidable');
const { exit } = require('process');
const { parse } = require("csv-parse");
require("dotenv").config();


const accessKeyId = -------------;
const secretAccessKey = --------------------;
  const s3 = new AWS.S3({
    accessKeyId,
    secretAccessKey,
  })
// html file containing upload form
var upload_html = fs.readFileSync("upload_file.html");
console.log('port 3000');
console.log(process.env.ABBAS)
http.createServer(function (req, res) {
    if (req.url == '/uploadform') {
      res.writeHead(200);
      res.write(upload_html);
      return res.end();
    } else if (req.url == '/fileupload') {
        var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            // oldpath : temporary folder to which file is saved to
            const imagePath = files.filetoupload.filepath
            const blob = fs.readFileSync(imagePath)
            const uploadedImage = s3.upload({
                Bucket: 'zip-s3',
                Key: files.filetoupload.originalFilename,
                Body: blob,
            }).promise()
            uploadedImage;
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(`upload success: ${files.filetoupload.originalFilename}`);
                
        });
    } 
}).listen(3000);
