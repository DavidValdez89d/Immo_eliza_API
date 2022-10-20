# Immo_eliza_API
Immo_eliza_API

Simple FastApi demo.

Made to be deployed anywhere!

## Docker usage
In order to use this with Docker, you need to:

### 1. Build the image
```bash
# Give your image with the name of you choice, here I used "demo-api"
docker build -t demo-api .
``` 

### 2. Run the image
```bash
# -e PORT=5000 --> I give the container an env variable "PORT" with a value of 5000
# -p 5000:5000 --> Link your localhost's port 5000 to the container's port 5000
docker run -e PORT=5000 -p 5000:5000 -it demo-api
```

### 3. Try it!
You can now try your API at: [localhost:5000/docs](http://localhost:5000/docs)
