# Deploy
## Web service

### Local

```bash
export FLASK_APP=<PATH_API>
export FLASK_ENV=development
flask run
```  

### Heroku

```bash
heroku login
heroku git:remote -a medical-appointment-classifier
heroku apps:create medical-appointment-classifier
git push heroku master
```  

## Front-end

### Dependências
- Vue.js:
```bash
npm install -g @vue/cli
# OR
yarn global add @vue/cli
```  

### Local
```bash
cd www/
yarn install
yarn serve
```  

### GitHub pages
```bash
cd www/
yarn install
yarn build
```  
