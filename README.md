# pretty-json
Just make JSON files really pretty

# Setup
```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

# Usage

## Dry Run (default)
```
python pretty.py json <filename>
```

## Overwriting File with Pretty Version
```
python pretty.py json <filename> --nodry_run
```
