Hay dos redes neuronales de diferente arquitectura:
- Una capa con 10 hidden layers
- Dos capas con 5 hidden layers cada una

Se intenta coger la red definida si hay archivos llamados network.json y weights.h5 en la carpeta.
Si no encuentra ninguno, crea una red nueva con la configuración que esté puesta.

Hay una opción de trainingOnline:
- Si está en False, la red predice las acciones según sus Qvalues y no entrena.
- Si está en True, se hacen acciones random para ganar experiencias y entrenar.

python pacman.py -q PacmanQAgent -l mediumClassic -n 10