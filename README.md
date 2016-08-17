# KVRX Website

A KVRX website redesign using Django. Check out [the wiki](https://github.com/ianmobbs/KVRX-Website/wiki) for a full list of features implemented and features to come, and see [issues](https://github.com/ianmobbs/KVRX-Website/issues) to look at our to-do list!s

## Current Features

- Create users and grant/revoke certain permissions
- Groups (such as 'Deejay' or 'Staff') automatically grant specific permissions to users in those groups
- Store Deejays, Shows, Playlists, and Songs
  - Specific detail pages for Deejays and Shows (which show Playlists)
  - Specific page showing all Deejays and Shows
- Create your own pages with custom HTML on the KVRX template
  - Display link to pages on the front page

## Run locally

Mac instructions

1. Navigate to the project directory in terminal `$ cd Downloads/KVRX-Website/`
2. Install the requirements `$ pip install -r requirements.txt` (or `$ sudo pip install -r requirements.txt`)
3. Run `$ python manage.py runserver`
4. Navigate to `http://127.0.0.1:8000/` in your browser of choice.