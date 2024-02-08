# CreateTT

I have probably created a timetable at least 10 times or more, but I didn't stick to any of them because of my laziness. The timetable was repetitive and not fully random, so `CreateTT` comes to the rescue.

## How to use CreateTT ?

CreateTT uses two files: one containing the things you want to include in the timetable (the actions) and another file containing different times at which you want to do something.

Once the timetable has been generated, it can be saved as `SVG`, `HTML` or `TXT` files.

### What are `Action` and `Time` files ?

The `Actions` and `Time` files contain the data needed to create time table, because `CreateTT` doesn't know what user does, so these files are used as data sources.

These files can be in any formats, but below format is preferred.

```txt
Swim
Code
```

```txt
08:00 - 09:00
10:00 - 11:00
```

### How to set up `VENV` ?

```bash
git clone https://github.com/surajkareppagol/CreateTT
cd CreateTT
python3 -m venv venv
```

```bash
source ./venv/bin/activate
pip install -r requirements.txt
```

To deactivate,

```bash
deactivate
```

### How to use `CreateTT` through command line ?

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt
```

Provide both `Actions.txt` and `Time.txt` file paths,

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20Path.png)

---

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -d 4
```

Use `-d` option to provide number of days,

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20D.png)

---

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -d 4 -s svg
```

Use `-s` option to export in different formats, available are `svg`, `html`, `txt` or `all`.

---

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -i
```

Use `-i` option for an interactive mode, users will be able to select the actions.

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20I.png)

---

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -c
```

Use `-c` option for customized mode, control the table using `w`, `a`, `s`, `d` and change data.

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20C.png)

---

```bash
python3 src/main.py -h
```

Get some help with `-h`,

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20Help.png)

## Is the time fixed ?

No, in the console, you can edit the time and action by yourself. (Adding Soon)

## What is used in this ?

`Python 3`, and for styling in the terminal, the `Rich` library is used.

## What next ?

It is not a complete implementation; there are still many features that need to be added, such as the ability to customize the timetable, provide time in any format, etcetera.
