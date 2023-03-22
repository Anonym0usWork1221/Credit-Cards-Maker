Credit-Card-Maker
====
[![GitHub stars](https://img.shields.io/github/stars/Anonym0usWork1221/Credit-Cards-Maker.svg)](https://github.com/Anonym0usWork1221/Credit-Cards-Maker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Anonym0usWork1221/Credit-Cards-Maker.svg)](https://github.com/Anonym0usWork1221/Credit-Cards-Maker/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Anonym0usWork1221/Credit-Cards-Maker.svg)](https://github.com/Anonym0usWork1221/Credit-Cards-Maker/issues)
[![Python](https://img.shields.io/badge/language-Python%203-black.svg)](https://www.python.org)
[![MIT_LICENSE](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/)
![code size](https://img.shields.io/github/languages/code-size/Anonym0usWork1221/Credit-Cards-Maker)

-----------


**_Credit-Card-Maker_** is a command line tool used for creating thousands of credit cards of different type 

 *  Version : Final
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  Repository  : https://github.com/Anonym0usWork1221/Credit-Cards-Maker

------
Warning
====
**_The Python tool for creating valid credit cards is intended for educational purposes only. Any use of
this tool for illegal or fraudulent activities is strictly prohibited and may result in severe legal consequences.
The tool generates credit card numbers that may be valid, but it is not intended to be used for making actual
purchases or transactions. The creator of this tool is not responsible for any illegal or unauthorized use of the
tool. Use at your own risk and discretion._**

----
Requirements
===
* Python3.x and install pip requirements
* ``pip3 install -r requirements``
------

Usage
===
_generator.py [-h] [-c CARD_TYPE] [-l LIMIT_CARDS] [-i] [-o OUTPUT_FILE]_

**options**:  
*  -h, --help            show this help message and exit
*  -c   
  **_(CARD_TYPE) Select the card from available cards: ['AMEX', 'Discover', 'MasterCard', 'Visa'] e.g: -c MasterCard_** 
* -l  
   **_(LIMIT_CARDS)Type number of card to generate e.g: -l 5_**
* -i  
   **_(CARD_INFO) Fetch information of bank and related data e.g: -i_**
*  -o  
   **_(OUTPUT_FILE) output file name to store card details e.g: -o ./file.txt_**

----

Script Execution
===
* **Basic**
``python3 generator.py -c AMEX -l 5``  
* **_Advance_**
``python3 generator.py -c AMEX -l 5 -i -o ./cards.txt``

---
Features
===
* **_Validation of luhn_**
* **_Validate credit cards from [binlist](https://binlist.net/)_**
----
Available Cards Types
===
| Card Types |
|------------|
| AMEX       |
| Discover   |
| MasterCard |
| Visa       |

