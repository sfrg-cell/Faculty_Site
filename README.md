# Faculty Website Project by Havryliuk Ioanna

## How to run project

1. Create virtual env
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Run the server
```bash
python manage.py runserver
```

## Endpoints

### Home
- `/` - homepage

### Programs
- `/programs/` - list of all programs
- `/programs/<int:id>/` - page of a program

### Departments
- `/departments/` - list of all departments
- `/departments/<int:id>/` - page of a department