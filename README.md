# Hybrid Django-React-Tailwind-Vite Setup
<img src="https://github.com/user-attachments/assets/04eba5fe-ed52-43b9-b444-37485b0892be" width="100%" height="350" />



Script to bootstrap hybrid django-react projects set up inspired by 
* The hybrid Python/Django/React Architecture as described by Cory Zue in [this article](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)
* Session based Auth for SPA/Django as described by Nik Tomazic in [this article](https://testdriven.io/blog/django-spa-auth/)
* The benefits of this set up is that you're able to use django features where you want and selectively use React. Also you don't have to worry about JWT as we're using normal django authentication.
## Quick Overview
1. React/Redux/Typescript (Javascript not recommended)
2. Vite is used for bundling
3. Tailwind CSS is used for styling
4. Quite opinionated but loosely coupled. The contents matter, structure doesn't
## Run The Script
1. You need to have node and a preferred dependency manager installed
2. Create a new virtual environment using `uv venv .venv` or equivalent
3. Install the package with `uv pip install django-react-tailwind-vite` or equivalent
4. Run the script with `dj-vite`, this will configure vite, redux and the react app
5. You can uninstall the package once you've verified successful installation
## Post Script Instructions
1. Install frontend packages by running `pnpm install` or equivalent
2. Install the python dependencies by running `uv pip install -r requirements.txt` or equivalent
3. The django project settings file has the following additions
   ```python
   #TEMPLATES["DIRS"] list in project/settings.py
   import os # top of file
   os.path.join(BASE_DIR, "templates")
   #static files section
   STATIC_ROOT = os.path.join(BASE_DIR.parent, "static")
   STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
   ]
   DJANGO_VITE = {
   "default": {
      "dev_mode": DEBUG, #to serve contents dynamically
      "manifest_path": os.path.join(BASE_DIR, "assets", "manifest.json"),
   }
   }
   #Allow Session Auth For React SPA
   CSRF_COOKIE_SAMESITE = "Lax"
   SESSION_COOKIE_SAMESITE = "Lax"
   CSRF_COOKIE_HTTPONLY = False  # False since we will grab it via universal-cookies
   SESSION_COOKIE_HTTPONLY = True

   SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 1 week
   ```
To further understand these values, read:
* [Nick Tomazic's article](https://testdriven.io/blog/django-spa-auth/) 
* [django-vite's documentation](https://github.com/MrBin99/django-vite)
4. For Making API Queries to your backend, use this snippet in your axios client
```javascript
import axios from "axios";
import Cookies from "universal-cookie";
const cookies = new Cookies();
async function restClient(url: string, method: string, data: any) {
  const response = await axios({
    url: url,
    method: method,
    data: data,
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": cookies.get("csrftoken"),
    },
    withCredentials: true,
  });
  return response;
}
```
The idea is to have csrf token as part of your headers. That's why you don't need JWT!
## Start Your Project
1. Run `pnpm run dev` and `./manage.py runserver` in separate terminal windows
2.  Navigate to `http://127.0.0.1:8000` and you will see the react home page loaded
 * Always use that url instead of localhost so that you use session auth
3. Try changing contents in `frontend/src/pages/home.tsx` to see live reload in action
4. The django urls connects to the react home via the `app/*` regex wildcard
5. Build on from there
## Production
1. Ensure you set the `DJANGO_VITE["default"]["dev_mode"]` to `False`
2. Run `pnpm run build`
3. Run `./manage.py collectstatic`
4. Deploy your app and django-vite will auto serve bundled files
