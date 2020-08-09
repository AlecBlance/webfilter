# WebFilter

WebFilter is a python program for filtering large list of websites or subdomains based on responses.

**Filters**:
* Status code
* Response length


## Installation
```bash
git clone https://github.com/AlecBlance/webfilter.git
```

## Usage

Simple command for iterating through the list
```bash
python3 webfilter.py -s google.txt
```
With filter of **status codes**:
```bash
python3 webfilter.py -s google.txt -fc 404
python3 webfilter.py -s google.txt -fc 404 301 302
```
With filter of **response length**
```bash
python3 webfilter.py -s google.txt -fs 1231
python3 webfilter.py -s google.txt -fs 1231 4512
```

| Argument | Value                | Description                            |
|----------|----------------------|----------------------------------------|
| -s       | file (example.txt)   | List of websites/subdomains            |
| -fs      | Response length/size | Filter based on response length/size   |
| -fc      | Status code          | Filter based on status code            |
| -t       | No. of threads       | Number of threads                      |
| -v       | [No value]           | Verbose output                         |
| -c       | [No value]           | Clean output (no Status code and size) |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENSE)
