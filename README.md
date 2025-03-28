## Order Managment

### **Instruction to upload & install app:**


| STEP | INSTRUCTION                                                                                             |
|-----:|---------------------------------------------------------------------------------------------------------|
|    1 | _Clone the repository to your PC:_<br/>```git clone git@github.com:AntiViruS90/python-project-49.git``` |
|    2 | _Go to repository:_<br/> ```cd python-project-49```                                                     |
|    3 | _Installation of dependencies:_ <br/>```make install```                                                 |
|    3 | _Generates Django migration files:_ <br/>```make migrations```                                          |
|    3 | _Applies migrations to the database:_ <br/>```make migrate```                                           |
|    4 | _Run the app on localhost:_ <br/>```make build```                                                       |


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
