## Installing Pygame
#### Checking for pip on macOS
```
$ pip --version
```

#### Installing Pygame on macOS
Install the libraries that Pygame depends on
```
$ brew install hg sdl sdl_image sdl_ttf
```
Install Pygame
```
$ pip3 install --user hg+http://bitbucket.org/pygame/pygame

```

Start a Python terminal session and import Pygame to check whether the installation was successful：
```
$ python3
>>> import pygame 
>>> 
```