# My Python Extensions For Albert Launcher
Check [Albert Launcher](https://github.com/albertlauncher/albert)

## Unix Time Converter
[Extension File](https://github.com/mitrichius/albert-extensions/blob/master/ut.py)  

Extension to convert unixtime to datetime and vice versa. Triggered with 'ut ' and copied result. 

Dependencies: 
- `python-dateutil`

Examples:  
- `ut 1607252664` - result is `2020-12-06 14:04:24`  
- `ut 2020-12-06 11:00:23` - result is `1607241623`  
- `ut 2020-12-06` - result is `1607202000`

## Snippet
[Extension File](https://github.com/mitrichius/albert-extensions/blob/master/snippet.py)  

Extension to use snippets from simple text files (replacement of native plugin). 

File name is used as search string, content as snippet.

Examples:  
- `s tm` - result is `tmux new-session -d -s SessionName "command"`  
