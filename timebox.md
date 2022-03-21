{% include navigation.html %}

## Project Time box

| Name          | Requirement   | Tickets |
| ------------- | ------------- | --------| 
| Gabriel Boudreau       | Binary Search Function    | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/GabrielBoudreau) |
| Nadira Haddach         | Find Your Conselor Form   | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/nadirahaddach)   |
| Katie Hickman          | Random Password Generator | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/katiehickman)   |
| Tyler Hickman          | Calculator                | [Task](https://github.com/nadirahaddach/TheSlayers/issues/assigned/Tyler929)   |

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
