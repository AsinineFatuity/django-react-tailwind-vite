# Hybrid Django-React Bootstrap
![image](https://github.com/user-attachments/assets/254d65ce-ba5c-41c4-832a-2a0a7f312556)

Script to bootstrap hybrid django-react projects set up inspired by 
* The hybrid Python/Django/React Architecture as described by Cory Zue in [this article](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)
* Session based Auth for SPA/Django as described by Nik Tomazic in [this article](https://testdriven.io/blog/django-spa-auth/)
* The benefits of this set up is that you're able to use django features where you want and selectively use React. Also you don't have to worry about JWT as we're using normal django authentication.
## Quick Overview
1. React/Redux/Typescript (Javascript not supported)
2. Webpack is used for bundling and Babel for the compiling
3. React Bootstrap for styling (Tailwind CSS coming soon)
4. Quite opinionated but loosely coupled. The contents matter, structure doesn't
## Run The Script
1. Install Django using your preferred package manager
2. Ensure you have installed node and npm
3. Run the script `python3 set_up_frontend.py`
4. This will configure webpack, redux and the react app and install all dependecies
## Post Script Instructions
1. Install frontend packages by running `pnpm install` or equivalent
2. Add this to your django project settings file
   ```python
   #TEMPLATES["DIRS"] list in project/settings.py
   import os # top of file
   os.path.join(BASE_DIR, "templates")
   #static files section
   STATIC_ROOT = os.path.join(BASE_DIR.parent, "static")
   STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
   ]
   #Allow Session Auth For React SPA
   CSRF_COOKIE_SAMESITE = "Lax"
   SESSION_COOKIE_SAMESITE = "Lax"
   CSRF_COOKIE_HTTPONLY = False  # False since we will grab it via universal-cookies
   SESSION_COOKIE_HTTPONLY = True

   SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 1 week
   ```

3. Add the following to your `.gitignore file`
```bash
node_modules/
dist/ 

# Ignore hot-update files and build output
static/hot/
static/index-bundle.js
static/index-bundle.js.map
static/main.css
static/main.css.map
static/index.html
static/index-bundle.js.LICENSE.txt
static/output.css

# Ignore the frontend environments
frontend/environments/.env.development
frontend/environments/.env.production
```
## Start Your Project
1. Run `npm start` and `./manage.py runserver` in separate terminal windows
2.  Navigate to `http://127.0.0.1:8000` and you will see the react home page loaded
3. Try changing contents in `frontend/src/pages/home.tsx` to see live reload in action
4. The django urls connects to the react home via the `app/*` regex wildcard
5. Build on from there
