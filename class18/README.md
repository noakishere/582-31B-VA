# How to install Flask

## Windows

### 1. Open Command prompt

```
python --version
```

or

```
py --version
```

### 2. Create your project folder

create your folder.

make sure your terminal is to address of that folder.

### 3. Create a virtual environment

Run this command inside the folder that you have your scripts

```
python -m venv .venv
```

### 4. Activate the virtual environment

```
.venv/bin/activate
```

or

```
.venv/Scripts/activate.bat
```

### 5. Install Flask

run the following command:

```
pip install Flask
```

if pip is not recognized, try the following command:

```
py -m pip install Flask
```

### 6. Verfiy Flask

```
flask --version
```

### 7. Run the Flask application

```
flask --app APPLICATION_NAME run --debug
```

or

```
python -m flask --app APPLICATION_NAME run --debug
```

---

# macOS

### 1. Open Terminal

```
python3 --version
```

### 2. Create your project folder

create your folder.

make sure your terminal is to address of that folder.

### 3. Create a virtual environment

Run this command inside the folder that you have your scripts

```
python3 -m venv .venv
```

### 4. Activate the virtual environment

```
. .venv/bin/activate
```

### 5. Install Flask

run the following command:

```
pip install Flask
```

if pip is not recognized, try the following command:

```
python3 -m pip install Flask
```

### 6. Verfiy Flask

```
flask --version
```

### 7. Run the Flask application

```
flask --app APPLICATION_NAME run --debug
```
