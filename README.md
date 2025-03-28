## Order Managment

### **Instruction to upload & install app:**


| STEP | INSTRUCTION                                                                                            |
|-----:|--------------------------------------------------------------------------------------------------------|
|    1 | _Clone the repository to your PC:_<br/>```git clone https://github.com/AntiViruS90/cafe_manager.git``` |
|    2 | _Go to repository:_<br/> ```cd cafe_manager```                                                         |
|    3 | _Installation of dependencies:_ <br/>```make install```                                                |
|    4 | _Generates Django migration files:_ <br/>```make migrations```                                         |
|    5 | _Applies migrations to the database:_ <br/>```make migrate```                                          |
|    6 | _Run the app on localhost:_ <br/>```make build```                                                      |
|    7 | _Go to localhost link:_ <br/>```http://127.0.0.1:8000/```                                              |


### **Tools in this ap**:

|  TOOLS | VERSION |
|-------:|---------|
| Python | 3.11    |
| Django | 5.1.7   |
|   Ruff | 0.11.2  |
| Pytest | 8.3.5   |


### **Commands for app**

|      Command | Description          |
|-------------:|----------------------|
| make install | Install dependencies |
|   make build | Build distributions  |
|    make test | Test coverage        |
|    make lint | PEP8 rules with ruff |
