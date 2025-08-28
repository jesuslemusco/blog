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
npx @tailwindcss/cli -i themes/personal/static/css/input.css -o themes/personal/static/css/output.css --watch
make regenerate
pelican --listen 
```

