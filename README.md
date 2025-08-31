# Jesus Lemus Personal Blog

tools: 
- Python 3.13
- Pelican
- NodeJs v24.6.0
- npm 11.5.1


## Set environment

```
npm install tailwindcss @tailwindcss/cli
pip install -r requirements.txt
```

## generate site steps

Open in each in different cli tap to run locally.

```
npx @tailwindcss/cli -i themes/simple-dev/static/css/main.css -o themes/simple-dev/static/css/style.css --watch
make regenerate
pelican --listen 
```

