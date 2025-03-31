# This is a Django project for Understanding and Deployment from scratch

# Creating a new Django Project 
```
Commad: django-admin startporject <project_name>
```

# Running the local server
```
command: python3 manage.py runserver
```

## creating a new app 
```
command: python manage.py startapp <app_name>
```

# Japan Travel Challenges - Django Project

This Django project provides a monthly travel challenge in Japan, suggesting destinations and activities for each month.

## Features
- **List of Monthly Challenges**: Displays all months with links to individual challenge pages.
- **Monthly Challenge Details**: Shows the travel destination and activities for a given month.
- **Number-Based Redirection**: Redirects users from `/challenges/{number}` to `/challenges/{month-name}`.
- **Proper Error Handling**: Returns a 404 response for invalid months.
- **Template-Based Rendering**: Uses Django templates to separate frontend from backend logic.

## Technologies Used
- **Django**: Python-based web framework.
- **Function-Based Views (FBVs)**: Handles request-response logic.
- **Dynamic URL Routing**: Uses `<str:month>` and `<int:month>` parameters.
- **HTML Rendering in Views**: Generates lists dynamically in responses.
- **CSS Styling**: Improves the appearance of the list of months and challenge pages.

## Project Structure
```
myDjangoLearning/
│── challenges/
│   │── static/
│   │   │── challenges/
│   │   │   │── challenge_page_style.css
│   │   │   │── challenges.css
│   │   │   │── schedule.css
│   │── templates/
│   │   │── challenges/
│   │   │   │── challenge.html
│   │   │   │── homePage.html
│   │── views.py
│   │── urls.py
│── myDjangoLearning/
│   │── settings.py
│   │── urls.py
│── static/
│   │── styles.css
│── templates/
│   │── 404.html
│   │── base.html
│── manage.py
```

## Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/japan-travel-challenges.git
   cd japan-travel-challenges
   ```
2. **Install Dependencies:**
   ```bash
   pip install django
   ```
3. **Run the Django Server:**
   ```bash
   python manage.py runserver
   ```
4. **Access the App:**
   Open `http://127.0.0.1:8000/challenges/` in your browser.

## URL Endpoints
| URL | Description |
|------|-------------|
| `/challenges/` | Displays the list of months with links |
| `/challenges/<str:month>/` | Shows the challenge for a given month |
| `/challenges/<int:month>/` | Redirects to the respective month's challenge |

## Concepts Used
- **URL Routing**: Maps URLs to views using `path()`.
- **Dynamic URL Parameters**: Extracts month names and numbers from URLs.
- **`reverse()` Function**: Generates URLs dynamically instead of hardcoding.
- **`HttpResponseRedirect`**: Redirects users based on numeric month input.
- **String Manipulation**: Formats month names properly.
- **Django Templates**: Uses challenge.html to render challenge pages dynamically.
- **Template Inheritance**: Allows reusing common HTML structures across pages.


## Understanding Templates

The **challenge.html** file inside `templates/challenges/` is responsible for displaying the monthly challenge information. Instead of returning raw HTML from views, Django templates separate the presentation from logic.

- **Dynamic Rendering**: The template receives data from views, such as the month, destination, and activities.
- **Reusability**: The same template structure is used for multiple months.
- **Separation of Concerns**: Keeps HTML separate from backend logic.
  

# Django `{% url %}` Template Tag

## Overview
The `{% url %}` template tag dynamically generates URLs in Django templates. This ensures that URLs remain consistent even if the `urls.py` configuration changes.

---

## 📌 Syntax
```django
{% url 'url_name' arg1 arg2 as var_name %}
```
OR
```django
<a href="{% url 'url_name' arg1 arg2 %}">Link Text</a>
```

---

## Explanation of Parameters
- `'url_name'`: The **name** of the URL pattern from `urls.py`.
- `arg1, arg2, ...`: Dynamic **arguments** to be passed in the URL (if required).
- `as var_name`: Stores the URL in a variable instead of rendering it directly. (Optional)

## Benefits of `{% url %}`
- Ensures URLs remain correct even if routes change.
- Avoids hardcoding URLs.
- Works with variables and loops dynamically.


## Template Inheritance in Django
- **Base Template**: Defines the common structure (like headers, footers) using blocks that can be overridden in child templates.

- **Child Template**: Inherits from the base template using `{% extends %}` and customizes content by overriding specific blocks with `{% block %}`.

- **Reusability**: Encourages code reuse, reducing duplication of common layout elements across different pages.

- **Maintainability**: Makes it easier to update common elements (like a header or footer) in one place (the base template) instead of all pages.

- **Settings**: Ensure that your templates are correctly configured in settings.py by defining the DIRS directory.

---
In `settings.py` under the project directory navigate to Templates list and add these permission so the the Django will understand the templates that was created.
```
'DIRS': [
    BASE_DIR / 'templates',
],
```
---

## Understanding `{% load static %}` and Linking CSS Files
### **Loading Static Files in Django**
Django provides the `{% load static %}` template tag to access static files like CSS, JavaScript, and images.

#### **Usage in a Template**
```django
{% load static %}
<link rel="stylesheet" href="{% static 'challenges/challenge_page_style.css' %}">
```
- `{% load static %}` → Enables static file handling in templates.
- `{% static 'path/to/file' %}` → Resolves the static file’s URL.

### **Using `{% block css_style %}` in Templates**
Instead of hardcoding styles, we can define a **block** in the base template and override it in child templates.

#### **Example in `base.html`**
```django
<head>
    {% block css_style %}{% endblock css_style %}
</head>
```

#### **Example in `challenge.html` (Child Template)**
```django
{% block css_style %}
    <link rel="stylesheet" href="{% static 'challenges/challenge_page_style.css' %}">
{% endblock css_style %}
```
- This ensures modular and reusable styling.

## **Static Files in Application vs. Project Level**
### **Static Files Inside an App (Application Level)**
- Each Django app can have its own `static/` folder.
- Example structure:
  ```
  challenges/
  ├── static/
  │   ├── challenges/
  │   │   ├── challenge_page_style.css
  ```
- **Usage:** `{% static 'challenges/challenge_page_style.css' %}`

### **Global Static Files (Project Level)**
- If you have static files **shared** across multiple apps, place them in a central `static/` directory at the project level.
- Example:
  ```
  myDjangoLearning/
  ├── static/
  │   ├── global.css
  ```
- **Usage:** `{% static 'global.css' %}`

## **Configuring `STATICFILES_DIRS` in `settings.py`**
Django needs to know where to find global static files. We define `STATICFILES_DIRS` for this purpose.

### **Adding `STATICFILES_DIRS` in `settings.py`**
```
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```
### **Difference Between `STATICFILES_DIRS`**
| Setting | Purpose |
|---------|---------|
| `STATICFILES_DIRS` | Defines additional directories where Django should look for static files during development. |



## Author
- **Sai Kumar K G**

