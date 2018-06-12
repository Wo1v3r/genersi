# genersi

Genetic Algorithm to player Reversi

### Pre-requisites
Python 3

### Required Libraries
```bash
sudo pip install futures
sudo pip install treelib
```

### Running an experiment

- Set variable values at `settings/variables.py`

```bash
./run.sh
```

When running an experiment, a settings file will be produced under `./experiments/<date-of-experiment>/settings.txt` with the variables. 

At the end of your experiments, a report will be produced to the same folder for your convenience.

### Contesting against an item

- Copy an item to the root dir with the following name: `champion.tree.json`
- Run the contest script:
- `--computer` flag will run the item against the computer
- `--noob\--adept\--master(default)` will set difficulty of the computer
- You can set `GAME_COUNT` to set the amount of games the champion will play against the computer.


```bash
cp experiments/1/item.tree.json ./champion.tree.json
python3 ./contest.py
```


#### Known issues
- Some versions of python will try to load champion.tree.json when importing a module. You can just copy any of the json trees as described above.