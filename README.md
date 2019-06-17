# Mummy Money SPA
Vue.js SPA served over Flask microframework

* Python: 3.7.3
* Vue.js: 2.5.2
* vue-router: 3.0.1
* axios: 0.19.0

## Build Setup

``` bash
# install front-end
cd frontend
npm install

# serve with hot reload at localhost:8080
npm run dev


# install back-end
cd ../backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# serve back-end at localhost:5000
python app.py
```
