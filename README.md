# pacman-avd
To run QlEARNING, you can choose the map with -l <map_name>

-x means number of training stages

-n means the number of training stages + the number of test that will be done after training [they are visualized]

--save_qtable true to store the cross q table

--qtable_file the file to load/save the q table

--load_qtable load the qtable for the very first game [if training, uses it to train and if playing, uses it to play]. If training and not provided, trains from an empty qtable


Train and save [if do not want to save, just not add the last arguments]:
```
python pacman.py -p CrossQLearningAgent -n 1090 -l smallClassic -x 1040 --qtable_file cross_q_table --save_qtable --load_qtable
````
Not train, just play with pretrained q agent:
```
python pacman.py -p CrossQLearningAgent -n 5 -l smallClassic --qtable_file cross_q_table --load_qtable
````