# pacman-avd
To run QlEARNING, you can choose the map with -l <map_name>

-x means number of training stages

-n means the number of training stages + the number of test that will be done after training [they are visualized]

```
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 60 -n 61 -l trickyClassic
````
