# photo-booth-automation
I started this project to help me operate a photo booth for an event later this year. When I found myself editing images, superimposing overlays, and printing on the fly, I said that there had to be a way to automate this. I found some pre-made software online already, but it didn't quite fit my needs so this project came to be. I hope others may find a use for this in support of some small events they may have have.

Base directory watch structure built off of [Bruno Rocha's guide](http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html)

##### What this does:
Stacks an overlay image over incoming base images (in my use case from a tethered DSLR)

### What you'll need first
* [Python 2.7](https://www.python.org/downloads/)
* [Python PIP](https://bootstrap.pypa.io/get-pip.py) - If you don't already have PIP, download and run `python get-pip.py`

### Get the good stuff
```
git clone https://github.com/jwu910/photo-booth-automation.git
```

### Getting it working
From `/PATH/photo-booth-automation/`
```
pip install -r requirements.txt
```
You may want to replace overlay.png with your own overlay image. Currently overlay image needs to be named overlay.png.
**Overlay image should share the same dimensions as incoming images**

*- Scalable overlay images to come in the future. -*

### Hit the ground running
Navigate to `/PATH/photo-booth-automation/` and run
```
python watch.py [path/to/watch/directory/parent]
```
Program will run in root directory if none is given.

Note: see `/tests/README.md` for testing instructions.

### Taking pictures
Once the script is running, your `watch-folder/` should be the destination directory for any pictures being taken. Adobe Lightroom tethered shooting is a great option, but I found [entangle](https://entangle-photo.org/) was a good open source alternative for Linux.

Whether you decide to use this script to support tethered shooting or you just want to stack the overlay over images as a bulk process, it could be done. Your `watch-folder/` directory will handle this completely. If you have your tethered shooting to save directly to the `watch-folder/`, the images will be processed as soon as they are taken. You can also simply drop a copy of any images to be processed in the `watch-folder/` as well.

### Contributing

Please read [CONTRIBUTING.md](https://github.com/jwu910/photo-booth-automation/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jwu910/photo-booth-automation/tags).

### Authors

* **Joshua Wu** - *Initial work*

See also the list of [contributors](https://github.com/jwu910/photo-booth-automation/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

* Thanks to [AlChiu](https://github.com/AlChiu), [psyduc](https://github.com/psyduc), [phuchle](https://github.com/phuchle), and [rainrivas](https://github.com/rainrivas) for putting up with 24 hour activity notifications, catching my mistakes, and putting up with all of my review requests.

#### tl;dr:
1. `git clone https://github.com/jwu910/photo-booth-automation.git`
2. `cd /PATH/photo-booth-automation`
3. `pip install -r requirements.txt`
4. Replace overlay.png with your own.
5. `python watch.py`
6. Take or add pictures to `watch-folder/`
7. View images in `save-folder/`
