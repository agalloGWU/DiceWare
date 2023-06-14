# Random Generator Stuff

## Online Random Number Generator

### Australian Site, Quantum
https://qrng.anu.edu.au/

#### Free API, no key required
https://qrng.anu.edu.au/contact/api-documentation/

##### sample api query/response
```
curl "https://qrng.anu.edu.au/API/jsonI.php?length=5&type=uint16"
{"type":"uint16","length":5,"data":[11047,3227,23825,23784,54966],"success":true}
```
A hex query/response
```
curl "https://qrng.anu.edu.au/API/jsonI.php?length=10&type=hex16&size=20"
{
  "type": "string",
  "length": 10,
  "size": 20,
  "data": [
    "55a35e9de82f173e7a8edadc4dffdfcd4423702c",
    "b0354fbc60d9ed67ede3b98060fba056e6538792",
    "67e67be0929fb6cea8286b6f5df23f475c2c64b1",
    "cf938d30574db00cbdbb3a9d4349767fbae6d60e",
    "4c17b628dbf7b8ba98937c5001eed4c55141ab55",
    "d2b1c70adc4ca43ddcdf4eed6e5a0f37962db8f9",
    "eb7e1318424364ac92cb8992a9db1b0ab99b5af6",
    "efa57cb834fab3a4e737234abcea9cdfeb32dae5",
    "14e338052a891ce1cdd2c6194ad59b188c0bbb1c",
    "77dd11b8269dfeaf7fd0b2c76082ac70b4a51f39"
  ],
  "success": true
}

```

** Hex allow for arbitrary block length (where was uint is either 8 or 16 bit, so max of 255 or 65535)
block length of 5 (ie, 0xFFFFF) results in a maximum of 1,048,575 which covers all the word lists so far




### Commercial Hardware

#### Cheap / USB
https://www.amazon.com/gp/product/B01KR2JHTA/ref=as_li_tl?ie=UTF8

#### Expensive
https://www.idquantique.com/random-number-generation/products/quantis-random-number-generator/


## Articles
https://blog.cloudflare.com/randomness-101-lavarand-in-production/
https://www.youtube.com/watch?v=1cUUfMeOijg


### seek random line in file (python)
https://www.tutorialspoint.com/random-access-to-text-lines-in-python-linecache



## Challenges
1. Read random line from file without loading entire file (seek?)
2. how much random data to get? (how many lines in the source word file?)
3. Case? (all lower, initial cap?, user selectable?)
4. Number of words (hard code to 3, but maybe user selectable)

For #2, the longest list I currently have is 370,105

