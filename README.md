# About Crawl in it
Crawl_in_it is a python tool designed to discover URLs. It will help penteration tester and bugbounty hunters to save time, so that they don't have to go manually through all the pages. This tool will generate logs which can helps penetration tester and bugbounty hunters retrieve the results of actions they performed in the past and also will allow them to see the status codes and length of the pages, the tool has crawled through.

# Screeshots
![Crawl In It](https://user-images.githubusercontent.com/35112049/170496013-75fc2a89-0a36-426d-bee8-c6f26e163c51.gif)
![logs](https://user-images.githubusercontent.com/35112049/170496034-25374041-fe3c-42de-9a51-90e3ee4ad102.png)

# Installation

```
git clone https://github.com/itszeeshan/crawlinit.git
```

# Recommended Python
Crawl in it currently only supports python3.
* The recommended version for python3 is 3.10.x

# Installing Dependencies

### Installing on Windows
```
python -m pip install -r requirements.txt
```

### Installing on Linux
```
sudo pip install -r requirements.txt
```

### Installing Modules independently
```
pip install numpy
pip install argparse
pip install torch
pip install traitlets
pip install bs4
pip install requests
pip install typing_extensions
```
# Usage
Short | Long      | Description
------|-----------|-------------
-d    | --domain  | Domain to crawl into
-o    | --output  | Save results to file
-h    | --help    | Shows help message and exit

### For Example
* to generate help message
```
python Crawler.py -h
```
* Specifying domain for crawling
```
python Crawler.py -d hackerone.com
```
* Specifying domain for crawling and saving results into a file
```
python Crawler.py -d hackerone.com -o hackerone.txt
```

### The tool will automatically generate logs!

# Thank You and show some love :)
