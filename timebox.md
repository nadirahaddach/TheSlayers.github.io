{% include navigation.html %}

## Project Time box

| Name          | Requirement   | Tickets |
| ------------- | ------------- | --------| 
| Gabriel Boudreau       | Binary Search Function    | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/GabrielBoudreau) |
| Nadira Haddach         | Find Your Conselor Form   | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/nadirahaddach)   |
| Katie Hickman          | Random Password Generator | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/katiehickman)   |
| Tyler Hickman          | Calculator                | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/Tyler929)   |

<br>

### [Coggle](https://coggle.it/diagram/YjzHqivA9yPIYTpw/t/-)
### [Wireframe](https://www.canva.com/design/DAE76xtfGkA/D13zxurkjVp3IqPmrqr9Iw/view?utm_content=DAE76xtfGkA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

<br>

### Find Your _______
```



    <body class="center">
    <br>
    <br>
    <h2>Find Your Counselor!</h2>
    <h5>Type your last name to find your counselor!</h5>

    <form method="POST" action="/councelorsearch/">
        <input type="text" id="lname" name="lname">
        <input type="submit" value="Submit" onclick="compare({{ input }})">
    </form>
    <br>
    <h4>Your counselor is: </h4><h3 id="counselor"></h3>

    <script>
        const input = '{{ input }}';
        let name = input.toUpperCase()

        const char1 = name.charCodeAt(0);
        let char2;
        let char3;

        <!-- we dont need to check if the first character is there bec the python does that -->

        if (name.charCodeAt(1).isNaN) {    <!-- if the second character is non existant -->
            char2 = 0
        } else {
            char2 = name.charCodeAt(1)
        }

        if (name.charCodeAt(2).isNaN) {    <!-- if the third character is non existant -->
            char3 = 0
        } else {
            char3 = name.charCodeAt(2)
        }

        <!-- uses decimal conversion of each letter one at a time to find where in the alphabet the last name is -->

        if ((char1 < 68) || (char1 <= 68 && char2 < 69) || (char1 <= 68 && char2 <= 69 && char3 <= 76)) {
            document.getElementById('counselor').innerHTML = "Mrs. Susie Kihneman";
        } else if (char1 <= 74) {
            document.getElementById('counselor').innerHTML = "Mr. Tim Roty";
        } else if ((char1 < 77) || (char1 <= 77 && char2 <= 84)) {
            document.getElementById('counselor').innerHTML = "Ms. Lauren Kennedy";
        } else if ((char1 < 83) || (char1 <= 83 && char2 < 72) || (char1 <= 83 && char2 <= 72 && char3 <= 65)) {
            document.getElementById('counselor').innerHTML = "Mr. Jesse Luna";
        } else {
            document.getElementById('counselor').innerHTML = "Mrs. Kathy Marron";
        }
    </script>

    <style>
        body,html,
        body {
            color: whitesmoke;
        }
        .center {
            text-align: center;
        }
    </style>
    </body>

```
<br>

### Random Password Generator
```
<div class="container">
    <p style="font-family: Baskerville; font-size: x-large; text-align: center">Generated Password</p>

    </script>
    <div>
        <textarea id="result" style="float: left" onchange
                  onpropertychange
                  onkeyuponpaste oninput="cs()" /></textarea>
        <button class="button" style="background-color: peachpuff; text-align: center" id="copyBtn"><img src=static/design/clipboard.png width="30" height="40"></button>
        <script>
            document.getElementById("copyBtn")
                .onclick = function() {
                let text = document.getElementById("result").value;
                navigator.clipboard.writeText(text)
                    .then(() => {
                        alert('Password copied to clipboard');
                    })
                    .catch(err => {
                        alert('Error in copying text: ', err);
                    });
            }
        </script>
        <p id="strength" style="margin-bottom: -55px; float:left; font-size: 25px"></p>
        <br>
        <br>
    </div>
    <div class="settings">
        <div class="setting">
            <label style="font-size: larger; font-family: Baskerville">Length</label>
            <input type="number" id="length" min="4" max="20" value="20" />
        </div>
        <div class="setting">
            <label style="font-size: larger; font-family: Baskerville">Capital Letters</label>
            <input type="checkbox" id="capital" checked />
        </div>
        <div class="setting">
            <label style="font-size: larger; font-family: Baskerville">Lowercase Letters</label>
            <input type="checkbox" id="lowercase" checked />
        </div>
        <div class="setting">
            <label style="font-size: larger; font-family: Baskerville">Numbers</label>
            <input type="checkbox" id="numbers" checked />
        </div>
        <div class="setting">
            <label style="font-size: larger; font-family: Baskerville">Special Characters</label>
            <input type="checkbox" id="symbols" checked />
        </div>
    </div>
    <button class="btn btn-large" id="generate">
        Submit!
    </button>
</div>


<script>

    const p = document.getElementById('strength');
    const resultEl = document.getElementById('result');
    const lengthEl = document.getElementById('length');
    const lowercaseEl = document.getElementById('lowercase');
    const generateEl = document.getElementById('generate');
    const capitalEl = document.getElementById('capital');
    const symbolsEl = document.getElementById('symbols')
    const numbersEl = document.getElementById('numbers')

    const cs = () => {
        const s = document.getElementById('result')
        const r = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,}$/;
        const t = r.test(s.value)
        if (t) {
            // password conforms to standards
            p.innerText = 'Strong'
            p.style.color = 'green'
        } else {
            p.innerText = 'Weak'
            p.style.color = 'red'
            // password doesn't
        }
    }


    const randomFunc = {
        lower: getRandomLower,
        capital: getRandomCapital,
        numbers: getRandomNumbers,
        symbols: getRandomSymbols,
    }

    generate.addEventListener('click', () => {
        const length = +lengthEl.value;
        const hasLower = lowercaseEl.checked;
        const hasCapital = capitalEl.checked;
        const hasNumbers = numbersEl.checked;
        const hasSymbols = symbolsEl.checked;
        const g = generatePassword(length, hasLower, hasCapital, hasNumbers, hasSymbols );

        resultEl.value = g
        cs()
    });

    function generatePassword(length, lower, capital, numbers, symbols) {
        let generatedPassword = '';
        const typesCount = lower + capital + numbers + symbols;
        const typesArr = [{lower}, {capital}, {numbers}, {symbols}].filter(item => Object.values(item)[0]);

        if(typesCount === 0) {
            return '';
        }

        for(let i=0; i<length; i+=typesCount) {
            typesArr.forEach(type => {
                const funcName = Object.keys(type)[0];
                generatedPassword += randomFunc[funcName]();
            });
        }
        const finalPassword = generatedPassword.slice(0, length);
        return finalPassword;
    }

    function getRandomLower() {
        return String.fromCharCode(Math.floor(Math.random() * 26) + 97);
    }
    function getRandomCapital() {
        return String.fromCharCode(Math.floor(Math.random() * 26) + 65);
    }
    function getRandomNumbers() {
        return +String.fromCharCode(Math.floor(Math.random() * 10) + 48);
    }
    function getRandomSymbols() {
        const symbols = '!@#$%^&*'
        return symbols[Math.floor(Math.random() * symbols.length)];
    }
</script>
```
