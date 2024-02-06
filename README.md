# CreateTT

I have probably created a timetable at least 10 times or more, but I didn't stick to any of them because of my laziness. The timetable was repetitive and not fully random, so `CreateTT` comes to the rescue.

## How to use CreateTT ?

CreateTT uses two files: one containing the things you want to include in the timetable (the actions) and another file containing different times at which you want to do something. So, in the end, it is just a random action chooser from the list.

Once the timetable has been generated, it will be converted into a SVG file and a HTML file.

The `Actions` and `Time` files can be in any formats, but below format is prepared.

```txt
Swim
Code
```

```txt
08:00 - 09:00
10:00 - 11:00
```

Create `venv` using,

```bash
git clone https://github.com/surajkareppagol/CreateTT
cd CreateTT
python3 -m venv venv
```

```bash
source ./venv/bin/activate
pip install -r requirements.txt
```

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt
```

Provide both `Actions.txt` and `Time.txt` file paths,

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20Path.png)

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -d 4
```

Use `-d` option to add optional days,

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20D.png)

```bash
python3 src/main.py -h
```

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20Help.png)

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -d 4 -s svg
```

Use `-s` option to export in different formats, available are `svg`, `html`, `txt`.

```bash
python3 src/main.py -a ./Actions.txt -t ./Time.txt -i
```

Use `-i` option for an interactive mode, users will be able to select the actions.

![Time Table](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/CreateTT/CreateTT%20I.png)

## Is the time fixed ?

No, in the console, you can edit the time and action by yourself. (Adding Soon)

## What is used in this ?

`Python 3` is the main component; then, for styling in the terminal, the `Rich` library is used.

## What next ?

It is not a complete implementation their are still many features that needs to be added, such as the ability to customize time table, provide time in any format, proper management of console arguments, etcetera.
