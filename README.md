# project-devops-aws
### The idea of the project: upload ZIP files and extract the file and sort the contents of the file, of course I used many components as needed, I am attaching a picture of how the project is structured.
![alt text](https://github.com/mohammedabbas2000/project-devops-aws/blob/main/diagram.jpg)
### We will run a website with one page through which the file will be uploaded to the target s3 and from there a lambda trigger function will be activated that will extract the file and sort them within s3 within it to the right according to the type of each file that was in the uploaded ZIP file.
### Of course I have two ec2's through which I run the site's code and through which we access the site and there is a load balancer with a target group whose purpose is to lead the two ec2's addresses and if one goes down the other will work like this.

