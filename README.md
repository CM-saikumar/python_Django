# This is a Django project for Understanding and Deployment from scratch

# Creating a new Django Project 
Commad: django-admin startporject <project_name>

# Running the local server
command: python3 manage.py runserver

## creating a new app 
command: python manage.py startapp <app_name>


# Japan Travel Challenges - Django Project

This Django project provides a monthly travel challenge in Japan, suggesting destinations and activities for each month.

## Features
- **List of Monthly Challenges**: Displays all months with links to individual challenge pages.
- **Monthly Challenge Details**: Shows the travel destination and activities for a given month.
- **Number-Based Redirection**: Redirects users from `/challenges/{number}` to `/challenges/{month-name}`.
- **Proper Error Handling**: Returns a 404 response for invalid months.

## Technologies Used
- **Django**: Python-based web framework.
- **Function-Based Views (FBVs)**: Handles request-response logic.
- **Dynamic URL Routing**: Uses `<str:month>` and `<int:month>` parameters.
- **HTML Rendering in Views**: Generates lists dynamically in responses.

## Project Structure
```
project_root/
│── challenges/
│   │── views.py
│   │── urls.py
│── project_root/
│   │── settings.py
│   │── urls.py
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

## Future Enhancements
- Add **HTML Templates** instead of plain `HttpResponse`.
- Use a **Database Model** to store challenge data dynamically.
- Implement a **CSS-styled Frontend** for better UI/UX.

## Author
- **Sai Kumar K G**

